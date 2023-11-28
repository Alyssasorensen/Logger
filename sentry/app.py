from flask import Flask
import sentry_sdk

sentry_sdk.init(
    dsn="https://ba8afdc49cf11be8b02456338c255304@o4506300835692547.ingest.sentry.io/4506300911845376",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World1"

@app.route('/error')
def creating_error():
    try:
        1/0
    except Exception as e:
        raise Exception(f'something went wrong: {e}')

if__name__== "__main__":
    app.run(debug=True)