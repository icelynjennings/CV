# SiteMap

Implements a new "SiteMap" data structure by extending the Python builtin `set` (eventually `abc.MutableSet`).

The use case is to create a proper, self-synchronising, 3rd party library data structure for working with sitemaps at scale, for convenience use in ORMs, db transformations or dataset analysis of web UIs.

## Usage

Run `python3 main.py [-h] [-v VERBOSITY] [-of [OUTFILE]] host` in a shell.

## Test

Run `python3 -m unittest test_sitemap.py` in a shell.

## Contributing

Take a look at some of the issues, fork the repository and assign @icelynjennings to the merge request.
