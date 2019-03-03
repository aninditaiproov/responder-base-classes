__author__ = "icleary"

import sys

from .utils import assign_credentials_from_base64

from .open_base_service import OpenBaseView


class AuthBaseView(OpenBaseView):
    """
    Auth Base Class for every View to inherit from that requires authentication
    Assumptions:
        - check headers for 'json' or 'yaml' as responder supports both as of this writing
        - overload these functions:
            execute_on_{method} (worker function)
            valid_credentials_for_route (specific to each route)
            get_user (however your system wants to implement user authentication)
                expects getattr(user, password) to match authorization, see valid_credential_format()
    """

    def __init__(self):
        super().__init__()

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
        return None

    @classmethod
    def valid_credentials_for_route(cls, req, user):
        """
        Validate credentials against req's product_line_name and name_of_product
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

    def valid_credential_format(self, req, resp):
        """
        check if headers specify credentials in an approved format
        :param req: Mutable request object
        :return: True if valid, false otherwise
        """

        # print("In valid_credential_format function")
        header_keys = set(req.headers.keys())

        if "username" in header_keys and "password" in header_keys:
            return True
        elif "authorization" in header_keys:
            # placeholder for HTTP basic authentication and base 64
            req = assign_credentials_from_base64(req)

            return True
        else:
            # print("Invalid Credential format")
            self.allowed_to_execute_method = False
            resp.status_code = 400  # bad request (can't get credentials)
            self.update_reason(resp, "credential format is invalid")
            return False

    def on_request(self, req, resp):
        """
        This is run before every request
        :param req: Mutable request object
        :param resp: Mutable response object
        :return:
        """
        # assumes failing checks, will override in on_post
        self.initialize_response_media(resp)

        # check headers for application/json
        if not self.valid_content_type(req, resp):
            return

        if not self.valid_credential_format(req, resp):
            return
        else:
            # inspect session for credentials that match the query
            user = self.get_user(req)

        if user is None:
            self.allowed_to_execute_method = False
            resp.status_code = 401  # Unauthorized
            self.update_reason(
                resp, "Invalid credentials for this request, user doesn't exist"
            )
            # print("user doesn't exist")
        elif req.headers["password"] != user.password:
            self.allowed_to_execute_method = False
            resp.status_code = 401  # Unauthorized
            self.update_reason(
                resp, "Invalid credentials for this request, password is wrong"
            )
            # print("password is wrong")
        elif not self.valid_credentials_for_route(req, user):
            # now check request against user access dict (overridden by each route)
            self.allowed_to_execute_method = False
            resp.status_code = 401  # Unauthorized
            self.update_reason(
                resp,
                "Valid user and password, but invalid authorization for this request",
            )
