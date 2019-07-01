## Using a custom OpenAPI specification file

You can place a custom OpenAPI specification file in this
directory. The file must be in JSON format, and must be named `spec3.json`.

If this files is present, the test suite will start its own telnyx-mock
process on a random available port. In order for this to work, `telnyx-mock`
must be on the `PATH` in the environment used to run the test suite.
