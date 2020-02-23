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
        default=0,
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
        help="serve metrics at given port (default 8080)",
        default=8080,
        type=int
    )

    return parser.parse_args()
