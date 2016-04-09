from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin, auth
from web.urls import url_patterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth.views.login, name='login'),
    url(r'^logout/$', auth.views.logout, {'next_page': '/'}, name='logout'),
    url(r'^', include(url_patterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
