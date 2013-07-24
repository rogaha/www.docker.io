{% extends 'getting-started.html' %}
{% load static %}
{% block meta-description %}Start using Docker in minutes and build awesome applications with the tutorials{% endblock %}
{% block meta-keywords %}Docker, Installation, install docker, download docker{% endblock %}
{% block title %}Getting Started - {% endblock %}


{% block copy_headline %}
# It's easy to start using Docker #
{% endblock %}


{% block copy_introduction %}

# Start using Docker
There are only a few steps you need to take to run Docker, but you have a couple of options, and which works best
    depends on your environment. Shown below is only the main (recommended) installation path for Ubuntu Linux.
    Other Installation paths can be found in the [installation documentation](http://docs.docker.io/en/latest/installation/).

{% endblock %}

{#{% block copy_install %}#}
{##}
{##}
{#{% endblock %}#}


{% block copy_install %}

## Installation

There are several installation options. Our recommended installation path is for **Ubuntu linux**,
    because Docker natively runs on Ubuntu and our installation package will do most of the work for you.

Mac, Windows and some Linux distributions cannot natively run Docker at this time so we help you setup a virtual
    Ubuntu virtual machine and run Docker inside of that.

<ul class="option-chooser-blocks">
    <a href="http://docs.docker.io/en/latest/installation/ubuntulinux/" target="_blank"><li>Ubuntu linux <img src="{% static 'img/platform-logos/ubuntu.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/binaries/" target="_blank"><li>From binaries <img src="{% static 'img/platform-logos/platform-02.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/vagrant/" target="_blank"><li>Mac, Linux <img src="{% static 'img/platform-logos/platform-03.png' %}">  </li></a>
    <a href="http://docs.docker.io/en/latest/installation/windows/" target="_blank"><li>Windows <img src="{% static 'img/platform-logos/platform-04.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/amazon/" target="_blank"><li>Amazon EC2 <img src="{% static 'img/platform-logos/platform-05.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/rackspace/" target="_blank"><li>Rackspace <img src="{% static 'img/platform-logos/platform-06.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/archlinux/" target="_blank"><li>Arch Linux <img src="{% static 'img/platform-logos/platform-07.png' %}"> </li></a>
    <br style="clear: both">
</ul>

{% endblock %}

{% block copy_hello_world %}
## Run 'hello world'

Now let's do some magic!

    docker run base /bin/echo hello world

This should output 'hello world'. Just one line? Yes, but a lot has happened..

Docker did all of the following

* It downloaded the base image from the [docker index](https://index.docker.io)
* it created a new LXC container
* It allocated a filesystem for it
* Mounted a read-write layer
* Allocated a network interface
* Setup an IP for it, with network address translation
* And then executed a process in there
* Captured its output and printed it to you

#### Run an interactive shell

You can also run an interactive shell session inside the container

    docker run -i -t base /bin/bash

This command create an interactive shell in a base container. And you will be able to use this shell just like
    you would any other linux machine or virtual machine.

{% endblock %}

{% block copy_user_guides %}

## What can you build?

These are just two example of what people have already build some cool stuff with Docker. For the full list, head
    over to the [community page]({% url 'community' %}#anchor-3)

* #### [Redis in Docker](http://www.johnmcostaiii.net/2013/installing-redis-on-docker/)
    John Costa explains how to use Docker to package Redis, an open source database.

* #### [Memcached as a service, using Docker](http://www.slideshare.net/julienbarbier42/building-a-saas-using-docker)
    Julien Barbier writes about how to build your own SaaS, with memcached a a proof-of-concept example.

{% endblock %}
