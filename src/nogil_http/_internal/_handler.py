from http.server import BaseHTTPRequestHandler
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from ._server import NoGILHTTPServer


class NoGILHTTPHandler(BaseHTTPRequestHandler):
    def nogil_server(self) -> NoGILHTTPServer:
        return cast(NoGILHTTPServer, self.server)
