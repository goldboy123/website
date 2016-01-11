from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'media').replace('\\','/'),}), 
    (r'^games/$','games.views.games'),
    (r'^articles/$','blog.views.PostShowIndex'),
    (r'^articles/(?P<num>\d+)/$','blog.views.PostShow'),
    (r'^listarc/$','blog.views.ListArc'),
    (r'^$','blog.views.Index'),
    (r'^about/$','blog.views.About'),
    (r'^works/$','blog.views.Works'),

)
urlpatterns += patterns('',
           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name='media'),
           url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT },name='static'),
           )

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )

