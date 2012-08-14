from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^auth$', 'ateoto_dayboard.views.auth', name="dayboard-auth"),
    url(r'^callback$', 'ateoto_dayboard.views.callback', name="dayboard-callback"),
)
