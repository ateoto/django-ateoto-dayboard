from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse

import requests
from requests_oauth2 import OAuth2

def auth(request):

    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET

    site = "http://accounts.google.com"

    authorize = "/o/oauth2/auth"
    token = "/o/oauth2/token"

    scope = "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/tasks https://www.googleapis.com/auth/userinfo.profile"

    redirect_uri =  request.build_absolute_uri(reverse('dayboard-callback'))

    oauth2_handler = OAuth2(client_id, client_secret, site, redirect_uri, authorize, token)
    auth_url = oauth2_handler.authorize_url(scope=scope,response_type='code')

    return HttpResponse('<a href="%s">Click</a>' % auth_url)

def callback(request):
    # This is a lot of duplicated work, put this in a function somewhere?
    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET

    site = "http://accounts.google.com"

    authorize = "/o/oauth2/auth"
    token = "/o/oauth2/token"

    scope = "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/tasks https://www.googleapis.com/auth/userinfo.profile"

    redirect_uri =  request.build_absolute_uri(reverse('dayboard-callback'))

    oauth2_handler = OAuth2(client_id, client_secret, site, redirect_uri, authorize, token)

    if request.method == 'GET':
        code = request.GET.get('code', None)
        if code:
            url = '%s%s' % (site, token)
            payload = { 'code' : code,
                        'client_id' : client_id,
                        'client_secret' : client_secret,
                        'redirect_uri' : redirect_uri,
                        'grant_type' : 'authorization_code'}
            #response = oauth2_handler.get_token(code)
            response = requests.post(url, data=payload)
            return HttpResponse(response.status_code)
        else:
            return HttpResponse('Code not found')
    else:
        return HttpResponse('Not GET')
