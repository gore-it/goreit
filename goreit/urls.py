from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'news.views.show', ),
    url(r'^news$', 'news.views.show', ),
    url(r'^cv', 'cv.views.show', ),
    url(r'^technologie', 'technology.views.show', ),
    url(r'^o_mnie', 'aboutme.views.show', ),
    url(r'^kontakt$', 'contact.views.contact', ),

    url(r'^admin/', include(admin.site.urls)),
)
