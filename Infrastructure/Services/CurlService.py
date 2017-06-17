import pycurl
import io
import json


class CurlService:
    def get_json(self, url):
        print(url)
        buffer = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, buffer.write)
        c.perform()
        c.close()

        body = buffer.getvalue().decode('UTF-8')
        return json.loads(body)