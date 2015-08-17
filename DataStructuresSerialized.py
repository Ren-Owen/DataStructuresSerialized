#!/usr/bin/env python3
#list 

class DataStructuresSerialized():
    def __init__(self, data, separator = '|'):
        self.separator             = separator
        self.serializedString      = None
        self.deserializationStruct = None

        if (isinstance(data, bytes)):
            data = data.decode()

        if (isinstance(data, str)):
            self.serializedString = data
            self._deserialization()
        elif isinstance(data, list):
            self.deserializationStruct = data
            self._serialized()
        
    def getSerializedString(self):
        return self.serializedString

    def getDeserializationStruct(self):
        return self.deserializationStruct

    def update(self, index, newString):
        if index == None or not newString or not self.deserializationStruct:
            return None

        for subscript, item in enumerate(self.deserializationStruct):
            if subscript == index:
                self.deserializationStruct[subscript] = newString
        
        self._serialized()

    def _deserialization(self):
        if not self.serializedString:
            self.deserializationStruct = None
            return

        self.deserializationStruct = self.serializedString.split(self.separator)

    def _serialized(self):
        if not self.deserializationStruct:
            self.serializedString = None
            return
        data = list(map(lambda i: str(i), self.deserializationStruct))

        for index, item in enumerate(data):
            if self.separator in item:
                self.serializedString = None
                return

        self.serializedString = self.separator.join(data)
