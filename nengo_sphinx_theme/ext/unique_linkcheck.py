"""
A version of the Sphinx linkchecker that only checks unique URLs.

The idea is that this will cut down on the number of outgoing requests, avoiding
throttling from external sites.
"""

from docutils import nodes

from sphinx.builders import linkcheck
from sphinx.util.nodes import get_node_line


class UniqueLinkChecker(linkcheck.CheckExternalLinksBuilder):
    name = "unique_linkcheck"

    def init(self):
        super().init()

        self.unique_uris = set()

    def write_doc(self, docname, doctree):
        n = 0

        # reference nodes
        for refnode in doctree.traverse(nodes.reference):
            if "refuri" not in refnode:
                continue
            uri = refnode["refuri"]
            if uri not in self.unique_uris:
                self.unique_uris.add(uri)
                lineno = get_node_line(refnode)
                self.wqueue.put((uri, docname, lineno), False)
                n += 1

        # image nodes
        for imgnode in doctree.traverse(nodes.image):
            uri = imgnode["candidates"].get("?")
            if uri and "://" in uri and uri not in self.unique_uris:
                self.unique_uris.add(uri)
                lineno = get_node_line(imgnode)
                self.wqueue.put((uri, docname, lineno), False)
                n += 1

        done = 0
        while done < n:
            self.process_result(self.rqueue.get())
            done += 1

        if self.broken:
            self.app.statuscode = 1


def setup(app):
    app.add_builder(UniqueLinkChecker)
