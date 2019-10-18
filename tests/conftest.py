import pytest
import responder
from responder_base_classes.auth_base_service import AuthService
from responder_base_classes.models import User
from responder_base_classes.open_base_service import OpenService


@pytest.fixture
def api():

    api = responder.API(debug=False, allowed_hosts=[";"])

    @api.route("/OpenService")
    class OpenServiceObject(OpenService):
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

    @api.route("/RequestOpenService")
    class RequestOpenService(OpenService):
        """An endpoint for Objects
        """

        @staticmethod
        async def execute_on_request(req, resp):
            resp.headers["X-Pizza"] = "42"

    @api.route("/AuthService")
    class AuthObjectView(AuthService):
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

    @api.route("/OnMethodLessOpenService")
    class OnMethodLessOpenService(OpenService):
        """An endpoint that hasn't defined any execute_on_{method}s
        """

    @api.route("/OnMethodLessAuthService")
    class OnMethodLessViewAuthService(AuthService):
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

            user = User(username="test_user", password="test_password")

            return user

    return api
