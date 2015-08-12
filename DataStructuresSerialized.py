#!/usr/bin/env python3
#list 

class DataStructuresSerialized():
    def __init__(self, data, separator = '|'):
        self.separator = separator
        if (isinstance(data, bytes)):
            data = data.decode()

        if (isinstance(data, str)):
            self.serializedString = data
            self._unserialize()
        elif isinstance(data, list):
            self.unserializedStruct = data
            self._serialize()
        else:
            self.serializedString   = None
            self.unserializedStruct = None

        
    def getSerializedString(self):
        self._serialize()
        return self.serializedString

    def getUnserializedStruct(self):
        self._unserialize()
        return self.unserializedStruct

    def update(self, index, newString):
        if not index or not newString or not self.unserializedStruct:
            return None
        
        for subscript, item in enumerate(self.unserializedStruct):
            if subscript == index:
                self.unserializedStruct[subscript] = newString

    def _unserialize(self):
        if not self.serializedString:
            self.unserializedStruct = None
            return

        self.unserializedStruct = self.serializedString.split(self.separator)

    def _serialize(self):
        if not self.unserializedStruct:
            self.serializedString = None
            return
        data = list(map(lambda i: str(i), self.unserializedStruct))

        for index, item in enumerate(data):
            if self.separator in item:
                self.serializedString = None
                return

        self.serializedString = self.separator.join(data)
