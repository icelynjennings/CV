import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "host",
        help='url of the remote host from which to generate a sitemap'
    )
    parser.add_argument(
        "-v", "--verbosity",
        action="store",
        help="increase output verbosity",
        default=1,
        type=int
    )
    parser.add_argument(
        "-of", "--outfile",
        nargs='?',
        const='',
        type=str
    )
    parser.add_argument(
        "-m", "--metrics",
        action="store",
        nargs='?',
        help="serve metrics at given port (default 8000)",
        const=8000,
        type=int
    )

    return parser.parse_args()
