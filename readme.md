# Denver Concert Application
For Applications of Software Architecture for Big Data class

## Tech Used
- Python
- Flask
- Heroku
- Github Actions

## Class-specific info

### Continuous Integration & Continuous Delivery
We are using Github Actions to run our unit and integration tests on every push to the main branch. We are also using Github Actions to deploy our application to Heroku on every push to the main branch.

See .github/workflows/main.yml for more information.

### Data Collection (Ticketmaster Discovery API)
- [Ticketmaster Discovery API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/)

You'll need to register and get an API key and add it to your environment variables.  Both in the application as well as in Heroku or your deployment environment.


## Using the Application
### How to run locally
`flask --app applications.web.app run --debug`

### Running the data collector
`python applications/data_collection/app.py`

### Running the data analyzer
`python applications/data_analyzer/app.py`

### Troubleshooting
#### If you get an error about the app not being found, try:
[chrome://net-internals/#sockets](chrome://net-internals/#sockets) -> Flush socket pools

### Testing
#### To run the unit tests, run:
`python -m unittest discover -s tests/unit -p '*_test.py'`
#### To run the integration tests, run:
`python -m unittest discover -s tests/integration -p '*_test.py'`

## Additional Information
### Useful Links
- [Python Virtualenv Mac](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Flask Testing](https://flask.palletsprojects.com/en/3.0.x/testing/)
- [Python Github Actions Setup](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)