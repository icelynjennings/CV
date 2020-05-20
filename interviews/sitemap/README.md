# SiteMap

Implements a new "SiteMap" data structure by extending the Python builtin `set` (eventually `abc.MutableSet`).

The use case is to create a proper, self-synchronising, 3rd party library data structure for working with sitemaps at scale, for convenience use in ORMs, db transformations or dataset analysis of web UIs.

## Usage

Run `python3 main.py [-h] [-v VERBOSITY] [-of [OUTFILE]] [-m [METRICS]] host` in a shell.

## Metrics

Passing the `--metrics [PORT]` argument runs an http server which outputs metrics scrapable by Prometheus. This server is NOT PRODUCTION READY (due to [Issue #20](https://github.com/icelynjennings/sitemap/issues/20)) and currently serves as a stub.

## Test

Run `make test` in a shell.

## Contributing

Take a look at some of the [issues](https://github.com/icelynjennings/sitemap/issues), fork the repository and assign @icelynjennings to the merge request.
