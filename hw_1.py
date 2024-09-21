from typing import Any, Awaitable, Callable
import urllib
import math
import statistics
import json
import urllib.parse

import chardet
the_encoding = chardet.detect(b'your string')['encoding']

async def application(
        scope: dict[str, Any],
        recieve: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]]
) -> None:

    if scope['type'] != 'http' and scope['method'] != 'GET':
        await answer(
            send,
            status_code=404,
            content_type='text/plain',
            body=b'404 Not found')
        return
    
    message = await recieve()

    paths = {'factorial': factorial, 'fibonacci': fibonacci, 'mean': mean}

    scope_path = scope['path']
    path = urllib.parse.urlparse(scope_path).path
    path_splitted = path.strip('/').split('/')
    args = None

    if path_splitted[0] not in paths:
        await answer(
            send,
            status_code=404,
            content_type='text/plain',
            body=b'404 Not found'
            )
        return
    
    if path_splitted[0] == 'factorial':
        enc = chardet.detect(scope['query_string'])['encoding']
        query_string = scope['query_string']
        if query_string == b'':
            await answer(send,
                    status_code = 422,
                    content_type = 'text/plain',
                    body = b'422 Unprocessable Entity'
                    )
            return            
        query_string_enc = query_string.decode(enc)
        query = urllib.parse.parse_qs(query_string_enc)
        if 'n' not in query.keys():
            await answer(send,
                    status_code = 422,
                    content_type = 'text/plain',
                    body = b'422 Unprocessable Entity'
                    )
            return
                
        try:
            n = int(query['n'][0])
        except:
            await answer(send,
                    status_code = 422,
                    content_type = 'text/plain',
                    body = b'422 Unprocessable Entity'
                    )
            return    
        if n < 0:
            await answer(send,
                    status_code = 400,
                    content_type = 'text/plain',
                    body = b'400 Bad request'
                    )
            return
        args = n

    if path_splitted[0] == 'fibonacci':
        try:
            n = int(path_splitted[1])
        except:
            await answer(send,
                    status_code = 422,
                    content_type = 'text/plain',
                    body = b'422 Unprocessable Entity'
                    )
            return    
        if n < 0:
            await answer(send,
                    status_code = 400,
                    content_type = 'text/plain',
                    body = b'400 Bad request'
                    )
            return
        args = n
        
    if path_splitted[0] == 'mean':
        try:
            body = json.loads(message.get('body', b'').decode('utf-8'))
        except:
            await answer(send,
                    status_code = 422,
                    content_type = 'text/plain',
                    body = b'422 Unprocessable Entity'
                    )
            return

        if len(body) == 0:
            await answer(send,
                    status_code = 400,
                    content_type = 'text/plain',
                    body = b'400 Bad request'
                    )
            return

        try:
            array_f = [float(x) for x in body]
        except:
            await answer(send,
                    status_code = 422,
                    content_type = 'text/plain',
                    body = b'422 Unprocessable Entity'
                    )
            return

        args = array_f
        
    function = paths[path_splitted[0]]
    await function(send, args)



async def answer(send,
                      status_code: int = 404,
                      content_type: str = 'text/plain',
                      body: bytes = b'404 Not Found',
                      ):
    await send({
        'type': 'http.response.start',
        'status': status_code,
        'headers': [[b'content-type', content_type.encode()]],
    })

    await send({
        'type': 'http.response.body',
        'body': body,
    })

async def factorial(send, args: int):
    res = json.dumps({'result': math.factorial(args)}).encode('utf-8')
    await answer(send,
                 status_code=200,
                 content_type='application/json',
                 body=res)
        
async def fibonacci(send, args: int):
    res = json.dumps({'result':  fibonacci_last(args)}).encode('utf-8')
    await answer(send,
                 status_code=200,
                 content_type='application/json',
                 body=res)


async def mean(send, args: list):
    res = json.dumps({'result':  statistics.mean(args)}).encode('utf-8')
    await answer(send,
                 status_code=200,
                 content_type='application/json',
                 body=res)


def fibonacci_last(n):
    fibonacci_numbers = [0, 1]
    for i in range(2,n):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return fibonacci_numbers[-1]