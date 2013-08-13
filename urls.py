from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'base.views.home', name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.md'), name="about"),

    url(r'^community/$', TemplateView.as_view(template_name='community.md'), name="community"),
    url(r'^gettingstarted/$', TemplateView.as_view(template_name='getting-started.md'), name="getting_started"),

    # url(r'^gettingstarted/$', 'base.views.gettingstarted', name="getting_started"),

    url(r'^the-whole-story/$', TemplateView.as_view(template_name='the-whole-story.md'), name="the-whole-story"),
    url(r'^live/$', TemplateView.as_view(template_name='live.md'), name="live"),

    url(r'^news_signup/$', 'base.views.email_thanks', name='email_thanks'),
    url(r'^news_signup_iframe/$', 'base.views.email_thanks', name='news_signup_iframe'),

    url(r'^tutorial/', include('tutorial.urls')),

    url(r'^testpage/$', TemplateView.as_view(template_name='tutorial/testpage.html'), name="testpage"),

    url(r'^whats-next/$', 'base.views.whats_next', name="whats-next"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
