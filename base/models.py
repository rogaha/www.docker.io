from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class TeamMember(models.Model):

    full_name = models.CharField(max_length=80, blank=True)
    bio = models.TextField()
    email = models.EmailField(blank=True,
                              help_text="This address will not be shown")
    gravatar_email = models.EmailField(_('gravatar email'), blank=True,
        help_text="This address will define which picture of you is shown, but the address itself will be hidden. <br>"
        "Change the picture at <a href='http://www.gravatar.com'>www.gravatar.com</a><br>")
    index_name = models.CharField(max_length=80, blank=True)
    github_handle = models.CharField(max_length=80, blank=True)
    sort_weight = models.IntegerField(default=10)
    show_as_team = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{}".format(self.full_name)

class NewsItem(models.Model):

    title = models.CharField(max_length=80, blank=False)
    text = models.TextField(blank=True, help_text="Markdown format accepted")
    link = models.URLField(blank=True)
    publication_date = models.DateField(default=datetime.now())
    show = models.BooleanField(default=False)
    author = models.ForeignKey(TeamMember)
    creation_date = models.DateTimeField(default=datetime.now(), editable=False)

    def __unicode__(self):
        return u"{}".format(self.title)

class Event(models.Model):

    title = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=80, blank=True)
    date_and_time = models.DateTimeField(default=datetime.utcnow(), help_text="Time local to the event")
    text = models.TextField(blank=True, help_text="Markdown format accepted")
    link = models.URLField(blank=True)

    def __unicode__(self):
        return u"{}".format(self.title)
