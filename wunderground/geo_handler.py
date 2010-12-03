from django.contrib.gis.utils import GeoIP

def get_locale_from_ip(ip_address):
    g = GeoIP()
    lat, lon = g.lat_lon('38.108.107.34')
    return lat, lon
