__author__ = "icleary"

import responder

from .decorators import valid_content_type, valid_credential_format, valid_credentials
from .models import AuthServiceInterface
from .open_base_service import OpenService


class AuthService(OpenService, AuthServiceInterface):
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

    def __init__(self) -> None:
        super().__init__()

    @valid_content_type
    @valid_credential_format
    @valid_credentials
    async def on_request(
        self, req: responder.models.Request, resp: responder.models.Response
    ) -> None:
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
