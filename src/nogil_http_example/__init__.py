from nogil_http import App


def main() -> None:
    app = App(("0.0.0.0", 8000))
    app.run()
