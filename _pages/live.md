{% extends 'about.html' %}
{% load static %}
{% block title %}About Docker - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}
{% block extra-meta %}<meta http-equiv="refresh" content="300">{% endblock %}


{% block copy_headline %}
# Follow what is going on at the docker hack-day, live. #
{% endblock %}

{% block copy_introduction %}
## Docker Live Stream.

Today we are having a Docker Hackday. As part of this hackday we feature a number of lightning talks. On this page you will
    be able to follow those live. The event should start around 6PM PST.

<img src="{% static 'img/temp/docker_hackday_6.png' %}" alt="docker hackday img">

{#<iframe width="625" height="394" src="http://www.youtube.com/embed/vVPUx2Yx6O4" frameborder="0" allowfullscreen></iframe>#}

Also check out our <a href="{% url 'community' %}" class="" title="community page">Community page</a>

{% endblock %}