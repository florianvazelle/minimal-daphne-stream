import time

from django.http.response import StreamingHttpResponse


def iterable_content():
    for _ in range(5):
        time.sleep(1)
        print('Returning chunk')
        yield b'a' * 10000


def test_stream_view(request):
    return StreamingHttpResponse(iterable_content())

