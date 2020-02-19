# SiteMap

Implements a new "SiteMap" data structure by extending the Python builtin `set` (eventually `abc.MutableSet`).

The use case is to create a proper, self-synchronising, 3rd party library data structure for working with sitemaps at scale, for convenience use in ORMs, db transformations or dataset analysis of web UIs.

## Usage

Run `python3 main.py` in a shell.

Run tests by running `python3 -m unittest test_sitemap.py` in a shell.

## TODO (SiteMap object)

* Transfer TODO into GitHub issues
* (PRIORITY!) Replace `set` inheritance with `abc.collections.MutableSet` abstract inheritance.
* Add validation - a user should never be able to append a non-url into a sitemap data structure.
* Come up with some interesting introspective functions
* Come up with more interesting behaviour in overloaded builtins.
* Define idempotent behaviour between sitemap objects. Joins? Filtering?
* Implement ContextManager for the object to clean up after itself.

## TODO (project)

* Transfer TODO into GitHub issues
* Come up with a name...
* Add an API to our backend, maybe with Flask. / can list options, /enqueue can add to some kind of task queue of targets to scrape.
* More tests!

## Research

* Research [django-sitemap](https://docs.djangoproject.com/en/3.0/ref/contrib/sitemaps/). How do they do it?
* Research urllib - they probably deal with something similar.
