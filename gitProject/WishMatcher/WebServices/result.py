import json


class JSONSerializable(object):
    def __repr__(self):
        return json.dumps(self.__dict__)

class result(JSONSerializable):
    def __init__(self, product, url):
        self.product = product
        self.url = url