from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    (r'^auth$', 'ateoto_dayboard.views.auth', name="dayboard-auth"),
    (r'^callback$', 'ateoto_dayboard.views.callback', name="dayboard-callback"),
)
