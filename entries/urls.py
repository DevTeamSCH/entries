from django.conf.urls import url, include
from django.contrib import admin
from pityu.urls import url_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^', include(url_patterns)),
]
