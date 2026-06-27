from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._handler import NoGILHTTPHandler


def process_request(handler: NoGILHTTPHandler) -> None:
    pass
