#!/bin/python3

import logging
import argparse

from sitemap import SiteMap
from parse_args import parse_args
from monitoring import serve

logging.basicConfig()
logger = logging.getLogger("sitemap")

if __name__ == '__main__':
    args = parse_args()
    logger.setLevel(args.verbosity * 10)

    sitemap = SiteMap(
        url=args.host,
        max_workers=30,
        worker_timeout=6
    )()

    sitemap.dump_to_file(args.outfile) if args.outfile else None
    serve(sitemap, args.metrics) if args.metrics else None
