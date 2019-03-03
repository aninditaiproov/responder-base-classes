# package imports
import responder
import yaml


def test_incorrect_content_type(api):
    # test case for unsupported media type

    headers = {"content-type": "application/xml"}

    r = api.requests.post("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_415  # unsupported media type


def test_yaml_content_type(api):
    # yaml as responder supports it for kubernetes, etc. etc.

    headers = {"content-type": "text/yaml", "Accept": "yaml"}

    r = api.requests.post("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK
    assert yaml.load(r.content) == {
        "status": "success",
        "reason": "executed on_post completely",
        "object": 42,
    }


def test_head(api):
    # test on_head and execute_on_head

    headers = {"Content-Type": "application/json"}

    r = api.requests.head("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK


def test_get(api):
    # test on_get and execute_on_get

    headers = {"Content-Type": "application/json"}

    r = api.requests.get("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_get completely",
        "object": 42,
    }


def test_post(api):
    # test on_post and execute_on_post

    headers = {"Content-Type": "application/json"}

    r = api.requests.post("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_post completely",
        "object": 42,
    }


def test_put(api):
    # test on_put and execute_on_put

    headers = {"Content-Type": "application/json"}

    r = api.requests.put("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_put completely",
        "object": 42,
    }


def test_patch(api):
    # test on_patch and execute_on_patch

    headers = {"Content-Type": "application/json"}

    r = api.requests.patch("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_patch completely",
        "object": 42,
    }


def test_delete(api):
    # test on_delete and execute_on_delete

    headers = {"Content-Type": "application/json"}

    r = api.requests.delete("/OpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_200  # OK

    assert r.json() == {
        "status": "success",
        "reason": "executed on_delete completely",
        "object": 42,
    }


def test_undefined_get(api):
    # test class that hasn't defined execute_on_get

    headers = {"Content-Type": "application/json"}

    r = api.requests.get("/OnMethodLessOpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_get not implemented for this URL path",
    }


def test_undefined_head(api):
    # test class that hasn't defined execute_on_head

    headers = {"Content-Type": "application/json"}

    r = api.requests.head("/OnMethodLessOpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented


def test_undefined_post(api):
    # test class that hasn't defined execute_on_post

    headers = {"Content-Type": "application/json"}

    r = api.requests.post("/OnMethodLessOpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_post not implemented for this URL path",
    }


def test_undefined_put(api):
    # test class that hasn't defined execute_on_put

    headers = {"Content-Type": "application/json"}

    r = api.requests.put("/OnMethodLessOpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_put not implemented for this URL path",
    }


def test_undefined_patch(api):
    # test class that hasn't defined execute_on_patch

    headers = {"Content-Type": "application/json"}

    r = api.requests.patch("/OnMethodLessOpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_patch not implemented for this URL path",
    }


def test_undefined_delete(api):
    # test class that hasn't defined execute_on_delete

    headers = {"Content-Type": "application/json"}

    r = api.requests.delete("/OnMethodLessOpenBaseView", headers=headers)

    assert r.status_code == responder.status_codes.HTTP_501  # Not Implemented

    assert r.json() == {
        "status": "failure",
        "reason": "execute_on_delete not implemented for this URL path",
    }
