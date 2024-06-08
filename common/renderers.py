from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler

from common.utils import build_response


class APIRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code

        if str(status_code).startswith('2'):
            response = build_response(data=data, status=status_code, data_only=True)
        else:
            response = build_response(error=data, status=status_code, data_only=True)

        return super().render(response, accepted_media_type, renderer_context)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # if response is not None:
    #     response.data['status_code'] = response.status_code

    return response
