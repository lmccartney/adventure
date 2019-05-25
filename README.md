# A Toy Django Project

There isn't much point to this project as of yet, the inspiration was sparked by
the fact that most of my work cannot be published and so I wanted something to 
point to that could at least begin speak to my expertise. Perhaps as I fiddle 
around with things purpose will be found, however for now it's basically a 
harebrained attempt to show the competencies I've developed.

## Configuring Custom Settings

The base settings file is imported from `adventure/settings/environments/` using
the environment variable `DJANGO_ENV` to select which file to import (i.e.
`DJANGO_ENV=development` will use `.../environments/development.py`). If 
`DJANGO_ENV` is not set, the default is development.

To override or configure your own custom settings, create the file
`adventure/settings/local.py` and include whatever settings you wish. This
will override or append to the default settings. Please do not commit this file.

## Documentation

I've started using Sphinx for my documenation tool, for which the Makefile can
be found in `docs/`. To generate docs, run make html in that directory and they
will be constructed locally in `docs/build/`. This directory is (or will be)
ignored so please do not commit these files. As this project progresses, I will
setup Sphinx-Autodoc with some custom configurations to generate documentation
automagically from docstrings. Given this, please use docstrings liberally and
preferably in reStructuredText format.

## Code Quality

I'm using Codacy because it's easy and free! I might setup my own linting and
code inspection tools later, but this is easy for now and gets to the point
that I highly value code quality.
