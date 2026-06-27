import os

from ._internal import NoGILHTTPHandler, NoGILHTTPServer


class App:
    server: NoGILHTTPServer

    def __init__(
        self, server_address: tuple[str, int], max_workers: int = os.cpu_count() or 4
    ):
        self.server = NoGILHTTPServer(server_address, NoGILHTTPHandler, max_workers)

    def run(self):
        self.server.serve_forever()
