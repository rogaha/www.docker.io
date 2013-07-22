{% extends 'getting-started.html' %}
{% block meta-description %}An open source project to pack, ship and run any application as a lightweight container{% endblock %}
{% block meta-keywords %}Docker, linux containers, PaaS, dotCloud, introduction, about, getting started{% endblock %}
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

{% block copy_install %}

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

## Contributed guides

A number of people have done great guides on how to setup and use Docker in various situations

* #### [Installing docker on Rackspace cloud](http://blog.docker.io/2013/05/running-docker-on-rackspace/)
    A detailed tutorial on setting up Rackspace for Docker

* #### [Installing docker on digital ocean](http://blog.docker.io/2013/06/running-docker-on-digital-ocean-with-ubuntu/)
    A detailed tutorial on settin put Digitial Ocean for Docker

* #### [Getting docker to run on Linode](http://nick.stinemat.es/#docker-on-linode)
    A detailed guide for setting up Linode for Docker


{% endblock %}
