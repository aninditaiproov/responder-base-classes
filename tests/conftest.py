import pytest
import responder

from responder_base_classes.open_base_service import OpenBaseView
from responder_base_classes.auth_base_service import AuthBaseView


@pytest.fixture
def api():

    api = responder.API(debug=False, allowed_hosts=[";"])

    @api.route("/OpenBaseView")
    class ObjectView(OpenBaseView):
        """An endpoint for Objects
        """

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
        async def execute_on_put(req, resp):
            resp.media = {
                "status": "success",
                "reason": "executed on_put completely",
                "object": 42,
            }
            resp.status_code = 200  # OK

        @staticmethod
        async def execute_on_patch(req, resp):
            resp.media = {
                "status": "success",
                "reason": "executed on_patch completely",
                "object": 42,
            }
            resp.status_code = 200  # OK

        @staticmethod
        async def execute_on_delete(req, resp):
            resp.media = {
                "status": "success",
                "reason": "executed on_delete completely",
                "object": 42,
            }
            resp.status_code = 200  # OK

    @api.route("/RequestOpenBaseView")
    class RequestObjectView(OpenBaseView):
        """An endpoint for Objects
        """

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
            print("In valid_credentials function: Class AuthObjectView")
            # something along the lines of checking if session includes 'username'
            # then checking if the username has the privileges for the request dict

            print(user)

            # check password
            if user is not None:
                print(
                    "Yeah, user is not None, but haven't checked valid credentials for route yet"
                )
                return True

            return False

        def get_user(cls, req):
            """
            Get User Class Object, facilitates checking credentials
            :param req: Mutable request object
            :return:
            """

            class User(object):
                def __init__(self, username, password):
                    self.username = username
                    self.password = password

            user = User(username="test_user", password="test_password")

            return user

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
        async def execute_on_put(req, resp):
            resp.media = {
                "status": "success",
                "reason": "executed on_put completely",
                "object": 42,
            }
            resp.status_code = 200  # OK

        @staticmethod
        async def execute_on_patch(req, resp):
            resp.media = {
                "status": "success",
                "reason": "executed on_patch completely",
                "object": 42,
            }
            resp.status_code = 200  # OK

        @staticmethod
        async def execute_on_delete(req, resp):
            resp.media = {
                "status": "success",
                "reason": "executed on_delete completely",
                "object": 42,
            }
            resp.status_code = 200  # OK

    @api.route("/OnMethodLessOpenBaseView")
    class OnMethodLessOpenBaseView(OpenBaseView):
        """An endpoint that hasn't defined any execute_on_{method}s
        """

    @api.route("/OnMethodLessAuthBaseView")
    class OnMethodLessViewAuthBaseView(AuthBaseView):
        """An endpoint that hasn't defined any execute_on_{method}s
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
            print("In valid_credentials function: Class OnMethodLessView")
            # something along the lines of checking if session includes 'username'
            # then checking if the username has the privileges for the request dict
            #  check against product line name and name of product in user collection

            print(user)

            # check password
            if user is not None:
                print(
                    "Yeah, user is not None, but haven't checked valid credentials for route yet"
                )
                return True

            return False

        def get_user(cls, req):
            """
            Get User Class Object, facilitates checking credentials
            :param req: Mutable request object
            :return:
            """

            class User(object):
                def __init__(self, username, password):
                    self.username = username
                    self.password = password

            user = User(username="test_user", password="test_password")

            return user

    return api
