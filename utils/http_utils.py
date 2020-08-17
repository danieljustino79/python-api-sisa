from bottle import response
from http import HTTPStatus
from json import dumps


class HttpUtils:
    @staticmethod
    def response_ok(data):
        return HttpUtils.response_data(HTTPStatus.OK, data)

    @staticmethod
    def response_bad_request(data):
        return HttpUtils.response_data(HTTPStatus.BAD_REQUEST, data)

    @staticmethod
    def response_unauthorized():
        return HttpUtils.response_status(HTTPStatus.UNAUTHORIZED)

    @staticmethod
    def response_not_found():
        return HttpUtils.response_status(HTTPStatus.NOT_FOUND)

    @staticmethod
    def response_status(status):
        response.status = status
        response.content_type = 'application/json'
        return None

    @staticmethod
    def response_data(status, data):
        response.status = status
        response.content_type = 'application/json'
        return dumps(data)
