# **nogil-http** for Python
> An HTTP server that achieves true parallelism without using multi-processing, implemented in pure Python.

## **0%** GIL, **100%** Parallelism
> How does it work?

`nogil-http` achieves true parallelism by \
utilizing the new free-threading feature in \
[CPython](https://github.com/python/cpython) 3.13 and later.

free-threading in Python allows multiple threads to run parallel \
without the GIL getting in their way, as it is disabled by default.

**However**, this requires [CPython](https://github.com/python/cpython)
to be built with support for \
free-threading by using the `--disable-gil` configure option.

Free-threaded Python is provided as a separate binary. \
The binary is typically named `python3.Xt`, where `X` is the major \
version number, so for Python 3.14, the binary would be named `python3.14t`.

> See the article [Python support for free threading](https://docs.python.org/3/howto/free-threading-python.html)

On [Fedora Linux](https://fedoraproject.org/), the free-threaded Python binaries are by the package, \
`python3-freethreading` or similarly named.
