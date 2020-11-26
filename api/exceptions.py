from rest_framework.exceptions import APIException


class IPStackException(APIException):

    def __init__(self, exception_data):
        super().__init__()
        self.status_code = exception_data['code']
        self.detail = exception_data['info']
        self.code = exception_data['type']
