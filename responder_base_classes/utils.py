__author__ = "icleary"

import base64


def assign_credentials_from_base64(req) -> object:
    # insert functions to convert and assign to username and password

    credentials = req.headers["authorization"]

    # separate to get encoded credentials
    (basic, encoded_credentials) = credentials.split(" ")

    # decode to byte string
    decoded_credentials = base64.b64decode(encoded_credentials)

    # convert byte string to string
    credentials_string = decoded_credentials.decode("utf-8")

    # print(decoded_credentials)

    (username, password) = credentials_string.split(":")

    # assign credentials to headers, as downstream doesn't handle basic auth
    # this again assumes HTTPS, as custom params or base64 are equivalent to plain text
    # as base64 is reversible

    req.headers["username"] = username
    req.headers["password"] = password

    return req
