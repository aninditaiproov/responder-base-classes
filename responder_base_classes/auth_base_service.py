__author__ = "icleary"

from .open_base_service import OpenBaseView

from .decorators import (
    initialize_response_media_valid_content_type,
    valid_credential_format,
    valid_credentials,
)


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
        raise NotImplementedError

    @classmethod
    def valid_credentials_for_route(cls, req, user):
        """
        Validate credentials against application
            Safe assumption that user exists and password matches, per on_request method
        This should be overridden for each method
        :param req: Mutable request object
        :param user: User object
        :return:
        """
        # Honestly not sure how to implement this...will add a test once I decide or get help :)
        # print("Exiting valid_credentials function")
        raise NotImplementedError

    @initialize_response_media_valid_content_type
    @valid_credential_format
    @valid_credentials
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
