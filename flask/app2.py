import logging 
from flask import Flask

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)

app = Flask(__name__)

@app.route("/")
def index():
    logging.debug("success! index page has been accessed")
    return "Hello World!"