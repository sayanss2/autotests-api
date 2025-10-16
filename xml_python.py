import xml.etree.ElementTree as ET
import myutils

xml_data = """
<user>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>john.doe@example.com</email>
</user>
"""

root = ET.fromstring(xml_data)
print(f'User ID: {root.find('id').text}')
print(f'User Name: {root.find('first_name').text} {root.find("last_name").text}')

print('---------------------------------------')

xml_file = 'xml_example.xml'
root_file = ET.parse(xml_file).getroot()

xml_dict = {}
for child in root_file:
    xml_dict[child.tag] = myutils.elem_to_dict(child)

print(myutils.pretty_xml_string(root, indent=4))