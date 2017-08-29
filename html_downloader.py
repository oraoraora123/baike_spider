from urllib import request



class HtmlDownloder(object):
    def download(self, url):
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()