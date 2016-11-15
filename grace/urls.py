from django.conf.urls import include, url
from django.contrib import admin

from grace.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'', include('grace.members_area.urls', namespace='members')),
    url(r'^admin/', admin.site.urls),
]
