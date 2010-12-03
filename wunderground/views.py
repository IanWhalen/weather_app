from django.shortcuts import render_to_response
from xml_handler import clean_weather_data
from uri_handler import assemble_uri, get_weather_from_uri
from geo_handler import get_locale_from_ip

def homepage_view(request):
    today = '2010-11-28'
    yesterday = '2010-11-27'

    # Capture IP address from request
    ip_address = request.META['REMOTE_ADDR']

    # Get lat and lon from IP address:
    latitude, longitude = get_locale_from_ip(ip_address)

    # Get weather for right now
    formatted_uri = assemble_uri(latitude, longitude)
    raw_weather_string = get_weather_from_uri(formatted_uri)
    current_temp = clean_weather_data(raw_weather_string)

    # Get weather for yesterday
    # TODO http://api.wunderground.com/weatherstation/WXDailyHistory.asp?ID=ITRAFFOR2&month=9&day=26&year=2010&format=1
    # formatted_uri = assemble_uri(latitude, longitude)
    # raw_weather_string = get_weather_for_uri(formatted_uri)
    # weather_data_yesterday = clean_weather_data(raw_weather_string)

    return render_to_response('weather.html', {'weather_today': current_temp})
