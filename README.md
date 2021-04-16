Simple set of files to interact with the Meater API.

To get started.

Assumes you have pipenv installed.

Run `pipenv install` to install all dependencies and create a virtual environment for your project.

Copy `.env.defaults` to `.env` and replace `MEATER_EMAIL` and `MEATER_PASSWORD` with your Meater account credentials.

Run `pipenv run getkey` to get your API key. This will also add it to your `.env` file as `MEATER_KEY`.

To get information about currently connected devices and cooks (if any) run `pipenv run devices`.

To use the Meater class.
Import with `from meater import Meater`
Create a new instance, optionally passing True of False, True converts all temps to Fahrenheit, False leaves them in Celcius.
`meater = Meater(True)`

Use `meater.get_devices()` to get information about all cloud connected probes and their associated cooks.

Use `meater.get_device(DEVICEID)` to get the information about a single connected probe by its id