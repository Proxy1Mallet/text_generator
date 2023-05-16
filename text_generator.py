from fake_useragent import FakeUserAgent
from requests import Session
class text_generator:
    def __init__(self, text: str):
        self.headers = {
            'user-agent': FakeUserAgent().random
        }
        self.session = Session()
        self.ajax = 'https://textgenerator.ru/font/{}/ajax'.format
        self.data = {'text': text}

    def aesthetic(self):
        req = self.session.post(url = self.ajax('aesthetic'), headers = self.headers, data = self.data)
        return req.text

    def ancient(self):
        req = self.session.post(url = self.ajax('ancient'), headers = self.headers, data = self.data)
        return req.text

    def arabian_night(self):
        req = self.session.post(url = self.ajax('arabian-night'), headers = self.headers, data = self.data)
        return req.text

    def asian(self):
        req = self.session.post(url = self.ajax('asian'), headers = self.headers, data = self.data)
        return req.text

    def black_bracket(self):
        req = self.session.post(url = self.ajax('black-bracket'), headers = self.headers, data = self.data)
        return req.text

    def black_bubble(self):
        req = self.session.post(url = self.ajax('black-bubble'), headers = self.headers, data = self.data)
        return req.text

    def black_square(self):
        req = self.session.post(url = self.ajax('black-square'), headers = self.headers, data = self.data)
        return req.text

    def bold(self):
        req = self.session.post(url = self.ajax('bold'), headers = self.headers, data = self.data)
        return req.text

    def bold_gothic(self):
        req = self.session.post(url = self.ajax('bold-gothic'), headers = self.headers, data = self.data)
        return req.text

    def bold_italic(self):
        req = self.session.post(url = self.ajax('bold-italic'), headers = self.headers, data = self.data)
        return req.text

    def bold_script(self):
        req = self.session.post(url = self.ajax('bold-script'), headers = self.headers, data = self.data)
        return req.text

    def bubble(self):
        req = self.session.post(url = self.ajax('bubble'), headers = self.headers, data = self.data)
        return req.text

    def chinese(self):
        req = self.session.post(url = self.ajax('chinese'), headers = self.headers, data = self.data)
        return req.text

    def currency(self):
        req = self.session.post(url = self.ajax('currency'), headers = self.headers, data = self.data)
        return req.text

    def double_line(self):
        req = self.session.post(url = self.ajax('double-line'), headers = self.headers, data = self.data)
        return req.text

    def double_struck(self):
        req = self.session.post(url = self.ajax('double-struck'), headers = self.headers, data = self.data)
        return req.text

    def eastern(self):
        req = self.session.post(url = self.ajax('eastern'), headers = self.headers, data = self.data)
        return req.text

    def efiopiya(self):
        req = self.session.post(url = self.ajax('efiopiya'), headers = self.headers, data = self.data)
        return req.text

    def emoji(self):
        req = self.session.post(url = self.ajax('emoji'), headers = self.headers, data = self.data)
        return req.text

    def fairy_tale(self):
        req = self.session.post(url = self.ajax('fairy-tale'), headers = self.headers, data = self.data)
        return req.text

    def glyphs(self):
        req = self.session.post(url = self.ajax('glyphs'), headers = self.headers, data = self.data)
        return req.text

    def gothic(self):
        req = self.session.post(url = self.ajax('gothic'), headers = self.headers, data = self.data)
        return req.text

    def greek(self):
        req = self.session.post(url = self.ajax('greek'), headers = self.headers, data = self.data)
        return req.text

    def indian(self):
        req = self.session.post(url = self.ajax('indian'), headers = self.headers, data = self.data)
        return req.text

    def italic(self):
        req = self.session.post(url = self.ajax('italic'), headers = self.headers, data = self.data)
        return req.text

    def kanadskiy_slog(self):
        req = self.session.post(url = self.ajax('kanadskiy-slog'), headers = self.headers, data = self.data)
        return req.text

    def monospace(self):
        req = self.session.post(url = self.ajax('monospace'), headers = self.headers, data = self.data)
        return req.text

    def old_italic(self):
        req = self.session.post(url = self.ajax('old-italic'), headers = self.headers, data = self.data)
        return req.text

    def runy(self):
        req = self.session.post(url = self.ajax('runy'), headers = self.headers, data = self.data)
        return req.text

    def script(self):
        req = self.session.post(url = self.ajax('script'), headers = self.headers, data = self.data)
        return req.text

    def small_capital(self):
        req = self.session.post(url = self.ajax('small-capital'), headers = self.headers, data = self.data)
        return req.text

    def smooth_curve(self):
        req = self.session.post(url = self.ajax('smooth-curve'), headers = self.headers, data = self.data)
        return req.text

    def square(self):
        req = self.session.post(url = self.ajax('square'), headers = self.headers, data = self.data)
        return req.text

    def squiggle(self):
        req = self.session.post(url = self.ajax('squiggle'), headers = self.headers, data = self.data)
        return req.text

    def strike(self):
        req = self.session.post(url = self.ajax('strike'), headers = self.headers, data = self.data)
        return req.text

    def tilde_strike(self):
        req = self.session.post(url = self.ajax('tilde-strike'), headers = self.headers, data = self.data)
        return req.text

    def underline(self):
        req = self.session.post(url = self.ajax('underline'), headers = self.headers, data = self.data)
        return req.text

    def upsidedown(self):
        req = self.session.post(url = self.ajax('upsidedown'), headers = self.headers, data = self.data)
        return req.text

    def white_bracket(self):
        req = self.session.post(url=self.ajax('white-bracket'), headers=self.headers, data=self.data)
        return req.text