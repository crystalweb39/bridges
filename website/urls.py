from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('bridges.website.views',
    url(r'^$', 'home'),
    url(r'^(?P<path>.*).html', 'page'),
                       
)