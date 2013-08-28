{% extends 'homepage.html' %}
{% load list_tweets %}{% load static %}

{% block title %}Homepage - {% endblock %}
{% block meta-description %}Docker: An open source project to pack, ship and run any application as a lightweight container{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud{% endblock %}

{% block copy_headline %}

# an open source project to pack, ship and run any application as a lightweight container #

{% endblock %}


{% block copy_introduction %}
Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application.
    The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal,
    OpenStack clusters, public clouds and more. <span class="read-more"><a href="{% url 'learn_more' %}" title="About Docker">Read more -></a></span>
{% endblock %}



{% block tweets %}
{% list_tweets %}

365541565243990017
365561874907004929
365516662306381824
365494583657902080

{#Extra's since docker hackday #6#}
362628082345050114
{#362601233980211202#}
{#362538212519981056#}
362465372949069824
{#362455829347176449#}
362414011612008448
362579117482323968
362350303997210625
{#362471730448572418#}
362432830657150976
362426814708203520
362397723242135553
362366694259294208
{#362359971612078081#}
{#362355578141556737#}
{#362341799680946176#}
{#362338537728782337#}
362319091178029056
{#362285886177677314#}
362277568092704769
362238819577245697
362083256922935297

{#As of July 19#}
{#354781876730335233#}
359360716584665088
357948061202386946
347003250299531264
347559367652032513
347915284977418241
348249053332647936
348281405974925313
354368422328541187
{#354970275353329664#}
{#355024956763021312#}
354954990277758978
355172662873567233
{#355346670520770561#}
{#355761264670162944#}
355705492087119875
355623162551083008
355404525793841153
{#355756267224047616#}
355955060607430656
354829574980378624
{#354411184524500992#}
{#354715613337354241#}
{#355705492087119875#}
{#355792575988371456#}
{#357972314660405249#}
{#356280542892802050#}
{#356763917625724928#}

{% end_list_tweets %}
{% endblock %}


{% block copy_news %}
### Latest updates
{% endblock %}



{% block copy_community %}
### Events & meetups

{% endblock %}


{% block press %}

[<img src="{% static 'img/press-logos/linux.com_150.png' %}" title="Linux.com: Docker: A 'Shipping Container' for Linux Code" class="press-img">](http://www.linux.com/news/enterprise/cloud-computing/731454-docker-a-shipping-container-for-linux-code/)
[<img src="{% static 'img/press-logos/techcrunch_wide_150.png' %}" title="Techcrunch" class="press-img">](http://techcrunch.com/2013/07/28/the-matrix-of-hell-and-two-open-source-projects-for-the-emerging-agnostic-cloud/)
[<img src="{% static 'img/press-logos/admin_magazine_150.png' %}" title="Admin Magazine" class="press-img">](http://www.admin-magazine.com/Archive/2013/16)
{#[<img src="{% static 'img/press-logos/gigaom.png' %}" title="GigaOm" class="press-img">](http://gigaom.com/2013/07/23/paas-pioneer-dotcloud-gets-new-ceo-in-industry-vet-ben-golub/)#}
{% endblock %}

{% block index_introduction %}
{% endblock %}
