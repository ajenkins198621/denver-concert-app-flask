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

## Using the Application
### How to run locally
`flask --app applications.web.app run`

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