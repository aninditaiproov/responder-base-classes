# Responder-base-classes: Base Classes for [Responder (kennethreitz)](https://github.com/kennethreitz/responder#installing-responder)

[![Build Status](https://img.shields.io/travis/com/iancleary/responder-base-classes/master.svg)](https://img.shields.io/travis/com/iancleary/responder-base-classes)
[![image](https://img.shields.io/pypi/v/responder-base-classes.svg)](https://pypi.org/project/responder-base-classes/)
[![Updates](https://pyup.io/repos/github/iancleary/responder-base-classes/shield.svg)](https://pyup.io/repos/github/iancleary/responder-base-classes/)
[![image](https://img.shields.io/pypi/l/responder-base-classes.svg)](https://pypi.org/project/responder-base-classes/)
[![image](https://img.shields.io/pypi/pyversions/responder-base-classes.svg)](https://pypi.org/project/responder-base-classes/)
[![image](https://img.shields.io/github/contributors/iancleary/responder-base-classes.svg)](https://github.com/iancleary/responder-base-classes/graphs/contributors)


# The Basic Idea

The primary concept is to provide base classes for REST APIs with JSON and [Responder's class based views](https://python-responder.org/en/latest/tour.html#class-based-views)

- Extend Responder with extensions similar to [Flask's extensions]( http://flask.pocoo.org/extensions)
- Responder executes the `on_request` method followed by `on_{method}`, where method is an HTTP verb.
    - extending that syntax to `execute_on_request` and `execute_on_{method}`
    - the expectation is that you implement or overload `execute_on_request` and `execute_on_{method}` as appropriate
- Two Base Classes are provided: `OpenBaseView` and `AuthBaseView`
- `OpenBaseView` requires no authorization but checks content-type and implemented routes
- `AuthBaseView` extends `OpenBaseView` with Basic Auth and Custom Auth, and has placeholder functions for your implementation of:
    - a `get_user` function for how you check general authorization for you backend
    - a `valid_credentials_for_route` function for specific authorization per route
   
# Example Usage
~~~~
import responder

from responder_base_classes.open_base_service import OpenBaseView
from responder_base_classes.auth_base_service import AuthBaseView

api = responder.API()

@api.route("/OpenBaseView")
class ObjectView(OpenBaseView):
    """An endpoint for Objects"""
    
    @staticmethod
    async def execute_on_get(req, resp):
        resp.media = {
            "status": "success",
            "reason": "executed on_get completely",
            "object": 42,
        }
        resp.status_code = 200  # OK
    
    @staticmethod
    async def execute_on_head(req, resp):
        resp.status_code = 200  # OK
    
    @staticmethod
    async def execute_on_post(req, resp):
        resp.media = {
            "status": "success",
            "reason": "executed on_post completely",
            "object": 42,
        }
        resp.status_code = 200  # OK
    
    @staticmethod
        async def execute_on_request(req, resp):
            resp.headers["X-Pizza"] = "42"

@api.route("/AuthBaseView")
class AuthObjectView(AuthBaseView):
    """An endpoint for Objects
    """
    
    @classmethod
    def valid_credentials_for_route(cls, req, user):
        """
        Validate credentials for route
        This should be overridden for each method
        :param req: Mutable request object
        :param user: User object
        :return:
        """
        # check password
        if user is not None:
            # something along the lines of checking if session includes 'username'
            # then checking if the username has the privileges for the request dict
            return True  # this defaults to allowed if user exists
        return False
    
    def get_user(cls, req):
        """
        Get User Class Object, facilitates checking credentials
        :param req: Mutable request object
        :return:
        """
        # you should implement for your application, below is just for testing
        class User(object):
            def __init__(self, username, password):
                self.username = username
                self.password = password
        user = User(username="test_user", password="test_password")
        return user
    
    @staticmethod
    async def execute_on_post(req, resp):
        resp.media = {
            "status": "success",
            "reason": "executed on_post completely",
            "object": 42,
        }
        resp.status_code = 200  # OK
        
headers = {"Content-Type": "application/json"}
r = api.requests.get("/OpenBaseView", headers=headers)
print(r.json())
{'status': 'success', 'reason': 'executed on_get completely', 'object': 42}

print(r.headers[X-Pizza'])
42

# Demo of AuthBaseView
import base64@staticmethod
        async def execute_on_request(req, resp):
            resp.headers["X-Pizza"] = "42"

# credentials that match placeholder in AuthObjectView.get_user
encoded_credentials = base64.b64encode(b"test_user:test_password")
encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

headers = {"Content-Type": "application/json", "authorization": encoded_header}
r = api.requests.patch("/AuthBaseView", headers=headers)

print(r.json())
{'status': 'failure', 'reason': 'execute_on_patch not implemented for this URL path'}
# note, we didn't implement execute_on_patch, we implemented execute_on_post

r = api.requests.post("/AuthBaseView", headers=headers)

print(r.json())
{'status': 'success', 'reason': 'executed on_post completely', 'object': 42}

# credentials that do not match placeholder in AuthObjectView.get_user
encoded_credentials = base64.b64encode(b"non_existent_user:bad_password")
encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

headers = {"Content-Type": "application/json", "authorization": encoded_header}

r = api.requests.get("/AuthBaseView", headers=headers)
print(r.json())
{'status': 'failure', 'reason': 'In on_get function: exiting before running execute_on_get_request; Invalid credentials for this request, password is wrong'}

# please note that this example's get_user defines a user,
# so it is indicating that the password doesn't match the defined user
# generally, this would indicate the 'non_existent_user' doesn't exist
# in thase case, print(r.json()) would return the following:
# {'status': 'failure', 'reason': 'In on_get function: exiting before running execute_on_get_request; Invalid credentials for this request, user doesn't exist"'}

~~~~

# Installing Responder-base-classes

Install the latest release:


    $ pip install responder-base-classes


Only **Python 3.6+** is supported ([as required by the Responder package](https://github.com/kennethreitz/responder#installing-responder))


# TODO
See [TODO](TODO.md) about possible next features/changes!

----------

# Contributing Guide

See the [Contributing Guide](CONTRIBUTING.md) and welcome!

Thank you and I hope you find my/our work useful!  Have a nice day :)
