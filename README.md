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


# Thoughts
- move to pipenv?
- helper function for a route's authorization per HTTP verb?

----------

# Contributing Guide (Welcome!)

### First Steps to fix an issue or bug
- Read the documentation (working on adding more)
- create the minimally reproducible issue
- try to edit the relevant code and see if it fixes it
- submit the fix to the provlem as a pull request 
- include an explanation of what you did and why

### First steps to contribute new features
- Create an issue to discuss the feature's scope and its fit for this package
- try to edit the relevant code and implement your new feature in a backwards compatible manner
- create new tests as you go
- update the documentation as you go
- run black to format you code as you go

### Requirements to merge code
- you must include test coverage
- you must update the documentation
- you must run black to format your code (run the snippet below from the base directory)

~~~~
black responder_base_classes/ tests/ setup.py
~~~~

---

### Recommended background reading on etiquette for contributions
- Mike McQuaid's [how-to-not-fail-at-using-open-source-software-in-your-organisation](https://mikemcquaid.com/2018/09/04/how-to-not-fail-at-using-open-source-software-in-your-organisation/)
    - No affiliation, just a fan of the article (the quote block below is from the article)
    - The Contributing Guide is based on it

> If you follow these steps your experience using and modifying OSS will be much more pleasant. What if you don’t feel confident making changes?
> *  help others help you by helping yourself
> You need to be willing to put in the time and effort to make it easier for others to help you. Starting with the easiest:
> 
> * read all the documentation before asking for help
> * create minimally reproducible issues
> * look at the code you think might be relevant
> * try to edit the relevant code and see if it fixes the problem
> * submit the fix to the problem as a pull request
> 
> Similarly on your issues, pull requests, tweets and everything related to open source:
>
> * have reasonable expectations (most maintainers are volunteering in their free time)
> * prioritise maintainers’ time (there’s more of you than there is of them so your time is less valuable)
> * defer to maintainers (it’s up to them if changes get made or merged; argue respectfully)
> * help others where you can (if you want help you need to give help)
>
> If you want to read more about how to do all aspects of OSS well check out the Open Source Guides. These are the best single resource on the internet on how to contribute to, start and maintain an open source project.
>
> Finally, just be a nice, kind human. It’s surprising how appreciated (and how rare) kind words are in OSS. Use them generously and you’ll reap the rewards.

Thank you and I hope you find my/our work useful!  Have a nice day :)
