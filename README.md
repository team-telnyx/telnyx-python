# Telnyx Python Library

[![image](https://img.shields.io/pypi/v/telnyx.svg)][pypi]
[![image](https://img.shields.io/pypi/l/telnyx.svg)][pypi]
[![image](https://img.shields.io/pypi/pyversions/telnyx.svg)][pypi]
[![Build Status](https://travis-ci.org/team-telnyx/telnyx-python.svg?branch=master)][travis]
[![Coverage Status](https://coveralls.io/repos/github/team-telnyx/telnyx-python/badge.svg?branch=master)][coveralls]

[pypi]: https://pypi.org/project/telnyx/
[travis]: https://travis-ci.org/team-telnyx/telnyx-python
[coveralls]: https://coveralls.io/github/team-telnyx/telnyx-python?branch=master

The Telnyx Python library provides convenient access to the Telnyx API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Telnyx
API.

## Documentation

See the [API Reference](https://developers.telnyx.com/docs/api/v2/overview) and the [Setup Guides](https://developers.telnyx.com/docs/v2/development/dev-env-setup).

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

    pip install --upgrade telnyx

Install from source with:

    python setup.py install

### Requirements

- Python 2.7 or 3.5+ (PyPy supported)

## Usage

The library needs to be configured with your account's API Key which is
available in your [Telnyx Dashboard][api-keys]. Set `telnyx.api_key` to its
value:

```python
import telnyx
telnyx.api_key = "KEY01234_yoursecretkey"

# list messaging profies
telnyx.MessagingProfile.list()

# retrieve single messaging profile
telnyx.MessagingProfile.retrieve("123")
```

You can read more about our API Keys [here](https://developers.telnyx.com/docs/v2/development/authentication).

### Per-Request Configuration

For apps that need to use multiple keys during the lifetime of a process,
it's also possible to set a per-request key and/or account:

```python
import telnyx

# list messaging profiles
telnyx.MessagingProfile.list(
    api_key="super-secret...",
)

# retrieve single messaging profile
telnyx.MessagingProfile.retrieve(
    "123",
    api_key="other-secret...",
)
```

### Configuring an HTTP Client

The library can be configured to use `urlfetch`, `requests`, `pycurl`, or
`urllib2` with `telnyx.default_http_client`:

```python
client = telnyx.http_client.UrlFetchClient()
client = telnyx.http_client.RequestsClient()
client = telnyx.http_client.PycurlClient()
client = telnyx.http_client.Urllib2Client()
telnyx.default_http_client = client
```

Without a configured client, by default the library will attempt to load
libraries in the order above (i.e. `urlfetch` is preferred with `urllib2` used
as a last resort). We usually recommend that people use `requests`.

### Configuring a Proxy

A proxy can be configured with `telnyx.proxy`:

```python
telnyx.proxy = "https://user:pass@example.com:1234"
```

### Configuring Automatic Retries

Number of automatic retries on requests that fail due to an intermittent
network problem can be configured:

```python
telnyx.max_network_retries = 2
```

### Reserved word keyword arguments
The Telnyx API includes `from` as an attribute that can be set on messages.
`from` is also a reserved word in Python. If you would like to use keyword
arguments where an argument is a reserved word you can add the suffix `_` e.g.

```
telnyx.Messages.create(
    to="+18665550001",
    from_="+18445550001",
    text="Foo"
)
```

The argument will be automatically rewritten to `from` in the keyword arguments dict.

> Pro Tip: You can alternatively unpack a dictionary like so:
> ```python
> message = {
>     "from": "+18445550001",
>     "to": "+18665550001",
>     "text": "Foo",
> }
> telnyx.Messages.create(**message)
> ```

### Logging

The library can be configured to emit logging that will give you better insight
into what it's doing. The `info` logging level is usually most appropriate for
production use, but `debug` is also available for more verbosity.

There are a few options for enabling it:

1. Set the environment variable `TELNYX_LOG` to the value `debug` or `info`

   ```
   $ export TELNYX_LOG=debug
   ```

2. Set `telnyx.log`:

   ```py
   import telnyx
   telnyx.log = 'debug'
   ```

3. Enable it through Python's logging module:
   ```py
   import logging
   logging.basicConfig()
   logging.getLogger('telnyx').setLevel(logging.DEBUG)
   ```

### Writing a Plugin

If you're writing a plugin that uses the library, we'd appreciate it if you
identified using `telnyx.set_app_info()`:

```py
telnyx.set_app_info("MyAwesomePlugin", version="1.2.34", url="https://myawesomeplugin.info")
```

This information is passed along when the library makes calls to the Telnyx
API.

## Development

The test suite depends on [telnyx-mock], so make sure to fetch and run it from a
background terminal ([telnyx-mock's README][telnyx-mock] also contains
instructions for installing via Homebrew and other methods):

    go get -u github.com/team-telnyx/telnyx-mock
    telnyx-mock

Install [pipenv][pipenv], then install all dependencies for the project:

    pipenv install --dev

Run all tests on all supported Python versions:

    make test

Run all tests for a specific Python version (modify `-e` according to your Python target):

    pipenv run tox -e py27

Run all tests in a single file:

    pipenv run tox -e py27 -- tests/api_resources/abstract/test_updateable_api_resource.py

Run a single test suite:

    pipenv run tox -e py27 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource

Run a single test:

    pipenv run tox -e py27 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource::test_save

Run the linter with:

    make lint

The library uses [Black][black] for code formatting. Code must be formatted
with Black before PRs are submitted, otherwise CI will fail. Run the formatter
with:

    make fmt

### Adding a new endpoint

1. Define a class for the object that the endpoint interacts with under
`telnyx/api_resources/`. The path name singularized should typically match
the record type of the object returned e.g. `/v2/available_phone_numbers`
returns a list of objects with the record_type `available_phone_number`.
Inherit from the classes that define the behavior available on the endpoint,one or more of `CreateableAPIResource`, `DeletableAPIResource`,
`ListableAPIResource`, `UpdateableAPIResource`.

2. Import your class in `telnyx/api_resources/__init__.py`.

3. Add your new class to the `OBJECT_CLASSES` block in `telnyx/util.py`.

4. Add tests for your new class under `tests/api_resources/`.


[api-keys]: https://portal.telnyx.com/#/app/auth/v2
[black]: https://github.com/ambv/black
[pipenv]: https://github.com/pypa/pipenv
[telnyx-mock]: https://github.com/team-telnyx/telnyx-mock

## Releasing

1. Update version in
    * `setup.py`  (in the `setup()` call, the `version` kwarg)
    * `telnyx/__init__.py`  (the `__version__` string)
2. Create new branch, add changes, commit, and push
3. Ensure commit passes tests in [Travis][travis-telnyx-python]
4. Tag that commit with `git tag -a v{VERSION} -m "Release v{VERSION}"`, and push the tag `git push --follow-tags`
5. Ensure checked out copy is entirely clean (best to create a new environment...)
6. `make dists`
7. *If you haven't done it before*, download the upload API keys from LastPass (search for "pypi") and put the contents between "PYPIRC FILE" tags into `~/.pypirc-telnyx`.
8. `make testupload`, check that it looks OK on PyPI and that it's installable via `pip`.
9. `make liveupload`, repeat checks for live version.
10. Ta-da.

[travis-telnyx-python]: https://travis-ci.org/team-telnyx/telnyx-python


## Acknowledgments

The contributors and maintainers of Telnyx Python would like to extend their
deep gratitude to the authors of [Stripe Python][stripe-python], upon which
this project is based. Thank you for developing such elegant, usable, and
extensible code and for sharing it with the community.

[stripe-python]: https://github.com/stripe/stripe-python

<!--
# vim: set tw=79:
-->
