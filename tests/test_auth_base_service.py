__author__ = "icleary"

# stdlib imports
import base64

# package imports
import responder


def test_json_content_type_incorrect_credential_format(api):
    # headers with no 'username' or 'password'
    headers = {"content-type": "application/json"}

    r = api.requests.post("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_custom_auth_incorrect_credential_format_1(api):
    # headers with no 'username' or 'password'
    headers = {
        "Content-Type": "application/json",
        "usernamefdsklj": "test_user",
        "password": "test_password",
    }

    r = api.requests.post("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_custom_auth_incorrect_credential_format_2(api):
    # headers with no 'username' or 'password'
    headers = {
        "Content-Type": "application/json",
        "username": "test_user",
        "passwordsfsd": "test_password",
    }

    r = api.requests.post("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_custom_auth_correct_credential_format(api):
    # headers with no 'username' or 'password'
    headers = {
        "Content-Type": "application/json",
        "username": "test_user",
        "password": "test_password",
    }

    r = api.requests.post("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK


def test_basic_auth_incorrect_credential_format(api):
    # attempt at basic headers with no 'authorization' and no 'username' or 'password'
    # Do I need another test for "basic {}"? Is that part of a spec?

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorizationsdf": encoded_header}

    r = api.requests.post("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_basic_auth_correct_credential_format(api):
    # attempt at basic headers with no 'authorization' and no 'username' or 'password'

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.post("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # bad request


def test_get_with_auth(api):
    # test on_get and execute_on_get

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.get("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_get completely",
        "object": 42,
    }


def test_head_with_auth(api):
    # test on_head and execute_on_head

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.head("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK


def test_post_with_auth(api):
    # test on_post and execute_on_post

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.post("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_post completely",
        "object": 42,
    }


def test_put_with_auth(api):
    # test on_put and execute_on_put

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.put("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_put completely",
        "object": 42,
    }


def test_patch_with_auth(api):
    # test on_patch and execute_on_patch

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.patch("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_patch completely",
        "object": 42,
    }


def test_delete_with_auth(api):
    # test on_delete and execute_on_delete

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.delete("/AuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_delete completely",
        "object": 42,
    }


def test_undefined_get_with_auth(api):
    # test class that hasn't defined execute_on_get

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.get("/OnMethodLessAuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_get not implemented for this URL path",
    }


def test_undefined_head_with_auth(api):
    # test class that hasn't defined execute_on_head

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.head("/OnMethodLessAuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented


def test_undefined_post_with_auth(api):
    # test class that hasn't defined execute_on_post

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.post("/OnMethodLessAuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_post not implemented for this URL path",
    }


def test_undefined_put_with_auth(api):
    # test class that hasn't defined execute_on_put

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.put("/OnMethodLessAuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_put not implemented for this URL path",
    }


def test_undefined_patch_with_auth(api):
    # test class that hasn't defined execute_on_patch

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.patch("/OnMethodLessAuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_patch not implemented for this URL path",
    }


def test_undefined_delete_with_auth(api):
    # test class that hasn't defined execute_on_delete

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.delete("/OnMethodLessAuthBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_delete not implemented for this URL path",
    }
