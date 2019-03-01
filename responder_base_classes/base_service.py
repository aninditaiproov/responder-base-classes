__author__ = "icleary"

import sys

from .utils import assign_credentials_from_base64


class BaseView(object):
    """
    Base Class for every View to inherit from
    Assumptions:
        - check headers for 'application/json'
        - overload these functions:
            execute_on_{method} (worker function)
            valid_credentials_for_route (specific to each route)
            get_user (however your system wants to implement user authentication)
                expects getattr(user, password) to match authorization, see valid_credential_format()
    """

    __slots__ = "allowed_to_execute_method"
    # default to enforce the above to make classes be explicit
    # __dict__ allows other variables to be assigned without __slots__ benefits

    def __init__(self):
        self.allowed_to_execute_method = (
            True
        )  # on_method sets to this to false, if appropriate

    async def on_get(self, req, resp):
        # this bootstraps on_method checking, since responder calls both on_request and on_{method}
        # expects execute_on_{method} to be overloaded, if you want to use that http method

        function_name = sys._getframe().f_code.co_name

        # print(f"In {function_name} function")

        if not self.allowed_to_execute_method:
            reason_str = f"In {function_name} function: exiting before running execute_{function_name}_request"
            # print(reason_str)
            self.update_reason(resp, reason_str)
            return

        execute_function_name = f"execute_{function_name}"

        if hasattr(self, execute_function_name):
            await getattr(self, execute_function_name)(req, resp)
        else:
            resp.media = {
                "status": "failure",
                "reason": f"{execute_function_name} not implemented for this URL path",
            }
            resp.status_code = 501  # Not Implemented

    async def on_head(self, req, resp):
        # this bootstraps on_method checking, since responder calls both on_request and on_{method}
        # expects execute_on_{method} to be overloaded, if you want to use that http method

        function_name = sys._getframe().f_code.co_name

        # print(f"In {function_name} function")

        if not self.allowed_to_execute_method:
            reason_str = f"In {function_name} function: exiting before running execute_{function_name}_request"
            # print(reason_str)
            self.update_reason(resp, reason_str)
            return

        execute_function_name = f"execute_{function_name}"

        if hasattr(self, execute_function_name):
            await getattr(self, execute_function_name)(req, resp)
        else:
            # no resp.media as head has no body
            resp.status_code = 501  # Not Implemented

    async def on_post(self, req, resp):
        # this bootstraps on_method checking, since responder calls both on_request and on_{method}
        # expects execute_on_{method} to be overloaded, if you want to use that http method

        function_name = sys._getframe().f_code.co_name

        # print(f"In {function_name} function")

        if not self.allowed_to_execute_method:
            reason_str = f"In {function_name} function: exiting before running execute_{function_name}_request"
            # print(reason_str)
            self.update_reason(resp, reason_str)
            return

        execute_function_name = f"execute_{function_name}"

        if hasattr(self, execute_function_name):
            await getattr(self, execute_function_name)(req, resp)
        else:
            resp.media = {
                "status": "failure",
                "reason": f"{execute_function_name} not implemented for this URL path",
            }
            resp.status_code = 501  # Not Implemented

    async def on_put(self, req, resp):
        # this bootstraps on_method checking, since responder calls both on_request and on_{method}
        # expects execute_on_{method} to be overloaded, if you want to use that http method

        function_name = sys._getframe().f_code.co_name

        # print(f"In {function_name} function")

        if not self.allowed_to_execute_method:
            reason_str = f"In {function_name} function: exiting before running execute_{function_name}_request"
            # print(reason_str)
            self.update_reason(resp, reason_str)
            return

        execute_function_name = f"execute_{function_name}"

        if hasattr(self, execute_function_name):
            await getattr(self, execute_function_name)(req, resp)
        else:
            resp.media = {
                "status": "failure",
                "reason": f"{execute_function_name} not implemented for this URL path",
            }
            resp.status_code = 501  # Not Implemented

    async def on_patch(self, req, resp):
        # this bootstraps on_method checking, since responder calls both on_request and on_{method}
        # expects execute_on_{method} to be overloaded, if you want to use that http method

        function_name = sys._getframe().f_code.co_name

        # print(f"In {function_name} function")

        if not self.allowed_to_execute_method:
            reason_str = f"In {function_name} function: exiting before running execute_{function_name}_request"
            # print(reason_str)
            self.update_reason(resp, reason_str)
            return

        execute_function_name = f"execute_{function_name}"

        if hasattr(self, execute_function_name):
            await getattr(self, execute_function_name)(req, resp)
        else:
            resp.media = {
                "status": "failure",
                "reason": f"{execute_function_name} not implemented for this URL path",
            }
            resp.status_code = 501  # Not Implemented

    async def on_delete(self, req, resp):
        # this bootstraps on_method checking, since responder calls both on_request and on_{method}
        # expects execute_on_{method} to be overloaded, if you want to use that http method

        function_name = sys._getframe().f_code.co_name

        # print(f"In {function_name} function")

        if not self.allowed_to_execute_method:
            reason_str = f"In {function_name} function: exiting before running execute_{function_name}_request"
            # print(reason_str)
            self.update_reason(resp, reason_str)
            return

        execute_function_name = f"execute_{function_name}"

        if hasattr(self, execute_function_name):
            await getattr(self, execute_function_name)(req, resp)
        else:
            resp.media = {
                "status": "failure",
                "reason": f"{execute_function_name} not implemented for this URL path",
            }
            resp.status_code = 501  # Not Implemented

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

    @classmethod
    def valid_credential_format(cls, req):
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
            return False

    @classmethod
    def valid_header_for_json(cls, req):
        """
        Check if headers specify application json
        :param req: Mutable request object
        :return: True if valid, false otherwise
        """

        # print(set(req.headers.keys()))
        if "content-type" in set(req.headers.keys()):
            if req.headers["content-type"] == "application/json":
                return True

        return False

    @classmethod
    def headers_are_valid(cls, req, resp):
        """
        Check if headers specify application json and update resp accordingly
        :param req: Mutable request object
        :param resp: Mutable response object
        :return:
        """
        if not cls.valid_header_for_json(req):
            resp.status_code = 415  # Unsupported media type
            resp.media.update(
                {
                    "status": "failure",
                    "reason": "content-type is not 'application/json'",
                }
            )
            return False

        return True

    @staticmethod
    def update_reason(resp, reason):
        """
        helper function to make on_request more readable
        :param resp: Mutable response object
        :param reason: string to add to resp.media
        :return:
        """
        if resp.media["reason"] is None:
            resp.media.update({"reason": reason})
        else:
            resp.media.update({"reason": reason + "; " + resp.media["reason"]})

    def on_request(self, req, resp):
        """
        This is run before every request
        :param req: Mutable request object
        :param resp: Mutable response object
        :return:
        """
        # assumes failing checks, will override in on_post
        resp.media = {"status": "failure", "reason": None}

        # check headers for application/json
        if not self.valid_header_for_json(req):
            self.allowed_to_execute_method = False
            resp.status_code = 415  # Unsupported media type
            self.update_reason(resp, "content-type is not 'application/json'")
            return

        if not self.valid_credential_format(req):
            self.allowed_to_execute_method = False
            resp.status_code = 400  # bad request (can't get credentials)
            self.update_reason(resp, "credential format is invalid")
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
