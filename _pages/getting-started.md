{% extends 'getting-started.html' %}
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

{### Installation#}
{##}
{#<ul class="option-chooser-blocks">#}
{#    <li>Ubuntu linux</li>#}
{#    <li>From binaries</li>#}
{#    <li>Mac, Linux</li>#}
{#    <li>Windows</li>#}
{#    <li>Amazon EC2</li>#}
{#    <li>Rackspace Cloud</li>#}
{#    <li>Arch Linux</li>#}
{#    <br style="clear: both">#}
{#</ul>#}

## Installing on Ubuntu

### Requirements

* Ubuntu 12.04 (LTS) (64-bit)
* *or* Ubuntu 12.10 (quantal) (64-bit)
* The 3.8 Linux Kernel

### Install dependencies

This linux-image-extra package is needed on standard Ubuntu EC2 AMIs in order to install the aufs kernel module.

    sudo apt-get install linux-image-extra-`uname -r`

### Install Docker

The following instructions will add the Ubuntu PPA (Personal Package Archive) sources to your apt sources list, update
    and install. This may import a new GPG key. This will be shown as: (key 63561DC6: public key "Launchpad PPA for
    dotcloud team" imported).

    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:dotcloud/lxc-docker
    sudo apt-get update
    sudo apt-get install lxc-docker

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
    over to the [community page](http://localhost:8008/community/#anchor-3)

* #### [Redis in Docker](http://www.johnmcostaiii.net/2013/installing-redis-on-docker/)
    John Costa explains how to use Docker to package Redis, an open source database.

* #### [Memcached as a service, using Docker](http://www.slideshare.net/julienbarbier42/building-a-saas-using-docker)
    Julien Barbier writes about how to build your own SaaS, with memcached a a proof-of-concept example.

{% endblock %}
