import httplib2

def assemble_uri(latitude, longitude):
    # Components from which to assemble final URI
    base = 'http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/'
    file_query = 'index.xml?query='
    latitude = str(latitude)
    longitude = str(longitude)

    # Actually assemble and return final URI
    return ''.join([base, file_query, latitude, ',', longitude])

def get_weather_from_uri(formatted_uri):
        # Pass URI to weather.gov REST service and store returned content
        h = httplib2.Http()
        resp, content = h.request(formatted_uri, 'GET')

        # Check validity of returned content
        assert resp.status == 200
        assert resp['content-type'] == 'text/xml'

        return content
