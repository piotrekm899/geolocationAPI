from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['error_code'] = response.status_code
        if getattr(exc, "code", None):
            response.data['code'] = exc.code

    return response




