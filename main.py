#!/bin/python3

import sys
import logging
import datetime
import argparse

from sitemap import SiteMap


def run(args) -> SiteMap:
    sitemap = SiteMap(
        url=args.host,
        max_workers=30,
        worker_timeout=6
    )()
    return sitemap


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "host", help='url of the remote host from which to generate a sitemap')
    parser.add_argument("-v", "--verbosity", action="store",
                        help="increase output verbosity", default=0, type=int)
    parser.add_argument("-of", "--outfile", nargs='?', const='', type=str)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.verbosity > 0:
        logging.basicConfig()
        logger = logging.getLogger("sitemap")
        logger.setLevel(logging.DEBUG)

    sitemap = run(args)

    if args.outfile:
        sitemap.dump_to_file(args.outfile)
