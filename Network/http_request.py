import requests


def string_from_request(req: requests.Request):
    def format_prepped_request(prepped, encoding=None):
        # prepped has .method, .path_url, .headers and .body attribute to view the request
        encoding = encoding or requests.utils.get_encoding_from_headers(prepped.headers)
        if prepped.body:
            body = prepped.body.decode(encoding) if encoding else '<binary data>'
        else:
            body = ''
        headers = '\n'.join(['{}: {}'.format(*hv) for hv in prepped.headers.items()])
        return f"""\
{prepped.method} {prepped.path_url} HTTP/1.1
{headers}

{body}"""


    session = requests.Session()
    prepped = session.prepare_request(req)
    return format_prepped_request(prepped, 'utf8')


if __name__ == '__main__':
    req = requests.Request("GET", "http://www.google.com/")
    print(string_from_request(req))
