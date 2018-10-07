import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    https://pymotw.com/2/xml/etree/ElementTree/create.html
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

patch_xml = ET.XML('''
    <country name="Singapore2">
        <rank>1</rank>
        <year>2099</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="S"/>
    </country>
''')
#print(patch_xml)
tree = ET.parse('country_data.xml')
root = tree.getroot()
root.append(patch_xml)
print(prettify(root))
