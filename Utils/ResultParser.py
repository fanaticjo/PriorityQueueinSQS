import json


class resultparser:
    def __init__(self, event):
        data = event.get('Records', None)
        if data is None:
            raise Exception('No data Found quitting Parsing')
        else:
            self.__messageid = [x.get('messageId') for x in data]
            self.__body = [json.loads(x.get('body')) for x in data]
            self.__attributes = [x.get('attributes') for x in data]
            self.__priority = [x.get('messageAttributes').get('priority').get('stringValue') for x in data]
            self.__md5=[x.get('md5OfBody') for x in data]

    @property
    def messageid(self):
        return self.__messageid[0]

    @property
    def body(self):
        return self.__body[0]

    @property
    def attributes(self):
        return self.__attributes[0]

    @property
    def priority(self):
        return self.__priority[0]

    @property
    def md5(self):
        return self.__md5[0]
