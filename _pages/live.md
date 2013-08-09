{% extends 'about.html' %}
{% load static %}
{% block title %}About Docker - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}


{% block copy_headline %}
# Follow what is going on at the Docker hack-day, live. #
{% endblock %}

{% block copy_introduction %}
## Docker Hack Day #6

The Docker Hack Day #6 is over. Tomorrow we will post the edited videos of the lightning talks, including:

*   <a href="https://twitter.com/dozba">Ted Dzubia</a> on how he uses Docker at <a href="http://www.ebay.com">Ebay</a>
*   <a href="https://twitter.com/sebp">Sebastien Pahl</a> on how he uses Docker at <a href="http://www.cloudflare.com">CloudFlare</a>
*   Sasha Klizhentas on how he uses Docker at <a href="http://www.mailgun.com">MailGun</a>

Stay tuned!

<img src="{% static 'img/temp/docker_hackday_6_videos.png' %}" alt="docker hackday img">

In the meantime check out our <a href="{% url 'community' %}" class="" title="community page">Community page</a>

{% endblock %}