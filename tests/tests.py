import unittest
from DataStructuresSerialized import DataStructuresSerialized

class TestSimple(unittest.TestCase):
    def test_nonsupportDataStructures(self):
        testTuples    = ('China', 10, 'beijing')
        testSeparator = '|'
        data          = DataStructuresSerialized(testTuples, testSeparator).getSerializedString()
        self.assertEqual(data, None)

    #test list serialized
    def test_listSerialized(self):
        testList     = ["China", 10, "beijing"]
        testSeparator = '|'
        data          = DataStructuresSerialized(testList, testSeparator).getSerializedString()

        self.assertEqual(data, 'China|10|beijing')

    def test_listSerializedDigit(self):
        testList     = [10, 21, 27]
        testSeparator = ','
        data          = DataStructuresSerialized(testList, testSeparator).getSerializedString()

        self.assertEqual(data, '10,21,27')

    def test_listSerializedNoSeparator(self):
        testList     = [10, 21, 27]
        data          = DataStructuresSerialized(testList).getSerializedString()

        self.assertEqual(data, '10|21|27')

    def test_listSerializedInvalidSeparator(self):
        testList     = ["China", 10, "beijing,haidian"]
        testSeparator = ','
        data          = DataStructuresSerialized(testList, testSeparator).getSerializedString()

        self.assertEqual(data, None)

    # test unserialized
    def test_unserialized(self):
        testString    = 'China|10|beijing'
        testSeparator = '|'
        data          = DataStructuresSerialized(testString, testSeparator).getDeserializationStruct()

        self.assertEqual(data, ['China', '10', 'beijing'])

    def test_unserializedEmpty(self):
        testString    = ''
        testSeparator = '|'
        data          = DataStructuresSerialized(testString, testSeparator).getDeserializationStruct()

        self.assertEqual(data, None)

    # test update
    def test_updateString(self):
        testString    = 'China|10|beijing'
        testSeparator = '|'
        index         = 1
        subString     = 'Hubei'
        dataClass     = DataStructuresSerialized(testString, testSeparator)
        dataClass.update(index, subString)
        data          = dataClass.getSerializedString()

        self.assertEqual(data, 'China|Hubei|beijing')

        dataClass.update(index, 'Ningxia')
        data          = dataClass.getSerializedString()
        
        self.assertEqual(data, 'China|Ningxia|beijing')

    def test_updateListStruct(self):
        testData      = ['China', 10, 'beijing']
        testSeparator = '|'
        index         = 1
        subString     = 'Hubei'
        dataClass     = DataStructuresSerialized(testData, testSeparator)
        dataClass.update(index, subString)
        data          = dataClass.getSerializedString()

        self.assertEqual(data, 'China|Hubei|beijing')

        dataClass.update(index, 'Ningxia')
        data          = dataClass.getSerializedString()
        
        self.assertEqual(data, 'China|Ningxia|beijing')










