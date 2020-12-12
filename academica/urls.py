from django.conf.urls import include, url
from django.contrib import admin
from matricula.views import index
from matricula.views.Auth import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'academica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^matricula/', include('matricula.urls')),
    url(r'^matricula_bills/', include('matricula.contrib.bills.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url('^accounts/profile/?$', get_profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
