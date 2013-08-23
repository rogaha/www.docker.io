{% extends 'getting-started.html' %}
{% load static %}
{% block meta-description %}Start using Docker in minutes and build awesome applications with the tutorials{% endblock %}
{% block meta-keywords %}Docker, Installation, install Docker, download Docker{% endblock %}
{% block title %}Getting Started - {% endblock %}


{% block copy_headline %}
# It's easy to start using Docker #
{% endblock %}


{% block copy_introduction %}

# Start using Docker
We try to make using Docker easy.

**Never tried Docker before?** <a href="#h_tutorial">start with the interactive tutorial.</a> **Looking to install?** <a href="#h_installation">jump to installation</a>

{% endblock %}

{% block copy_interactive_tutorial %}
## <a id="h_tutorial"></a>Interactive tutorial

The best way to learn how Docker works is to use it!

This hands-on tutorial is 100% online, so you don't need to install a thing. In about 10-15 minutes you'll be familiar with the basic
    Docker commands.


{% include 'tutorial/snippet.html' %}

{% endblock %}




{% block copy_install %}

## <a id="h_installation"></a>Installation
{### Installation#}

There are several installation options. Our recommended installation path is for **Ubuntu linux**,
    because we develop Docker on Ubuntu and our installation package will do most of the work for you.

Mac, Windows and some Linux distributions cannot natively run Docker at this time so we help you setup a
    Ubuntu virtual machine and run Docker inside of that.

<ul class="option-chooser-blocks">
    <a href="http://docs.docker.io/en/latest/installation/ubuntulinux/" target="_blank"><li>Ubuntu linux <img src="{% static 'img/platform-logos/ubuntu.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/binaries/" target="_blank"><li>From binaries <img src="{% static 'img/platform-logos/binaries.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/vagrant/" target="_blank"><li>Mac, Linux <img src="{% static 'img/platform-logos/mac-linux.png' %}">  </li></a>
    <a href="http://docs.docker.io/en/latest/installation/windows/" target="_blank"><li>Windows <img src="{% static 'img/platform-logos/windows.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/amazon/" target="_blank"><li>Amazon EC2 <img src="{% static 'img/platform-logos/amazonaws.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/rackspace/" target="_blank"><li>Rackspace <img src="{% static 'img/platform-logos/rackspace.png' %}"> </li></a>
    <a href="http://docs.docker.io/en/latest/installation/archlinux/" target="_blank"><li>Arch Linux <img src="{% static 'img/platform-logos/archlinux.png' %}"> </li></a>
    <br style="clear: both">
</ul>

{% endblock %}


{% block copy_hello_world %}
## Run 'hello world'

Now let's do some magic!

    docker run ubuntu /bin/echo hello world

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

    docker run -i -t ubuntu /bin/bash

This command creates an interactive shell in a minimal ubuntu container. You will be able to use this shell just like
    you would any other linux machine or virtual machine. Press Ctrl-D to exit the shell.

{% endblock %}

{% block copy_user_guides %}

## What can you build?

Here are just two examples of some cool stuff people have already built with Docker. For the full list, head
    over to the [community page]({% url 'community' %}#What-people-have-already-built-using-Docker)

* #### [Redis in Docker](http://www.johnmcostaiii.net/2013/installing-redis-on-docker/)
    John Costa explains how to use Docker to package Redis, an open source database.

* #### [Memcached as a service, using Docker](http://www.slideshare.net/julienbarbier42/building-a-saas-using-docker)
    Julien Barbier writes about how to build your own SaaS, with memcached a a proof-of-concept example.


{% endblock %}
