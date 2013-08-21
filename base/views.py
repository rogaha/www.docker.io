# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import request
from mailchimp import utils as mailchimputils
from datetime import datetime
from forms import NewsSubscribeForm, FilePickerForm
from django.http import HttpResponseRedirect
# from .utils import get_app_auth_twitter
from utils import TwitterClient
import json
from django.core.cache import cache

#We are not using the intercom plugin because we use js instead
#from intercom import Intercom

def home(request):
    """
    homepage
    """
    form = NewsSubscribeForm()

    return render_to_response("homepage.md", {
        "form": form,
    }, context_instance=RequestContext(request))


def email_thanks(request):
    """
    Page for thanking the user for signup
    """

    if request.method == "POST":
        form = NewsSubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            list_id = 'c0995b6e8f'
            CACHE_TIMEOUT = 3600 * 24 * 3

            mailchimp_list = cache.get(list_id)

            if mailchimp_list:
                pass
            else:
                connection = mailchimputils.get_connection()
                mailchimp_list = connection.get_list_by_id(list_id)

                cache.set(list_id, mailchimp_list, CACHE_TIMEOUT)


            results = mailchimp_list.subscribe(
                email,
                {
                    'EMAIL': email,
                    'FNAME': '',
                    'LNAME': '',
                    'MMERGE3': '',
                    'MMERGE4': '',
                    'MMERGE5': 'www.docker.io/',
                    },
                'html',
                'true'
            )

            intercom_extra = {
                'email': email,
                'news_signup_at': datetime.now().strftime("%Y-%m-%d"),
                'signup_location': "www.docker.io",
            }

            return render_to_response('base/email_thanks.html',
                {
                    'form': form,
                    'intercom_extra': intercom_extra
                },
                context_instance=RequestContext(request))

        else:
            # form = NewsSubscribeForm()

            return render_to_response('base/email_form.html',
                {
                    'form': form,
                },
                context_instance=RequestContext(request))

    else:
        form = NewsSubscribeForm()
        return render_to_response('base/email_form.html',
            {
                'form': form,
            },
            context_instance=RequestContext(request))


    return render_to_response("homepage.md", {
        "form": form,
        }, context_instance=RequestContext(request))


def filepicker(request):

    form = FilePickerForm()

    return render_to_response("base/filepicker.html", {
        "form": form,
    }, context_instance=RequestContext(request))
