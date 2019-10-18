# package imports
import responder
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class Base(object):
    """
    Base Class for every View or Service to inherit from
    Assumptions:
        - check headers for 'html', 'json' or 'yaml'content types
            responder supports json and yaml as of this writing
        - overload these functions:
            execute_on_{method} (worker function)
            valid_credentials_for_route (specific to each route)
            get_user (however your system wants to implement user authentication)
                expects getattr(user, password) to match authorization, see valid_credential_format()
    """

    _slots__ = ["allowed_to_execute_method"]
    # default to enforce the above to make classes be explicit
    # __dict__ allows other variables to be assigned without __slots__ benefits
    allowed_content_types = ["json", "yaml", "html"]

    def __init__(self) -> None:
        self.allowed_to_execute_method = True
        # on_method sets to this to false, if appropriate


class View(Base):
    allowed_content_types = ["html"]

    def __init__(self) -> None:
        super().__init__()


class Service(Base):
    allowed_content_types = ["json", "yaml"]

    def __init__(self) -> None:
        super().__init__()


class AuthServiceInterface(Service):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_user(cls, req: responder.models.Request) -> User:
        """
        Get User Class Object, facilitates checking credentials
        :param req: Mutable request object
        :return: user: User object that has password->str used for authentication
        """
        raise NotImplementedError

    @classmethod
    def valid_credentials_for_route(
        cls, req: responder.models.Request, user: User
    ) -> bool:
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
