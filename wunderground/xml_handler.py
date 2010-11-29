from xml.dom import minidom

def clean_weather_data(raw_weather_string):
    dom = minidom.parseString(raw_weather_string)

    # Get and return current temperature
    temp_f = dom.getElementsByTagName('temp_f')
    return temp_f[0].firstChild.nodeValue
