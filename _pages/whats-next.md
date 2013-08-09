{% extends 'whats-next.html' %}
{% load static %}
{% block title %}What's next - {% endblock %}
{% block meta-description %}Docker is an open-source engine that automates the deployment of any application as a lightweight, portable, self-sufficient container that will run virtually anywhere. Learn more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, containers, how it works{% endblock %}

{% block copy_headline %}
# Great, you've got the basics down, what next?


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


## 2. Setup a machine in the cloud to run Docker

If you want to setup a machine to get up and running with Docker quickly, one of the fastest ways is to setup a
    virtual machine on one of the public clouds. Digital Ocean provides one of the cheapest options with
    virtual servers for a flat $5 / month.

<a href="https://www.digitalocean.com/?refcode=9152ecbd91ab" target="_blank" title="referral link to Digital Ocean"><img src="{% static 'img/community/digital-ocean-horizontal.jpg' %}"><br /> </a>


## 3. Install Docker

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


## 4. Run the examples

At this point you probably want to continue to the <a href="https://docs.docker.io/en/latest/examples/">examples</a> on the documentation


{% endblock %}