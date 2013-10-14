{% extends 'homepage.html' %}
{% load static %}

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


{% block copy_news %}
### Latest updates
{% endblock %}



{% block copy_community %}
### Events & meetups

{% endblock %}


{% block press %}

[<img src="{% static 'img/press-logos/hackernews_logo.png' %}" title="Hacker News, Y-combinator" class="press-img">](https://www.hnsearch.com/search#request/all&q=docker/)
[<img src="{% static 'img/press-logos/linux.com_150.png' %}" title="Linux.com: Docker: A 'Shipping Container' for Linux Code" class="press-img">](http://www.linux.com/news/enterprise/cloud-computing/731454-docker-a-shipping-container-for-linux-code/)
[<img src="{% static 'img/press-logos/techcrunch_wide_150.png' %}" title="Techcrunch" class="press-img">](http://techcrunch.com/2013/07/28/the-matrix-of-hell-and-two-open-source-projects-for-the-emerging-agnostic-cloud/)
[<img src="{% static 'img/press-logos/admin_magazine_150.png' %}" title="Admin Magazine" class="press-img">](http://www.admin-magazine.com/Archive/2013/16)
{% endblock %}

{% block index_introduction %}
{% endblock %}
