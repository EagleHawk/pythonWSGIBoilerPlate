from flask import Flask, make_response
from http import HTTPStatus
import os
import json
import gunicorn


def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/", methods=['GET'])
    def index():
        return f"Hello Boilerplate <br>Testing: {testing}", HTTPStatus.OK

    return app


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

gunicorn