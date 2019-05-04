# stdlib imports
import inspect

# package imports
import wrapt

# local imports
from .utils import update_reason, assign_credentials_from_base64


@wrapt.decorator
def initialize_response_media_valid_content_type(wrapped, instance, args, kwargs):
    """
    1) Initializes response media
    2) Check if headers specify valid content type
      - executes func if valid content type
    :param req: Mutable request object
    :param resp: Mutable response object
    """

    runtime_message = "Decorator can only be applied to a staticmethod"

    if instance is None:
        if inspect.isclass(wrapped):
            # Decorator was applied to a class.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to a function or staticmethod.
            raise RuntimeError(runtime_message)
    else:
        if inspect.isclass(instance):
            # Decorator was applied to a classmethod.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to an staticmethod.

            def _execute(req, resp, *_args, **_kwargs):
                """
                :param req: Mutable request object
                :param resp: Mutable response object
                :param _args: inner args
                :param _kwargs: inner kwargs
                :return:
                """
                # assumes failing checks, will override in on_{method}
                resp.media = {"status": "failure", "reason": None}

                # check content type against allowed types
                if "content-type" in set(req.headers.keys()):
                    for content_type in instance.allowed_content_types:
                        if content_type in req.headers["content-type"]:
                            return wrapped(req, resp, *_args, **_kwargs)

                instance.allowed_to_execute_method = False
                resp.status_code = 415  # Unsupported media type
                update_reason(
                    resp, f"content-type is not in {instance.allowed_content_types}"
                )
                return wrapped(req, resp, *_args, **_kwargs)

            return _execute(*args, **kwargs)


@wrapt.decorator
def execute_on_method_if_allowed_to_execute_method(wrapped, instance, args, kwargs):
    """
    1) this bootstraps on_{method} checking, since responder calls both on_request and on_{method}
    2) expects execute_on_{method} to be overloaded, if you want to use that http method

    """

    runtime_message = "Decorator can only be applied to a staticmethod"

    if instance is None:
        if inspect.isclass(wrapped):
            # Decorator was applied to a class.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to a function or staticmethod.
            raise RuntimeError(runtime_message)
    else:
        if inspect.isclass(instance):
            # Decorator was applied to a classmethod.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to an staticmethod.

            async def _execute(req, resp, *_args, **_kwargs):
                """
                :param req: Mutable request object
                :param resp: Mutable response object
                :param _args: inner args
                :param _kwargs: inner kwargs
                :return:
                """
                wrapped_function_name = wrapped.__name__

                ###
                # print(wrapped_function_name)
                ###

                if not instance.allowed_to_execute_method:
                    reason_str = f"In {wrapped_function_name} function: exiting before running execute_{wrapped_function_name}_request"
                    # print(reason_str)
                    update_reason(resp, reason_str)
                    return

                execute_function_name = f"execute_{wrapped_function_name}"

                if hasattr(instance, execute_function_name):
                    await getattr(instance, execute_function_name)(req, resp)
                else:
                    resp.media = {
                        "status": "failure",
                        "reason": f"{execute_function_name} not implemented for this URL path",
                    }
                    resp.status_code = 501  # Not Implemented

                return wrapped(req, resp, *_args, **_kwargs)

            return _execute(*args, **kwargs)


@wrapt.decorator
def valid_credential_format(wrapped, instance, args, kwargs):
    """
    1) this checks that credentials are formatted correctly
    """

    runtime_message = "Decorator can only be applied to a staticmethod"

    if instance is None:
        if inspect.isclass(wrapped):
            # Decorator was applied to a class.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to a function or staticmethod.
            raise RuntimeError(runtime_message)
    else:
        if inspect.isclass(instance):
            # Decorator was applied to a classmethod.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to an staticmethod.

            async def _execute(req, resp, *_args, **_kwargs):
                """
                :param req: Mutable request object
                :param resp: Mutable response object
                :param _args: inner args
                :param _kwargs: inner kwargs
                :return:
                """

                # check credential format
                header_keys = set(req.headers.keys())

                format_is_username_and_password = (
                    "username" in header_keys and "password" in header_keys
                )
                format_is_base64_authorization = "authorization" in header_keys

                if format_is_username_and_password:
                    ###
                    # print("format_is_username_and_password")
                    ###

                    return wrapped(req, resp, *_args, **_kwargs)
                elif format_is_base64_authorization:
                    ###
                    # print("format_is_authorization")
                    ###

                    # placeholder for HTTP basic authentication and base 64
                    req = assign_credentials_from_base64(req)
                    return wrapped(req, resp, *_args, **_kwargs)
                else:
                    # invalid credential format, update status/reason

                    ###
                    # print("else, bad credential format")
                    ###

                    instance.allowed_to_execute_method = False
                    resp.status_code = 400  # bad request (can't get credentials)
                    update_reason(resp, "credential format is invalid")

                return wrapped(req, resp, *_args, **_kwargs)

            return _execute(*args, **kwargs)


@wrapt.decorator
def valid_credentials(wrapped, instance, args, kwargs):
    """
    1) this checks that credentials are valid
    2) expects execute_on_{method} to be overloaded, if you want to use that http method

    """

    runtime_message = "Decorator can only be applied to a staticmethod"

    if instance is None:
        if inspect.isclass(wrapped):
            # Decorator was applied to a class.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to a function or staticmethod.
            raise RuntimeError(runtime_message)
    else:
        if inspect.isclass(instance):
            # Decorator was applied to a classmethod.
            raise RuntimeError(runtime_message)
        else:
            # Decorator was applied to an staticmethod.

            async def _execute(req, resp, *_args, **_kwargs):
                """
                :param req: Mutable request object
                :param resp: Mutable response object
                :param _args: inner args
                :param _kwargs: inner kwargs
                :return:
                """

                # get user using req headers
                user = instance.get_user(req)

                if user is None:
                    instance.allowed_to_execute_method = False
                    resp.status_code = 401  # Unauthorized
                    update_reason(
                        resp, "Invalid credentials for this request, user doesn't exist"
                    )
                    # print("user doesn't exist")
                elif req.headers["password"] != user.password:
                    instance.allowed_to_execute_method = False
                    resp.status_code = 401  # Unauthorized
                    update_reason(
                        resp, "Invalid credentials for this request, password is wrong"
                    )
                    ###
                    # print("password is wrong")
                    ###

                # THIS CAN PROBABLY CHANGE TO A arg or kwarg for the decorator
                # SOMETHING LIKE WHAT GROUP THEY ARE REQUIRED TO BE IN
                elif not instance.valid_credentials_for_route(req, user):
                    # now check request against user access dict (overridden by each route)
                    instance.allowed_to_execute_method = False
                    resp.status_code = 401  # Unauthorized
                    update_reason(
                        resp,
                        "Valid user and password, but invalid authorization for this request",
                    )

                return wrapped(req, resp, *_args, **_kwargs)

            return _execute(*args, **kwargs)
