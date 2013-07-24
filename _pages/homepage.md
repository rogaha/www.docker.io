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
    OpenStack clusters, public clouds and more. <span class="read-more"><a href="{% url 'about' %}" title="About Docker">Read more -></a></span>
{% endblock %}


{% block copy_news %}
### Latest updates

#### Jul 23 • Press coverage from GigaOM, Reuters and Yahoo Finance

[<img src="{% static 'img/homepage/gigaom.png' %}" alt="gigaom">](http://gigaom.com/2013/07/23/paas-pioneer-dotcloud-gets-new-ceo-in-industry-vet-ben-golub/)
[<img src="{% static 'img/homepage/reuters.png' %}" alt="reuters">](http://www.reuters.com/article/2013/07/23/ca-dotcloud-idUSnBw235523a+100+BSW20130723)
[<img src="{% static 'img/homepage/yahoo.png' %}" alt="yahoo finance">](http://finance.yahoo.com/news/dotcloud-appoints-ben-golub-chief-133000939.html)

#### Jul 23 • Ben Golub Joins as CEO
Open source veteran Ben Golub joins as CEO to drive the docker vision forward.
    <span class="read-more"><a href="http://finance.yahoo.com/news/dotcloud-appoints-ben-golub-chief-133000939.html">read more -></a></span>

#### Jul 18 • Docker 0.5 Released
We've released version 0.5. Amongst other things, this release containes External Volumes, Advanced Networking and
    support for an Self Hosted Registry,
    <span class="read-more"><a href="http://blog.docker.io/2013/07/docker-0-5-0-external-volumes-advanced-networking-self-hosted-registry/">read more -></a></span>

#### Jul 11 • Featuring awesome projects
Everyday the Docker community is building awesome tools and projects with and for Docker. We want to share some of these with you.
    <span class="read-more"><a href="http://blog.docker.io/2013/07/docker-projects-from-the-docker-community/">read more -></a></span>

#### Jun 25 • dotCloud and Docker join the Linux Foundation
By joining the foundation, we are excited to support the amazing open source contributions that have come before us, and support those yet to come!
    <span class="read-more"><a href="http://blog.docker.io/2013/06/dotcloud-and-docker-join-the-linux-foundation/">read more -></a></span>

#### Jun 6 • Docker in Openstack
Sam Alba presents an article about the integration of Docker in OpenStack's cloud computing platform: NOVA. This integration
    allows users of OpenStack to seamlessly create Docker containers from the interface they are already using.
    <span class="read-more"><a href="http://blog.docker.io/2013/06/openstack-docker-manage-linux-containers-with-nova/">read more -></a></span>

{% endblock %}


{% block copy_community %}
### Community events

#### Upcoming Meetup • Jul 30:
Come to our July Meetup in San Francisco to hear representatives from **EBay**, **Mailgun (Rackspace)** and **CloudFlare**
    discuss how they are using Docker.
    <span class="read-more"><a href="http://www.meetup.com/Docker-meetups/">go to meetup -></a></span>

<img src="{% static 'img/homepage/ebay.png' %}" title="logo's of EBay, Mailgun and CloudFlare">
<img src="{% static 'img/homepage/mailgun.png' %}" title="logo's of EBay, Mailgun and CloudFlare">
<img src="{% static 'img/homepage/cloudflare.png' %}" title="logo's of EBay, Mailgun and CloudFlare">


#### Our previous hackday • Jun 11:
At our last day there was an impressive turnout and there was lots of talk about packing and using Docker in various
    ways.


<img src="{% static 'img/homepage/hackday_june_2013_brighter_400px.png' %}" alt="picture of Docker hackday at dotCloud office">

{% endblock %}


{% block copy_1 %}

# The title #

{% endblock %}


{% block tweets %}


{% list_tweets %}

354781876730335233
359360716584665088
357948061202386946
347003250299531264
347559367652032513
347915284977418241
348249053332647936
348281405974925313
354368422328541187
354970275353329664
355024956763021312
354954990277758978
355172662873567233
355346670520770561
355761264670162944
355705492087119875
355623162551083008
355404525793841153
355756267224047616
355955060607430656
354829574980378624
354411184524500992
354715613337354241
355705492087119875
355792575988371456
357972314660405249
356280542892802050
356763917625724928

{% end_list_tweets %}

{% endblock %}

