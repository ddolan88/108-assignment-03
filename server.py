from unittest import mock
from flask import Flask

from about import me

import json

from data import mock_data


app = Flask('server')


@app.get("/")
def home():
    return "Hello from flask server"


@app.get("/test")
def test():
    return "This is just a simple test"

# get /about


@app.get("/about")
def about_me():
    return "My name is Derek"


########################################################
############ API ENDPOINTS = PRODUCTS ##################
########################################################

# get /api/version
# @app.get("/api/version")

@app.get("/api/version")
def version():
    return "1.0"

# create a get request /api/about  and return first name and last name


@app.get("/api/about")
def about_json():

    # return me["first"] + " " + me["last"]

    # return f"{me['first']} {me['last']}"

    return json.dumps(me)  # parse the dicionary into a json string


# get /api/products
# return mock_data as a json string

@app.get("/api/products")
def products_data():
    return json.dumps(mock_data)


@app.get("/api/products/<id>")
def get_products_by_id(id):
    for prod in mock_data:
        if str(prod["id"]) == id:
            return json.dumps(prod)
    return "404 NOT FOUND"

    # travel mock_data list
    # compare the id with id variable
    # if they match, return the product as a json string


app.run(debug=True)
