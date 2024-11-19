from argparse import ArgumentParser

from ..cookies import browsers

def gui_parser():
    parser = ArgumentParser(description="Run the GUI")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="hostname")
    parser.add_argument("--port", "-p", type=int, default=8080, help="port")
    parser.add_argument("--debug", "-d", "-debug", action="store_true", help="debug mode")
    parser.add_argument("--ignore-cookie-files", action="store_true", help="Don't read .har and cookie files.")
    parser.add_argument("--cookie-browsers", nargs="+", choices=[browser.__name__ for browser in browsers],
                            default=[], help="List of browsers to access or retrieve cookies from.")
    return parser