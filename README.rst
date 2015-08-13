|

NAME
====

    python data structures list serialized and deserialization


|

SYNOPSIS
========

.. code-block::


    from DataStructuresSerialized import DataStructuresSerialized

    city       = ["China", "010", "beijing"]
    separator  = '|'
    serialized = DataStructuresSerialized(city, separator).getSerializedString()
    print(serialized)

    DataStructuresSerialized $ China|010|beijing

    cityString = "China|010|beijing"
    separator  = '|'
    city       = DataStructuresSerialized(city, separator).getDeserializationStruct()
    print(city)

    DataStructuresSerialized $ ['China', '10', 'beijing']

    cityString = "China|010|beijing"
    separator  = '|'
    index      = 1
    newString  = "000"
    city       = DataStructuresSerialized(cityString, separator)

    city.update(index, newString)
    newCityString = city.getSerializedString()

    print(newCityString)

    DataStructuresSerialized $ China|000|beijing


|

DESCRIPTION
===========

getSerializedString
-------------------
    return serialized string, only support list data structures serialized

getDeserializationStruct
------------------------
    return deserialization list data struct

update
------
    update serialized string or list data structures some substring
