from django.http import JsonResponse


def build_response(data=None, error=None, status=200, data_only=False):
    data = {
        'data': data,
        'error': error,
        'status': False if error else True,
    }
    if data_only:
        return data
    else:
        return JsonResponse(
            data,
            status=status
        )
