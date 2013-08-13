{% extends 'whats-next.html' %}
{% load static %}
{% block title %}What's next - {% endblock %}
{% block meta-description %}Docker is an open-source engine that automates the deployment of any application as a lightweight, portable, self-sufficient container that will run virtually anywhere. Learn more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, containers, how it works{% endblock %}

{% block copy_headline %}
# Great, you've got the basics down, what's next?


{% endblock %}
{% block copy_introduction %}

{## Congratulations!#}
{#You have successfully completed the tutorial! Now you've got the basics down, you might want to take the following steps:#}

{% endblock %}


{% block copy_1 %}

## 1. Register for news and updates

At irregular intervals, mostly for new releases and other important updates we send out an email. If you'd like to
    keep updated, please sign up.

<form method="POST" action="{% url 'email_thanks' %}">
{% csrf_token %}
{{ form }}
<input type="submit" value="submit">
</form>


Also make sure to follow us on twitter -
<img src="{% static 'img/community/twitter-blue.png' %}" style="height: 40px; width: 40px" />
<a href="http://twitter.com/docker">twitter.com/docker</a>



## 2. Setup a machine to run Docker

Docker can run in many places and in a couple of different ways. Our experience is that one of the fastest ways to
    get up and running is to spin up a Ubuntu 12.04 or 13.04 virtual machine with one of the public cloud providers.

{#Here are some popular options.#}
{##}
{#<ul class="option-chooser-blocks">#}
{#    <a href="https:///www.rackspace.com" target="_blank"><li>Rackspace<img src="{% static 'img/platform-logos/platform-logo_rackspace.png' %}"> </li></a>#}
{#    <a href="https://www.digitalocean.com/?refcode=9152ecbd91ab" target="_blank"><li>Digital Ocean<img src="{% static 'img/platform-logos/platform-logo_digital-ocean.png' %}"> </li></a>#}
{#    <a href="http://www.aws.amazon.com/" target="_blank"><li>Amazon EC2 <img src="{% static 'img/platform-logos/amazonaws.png' %}"> </li></a>#}
{#    <a href="https://www.linode.com/" target="_blank"><li>Linode<img src="{% static 'img/platform-logos/platform-logo_linode.png' %}"> </li></a>#}
{#    <a href="http://www.softlayer.com/" target="_blank"><li>Softlayer<img src="{% static 'img/platform-logos/platform-logo_softlayer.png' %}"> </li></a>#}
{#    <br style="clear: both">#}
{#</ul>#}


## 3. Install Docker

If you have created an Ubuntu 12.04 or 13.04 machine you can follow [these installation instructions](https://docs.docker.io/en/latest/installation/ubuntulinux)

{#<ul class="option-chooser-blocks">#}
{#    <a href="http://docs.docker.io/en/latest/installation/ubuntulinux/" target="_blank"><li>Ubuntu linux <img src="{% static 'img/platform-logos/ubuntu.png' %}"> </li></a>#}
{#    <a href="http://docs.docker.io/en/latest/installation/binaries/" target="_blank"><li>From binaries <img src="{% static 'img/platform-logos/binaries.png' %}"> </li></a>#}
{#    <a href="http://docs.docker.io/en/latest/installation/vagrant/" target="_blank"><li>Mac, Linux <img src="{% static 'img/platform-logos/mac-linux.png' %}">  </li></a>#}
{#    <a href="http://docs.docker.io/en/latest/installation/windows/" target="_blank"><li>Windows <img src="{% static 'img/platform-logos/windows.png' %}"> </li></a>#}
{#    <a href="http://docs.docker.io/en/latest/installation/amazon/" target="_blank"><li>Amazon EC2 <img src="{% static 'img/platform-logos/amazonaws.png' %}"> </li></a>#}
{#    <a href="http://docs.docker.io/en/latest/installation/rackspace/" target="_blank"><li>Rackspace <img src="{% static 'img/platform-logos/rackspace.png' %}"> </li></a>#}
{#    <a href="http://docs.docker.io/en/latest/installation/archlinux/" target="_blank"><li>Arch Linux <img src="{% static 'img/platform-logos/archlinux.png' %}"> </li></a>#}
{#    <br style="clear: both">#}
{#</ul>#}


## 4. Run the examples

At this point you probably want to continue to the <a href="https://docs.docker.io/en/latest/examples/">examples</a> on the documentation


{% endblock %}