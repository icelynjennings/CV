#!/bin/python3

import sys
import logging
import datetime
import argparse

from sitemap import SiteMap
from parse_args import parse_args


def run(args) -> SiteMap:
    sitemap = SiteMap(
        url=args.host,
        max_workers=30,
        worker_timeout=6
    )()
    return sitemap


if __name__ == '__main__':
    args = parse_args()

    if args.verbosity > 0:
        logging.basicConfig()
        logger = logging.getLogger("sitemap")
        logger.setLevel(logging.DEBUG)

    sitemap = run(args)

    if args.outfile:
        sitemap.dump_to_file(args.outfile)
