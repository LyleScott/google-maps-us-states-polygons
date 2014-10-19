from pprint import pprint
from xml.dom import minidom


def xml2dict(path):
    data = []
    with open(path) as fp:
        xml = ''.join([line.strip() for line in fp.readlines()])
        doc = minidom.parseString(xml).documentElement
        for state in doc.childNodes:
            # str() to avoid the 'u' prefix for unicode strings.
            state_name = str(state.attributes['name'].value)
            points = []
            for point in state.childNodes:
                points.append([
                    float(point.attributes['lat'].value),
                    float(point.attributes['lng'].value),
                ])
            data.append([state_name, points])
    return data


def write_file(path, data):
    with open(path, 'w') as fp:
        fp.write('var stateCoords = ')
        pprint(data, stream=fp)


if __name__ == '__main__':
    xml_file = 'states.xml'
    out_file = 'coords.js'
    write_file(out_file, xml2dict(xml_file))