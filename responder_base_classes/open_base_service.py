__author__ = "icleary"

import responder

from .decorators import (
    execute_on_method_if_allowed_to_execute_method,
    valid_content_type,
)
from .models import Service


class OpenService(Service):
    """
    Base Class for every API service class to inherit from
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

    @execute_on_method_if_allowed_to_execute_method
    async def on_get(
        self, req: responder.models.Request, resp: responder.models.Response
    ) -> None:
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_head(
        self, req: responder.models.Request, resp: responder.models.Response
    ) -> None:
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_post(
        self, req: responder.models.Request, resp: responder.models.Response
    ) -> None:
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_put(
        self, req: responder.models.Request, resp: responder.models.Response
    ) -> None:
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_patch(
        self, req: responder.models.Request, resp: responder.models.Response
    ) -> None:
        pass

    @execute_on_method_if_allowed_to_execute_method
    async def on_delete(
        self, req: responder.models.Request, resp: responder.models.Response
    ) -> None:
        pass

    @valid_content_type
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
