import json

from flask import Response


class ApiBaseException(Exception):
    status_code = 500
    message = None
    payload = None

    def __init__(self, message, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload


def generic_render(exception: ApiBaseException):
    return Response(
        response=json.dumps(
            {"message": exception.message, "payload": exception.payload}
        ),
        status=exception.status_code,
        mimetype="application/json",
    )


def error_notification_render(exception: ApiBaseException):
    return Response(
        response=exception.payload,
        status=exception.status_code,
        mimetype="application/text",
    )


class NotFound(ApiBaseException):
    status_code = 404
    message = "Entity not found"

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)


class Unauthorized(ApiBaseException):
    status_code = 401
    message = "Unauthorized"

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)


class DataFail(ApiBaseException):
    status_code = 400
    message = "It's not a valid object"

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)


class BusinessFail(ApiBaseException):
    status_code = 422
    message = "Fail on validation object"

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)
