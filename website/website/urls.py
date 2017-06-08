
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from home import views


urlpatterns = [ 
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', views.home_files, name='home-files'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^french/$', views.set_french, name='set_french'),
    url(r'^english/$', views.set_english, name='set_english'),
    url(r'^spanish/$', views.set_spanish, name='set_spanish'),
]

urlpatterns += i18n_patterns(
    url(r'^', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^portfolio/', include('portfolio.urls'))
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^translate/', include('rosetta.urls')),
    ] + urlpatterns
