{% extends 'learn-more.html' %}
{% load static %}
{% block title %}About Docker - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}

{% block copy_headline %}
# Learn what Docker is all about #
{% endblock %}

{% block copy_introduction %}
## About Docker

Docker  is an open-source engine that automates the deployment of any application as a lightweight, portable, self-sufficient container that will run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on and between virtually any server. The same container that a developer builds and tests on a laptop will run at scale, in production, on VMs, bare-metal servers, OpenStack clusters, public instances, or combinations of the above.

Common use cases for Docker include:

*   Automating the packaging and deployment of applications
*   Creation of lightweight, private PAAS environments
*   Automated testing and continuous integration/deployment
*   Deploying and scaling web apps, databases and backend services

## Learn what Docker is all about

The following presentation explains what Docker is in laymen terms and then goes into more detail what makes Docker
    special and different from virtual machines.

<iframe class="slideshare-presentation" src="https://www.slideshare.net/slideshow/embed_code/24441742" width="630" height="393" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>

<a href="{% url 'the_whole_story' %}" title="Read the whole story in html format">Read the full story</a>

Or, if you want to give it a spin:

<a href="{% url 'getting_started' %}" class="btn btn-large btn-primary primary-action-button center" title="getting started">Get started!</a>

{% endblock %}