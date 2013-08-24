from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'base.views.home', name='home'),
    url(r'^learn_more/$', TemplateView.as_view(template_name='learn-more.md'), name="learn_more"),
    url(r'^gettingstarted/$', TemplateView.as_view(template_name='getting-started.md'), name="getting_started"),
    url(r'^community/$', TemplateView.as_view(template_name='community.md'), name="community"),


    # url(r'^gettingstarted/$', 'base.views.gettingstarted', name="getting_started"),

    url(r'^the_whole_story/$', TemplateView.as_view(template_name='the-whole-story.md'), name="the_whole_story"),
    url(r'^the-whole-story/$', RedirectView.as_view(url=reverse_lazy('the_whole_story'))),

    url(r'^live/$', TemplateView.as_view(template_name='live.md'), name="live"),

    url(r'^news/$', 'base.views.news', name="news"),
    url(r'^team/$', 'base.views.team', name="team"),
    url(r'^press/$', TemplateView.as_view(template_name='about/press.md'), name="press"),
    url(r'^events/$', TemplateView.as_view(template_name='about/events.md'), name="events"),


    url(r'^news_signup/$', 'base.views.email_thanks', name='email_thanks'),

    url(r'^tutorial/', include('docker_tutorial.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
