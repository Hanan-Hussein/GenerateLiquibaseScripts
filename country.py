
from xml.dom import minidom
import os
import requests
import uuid
import json


def GenerateXML(country):

    insert = root.createElement('insert')
    insert.setAttribute('dbms', 'postgresql, mssql, hsqldb')
    insert.setAttribute('tableName', 'COUNTRY')

    xml.appendChild(insert)

    for key, value in x.items():
        # print(key,">>>",value)
        columns = root.createElement('column')
        columns.setAttribute('name', key.upper())
        columns.setAttribute('value', value)

        insert.appendChild(columns)

    xml_str = root.toprettyxml(indent="\t")

    save_path_file = "country.xml"

    with open(save_path_file, "w") as f:
        f.write(xml_str)


root = minidom.Document()

xml = root.createElement('changeSet')
xml.setAttribute('author', 'Tathmini')
xml.setAttribute('context', '!cuba')

root.appendChild(xml)

x = requests.get("https://countriesnow.space/api/v0.1/countries/flag/unicode")

allCountries = x.json()["data"]


for x in allCountries:

    myuuid = uuid.uuid4()
    myuuidStr = str(myuuid)

    x.update({"id": myuuidStr})
    print(x)
    x.update({"version": "1"})

    GenerateXML(x)
