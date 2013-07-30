{% extends 'about.html' %}
{% load static %}
{% block title %}About Docker - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}

{% block copy_headline %}
# Follow what is going on at the docker hack-day, live. #
{% endblock %}

{% block copy_introduction %}
## Docker Live Stream.

Today you are able to see and work with the Hackday's live stream. The event should start around 2PM PST
    Please come back soon, or check on IRC for the status.


Also check out our <a href="{% url 'community' %}" class="" title="community page">Community page</a>

{% endblock %}