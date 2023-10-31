import xml
import xml.etree.ElementTree as ET
import xmltodict
from bs4 import BeautifulSoup
import json
from xml.dom.minidom import parse, parseString


root_node = ET.parse('doc.xml')
root = root_node.getroot()

f = open("result.txt", "w")

for elem in root:
    for subelem in elem:
        result = subelem.text
        f.write(str(result))

f2 = open("result.txt", "r")
content = f2.read()
lines = content.splitlines()
del lines[0]
new_content = "\n".join(lines)
new_file = open("result.txt", "w")
new_file.write(new_content)

