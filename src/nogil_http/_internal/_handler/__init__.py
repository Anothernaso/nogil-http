from http.server import BaseHTTPRequestHandler
from typing import TYPE_CHECKING, cast

from ._process import process_request

if TYPE_CHECKING:
    from .._server import NoGILHTTPServer


class NoGILHTTPHandler(BaseHTTPRequestHandler):
    def nogil_server(self) -> NoGILHTTPServer:
        return cast(NoGILHTTPServer, self.server)

    def do_GET(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()

    def do_HEAD(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()

    def do_POST(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()

    def do_PUT(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()

    def do_DELETE(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()

    def do_OPTIONS(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()

    def do_CONNECT(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()

    def do_TRACE(self) -> None:
        self.nogil_server().executor.submit(process_request, self).result()
