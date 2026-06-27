import os
from concurrent.futures import ThreadPoolExecutor
from http.server import HTTPServer
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from ._handler import NoGILHTTPHandler


class NoGILHTTPServer(HTTPServer):
    executor: ThreadPoolExecutor

    def __init__(
        self,
        server_address: tuple[str, int],
        handler_class: Type[NoGILHTTPHandler],
        max_workers: int,
    ):
        super().__init__(server_address, handler_class)

        self.executor = ThreadPoolExecutor(max_workers=max_workers)
