from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ContentAppBarraPunto/$', 'ContentAppBarraPunto.views.muestra_todo'),
    url(r'^ContentAppBarraPunto/(\d+)', 'ContentAppBarraPunto.views.pagina'),
    url(r'^admin/', include(admin.site.urls)),
)
