# stdlib imports
import base64

# package imports
import responder


def test_incorrect_content_type(api):
    # test case for incorrect media type...considering adding yaml support, thoughts/desires?

    headers = {"content-type": "application/yaml"}

    r = api.requests.post("/", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_415  # unsupported media type


def test_correct_media_incorrect_credential_format(api):
    # headers with no 'username' or 'password'
    headers = {"content-type": "application/json"}

    r = api.requests.post("/", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_custom_auth_incorrect_credential_format_1(api):
    # headers with no 'username' or 'password'
    headers = {
        "Content-Type": "application/json",
        "usernamefdsklj": "test_user",
        "password": "test_password",
    }

    r = api.requests.post("/", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_custom_auth_incorrect_credential_format_2(api):
    # headers with no 'username' or 'password'
    headers = {
        "Content-Type": "application/json",
        "username": "test_user",
        "passwordsfsd": "test_password",
    }

    r = api.requests.post("/", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_custom_auth_correct_credential_format(api):
    # headers with no 'username' or 'password'
    headers = {
        "Content-Type": "application/json",
        "username": "test_user",
        "password": "test_password",
    }

    r = api.requests.post("/", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK


def test_basic_auth_incorrect_credential_format(api):
    # attempt at basic headers with no 'authorization' and no 'username' or 'password'
    # Do I need another test for "basic {}"? Is that part of a spec?

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorizationsdf": encoded_header}

    r = api.requests.post("/", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_400  # bad request


def test_basic_auth_correct_credential_format(api):
    # attempt at basic headers with no 'authorization' and no 'username' or 'password'

    encoded_credentials = base64.b64encode(b"test_user:test_password")
    encoded_header = "Basic {}".format(encoded_credentials.decode("utf-8"))

    headers = {"Content-Type": "application/json", "authorization": encoded_header}

    r = api.requests.post("/", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # bad request
