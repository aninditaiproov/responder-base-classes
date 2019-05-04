__author__ = "icleary"

import sys

from .utils import update_reason
from .decorators import initialize_response_media_valid_content_type
from .decorators import execute_on_method_if_allowed_to_execute_method


class OpenBaseView(object):
    """
    Base Class for every View to inherit from
    Assumptions:
        - check headers for 'json' or 'yaml' as responder supports both as of this writing
        - overload these functions:
            execute_on_{method} (worker function)
            valid_credentials_for_route (specific to each route)
            get_user (however your system wants to implement user authentication)
                expects getattr(user, password) to match authorization, see valid_credential_format()
    """

    __slots__ = ["allowed_to_execute_method"]
    # default to enforce the above to make classes be explicit
    # __dict__ allows other variables to be assigned without __slots__ benefits
    allowed_content_types = ["json", "yaml"]

    def __init__(self):
        self.allowed_to_execute_method = (
            True
        )  # on_method sets to this to false, if appropriate

    @execute_on_method_if_allowed_to_execute_method
    async def on_get(self, req, resp):
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_head(self, req, resp):
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_post(self, req, resp):
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_put(self, req, resp):
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_patch(self, req, resp):
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_delete(self, req, resp):
        pass

    @classmethod
    def get_user(cls, req):
        """
        Get User Class Object, facilitates checking credentials
        :param req: Mutable request object
        :return: user: User object that has password->str used for authentication
        """
        # print("In get_user function")
        # print(req.headers)
        # name = req.headers["username"]
        # user = User.get_by_name(name)
        #
        # # check that user exists
        # if user is not None:
        #     print("Yeah, user exists")
        #     return user
        #
        # print("Exiting get_user function with no user")
        return NotImplementedError

    @classmethod
    def valid_credentials_for_route(cls, req, user):
        """
        Validate credentials against route for application
            Safe assumption that user exists and password matches, per on_request method
        This should be overridden for each method
        :param req: Mutable request object
        :param user: User object
        :return:
        """
        # print("In valid_credentials function")

        # something along the lines of checking if session includes 'username'
        # then checking if the username has the privileges for the request dict
        #  check against product line name and name of product in user collection

        # Honestly not sure how to implement this...will add a test once I decide or get help :)
        # print("Exiting valid_credentials function")
        return False

    @initialize_response_media_valid_content_type
    async def on_request(self, req, resp):
        """
        This is run before every request
        :param req: Mutable request object
        :param resp: Mutable response object
        :return:
        """

        # valid content type, execute on_request method
        execute_function_name = "execute_on_request"
        if hasattr(self, execute_function_name):
            await getattr(self, execute_function_name)(req, resp)

        return
