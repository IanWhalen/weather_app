from django.shortcuts import render_to_response
from django.http import HttpResponse
import httplib2

def homepage_view(request):
    h = httplib2.Http()
    
    base_1 = 'http://www.weather.gov/forecasts/xml/'
    base_2 = 'sample_products/browser_interface/ndfdBrowserClientByDay.php?'
    zip_code_list = 'zipCodeList=19010'
    hour_format = '&format=24+hourly'
    start_date = '&startDate=2010-11-25'

    formatted_uri = ''.join([base_1, base_2, zip_code_list, hour_format, start_date])

    resp, content = h.request(formatted_uri)

    assert resp.status == 200
    assert resp['content-type'] == 'text/xml'

    html = content
    return HttpResponse(html)
