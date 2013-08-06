{% extends 'homepage.html' %}
{% load list_tweets %}{% load static %}

{% block title %}Homepage - {% endblock %}
{% block meta-description %}Docker: An open source project to pack, ship and run any application as a lightweight container{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud{% endblock %}

{% block copy_headline %}

# an open source project to pack, ship and run any application as a lightweight container #

{% endblock %}


{% block copy_introduction %}
Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application.
    The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal,
    OpenStack clusters, public clouds and more. <span class="read-more"><a href="{% url 'about' %}" title="About Docker">Read more -></a></span>
{% endblock %}

{% block copy_news %}
### Latest updates

#### Aug 6 • now @docker on Twitter
This morning we changed our Twitter handle from getdocker to docker on twitter. So please tweet @docker now!

#### Jul 23 • Ben Golub Joins as CEO
Open source veteran Ben Golub joins as CEO to drive the docker vision forward. Read more:

[<img src="{% static 'img/homepage/gigaom.png' %}" alt="gigaom">](http://gigaom.com/2013/07/23/paas-pioneer-dotcloud-gets-new-ceo-in-industry-vet-ben-golub/)
[<img src="{% static 'img/homepage/reuters.png' %}" alt="reuters">](http://www.reuters.com/article/2013/07/23/ca-dotcloud-idUSnBw235523a+100+BSW20130723)
[<img src="{% static 'img/homepage/yahoo.png' %}" alt="yahoo finance">](http://finance.yahoo.com/news/dotcloud-appoints-ben-golub-chief-133000939.html)

#### Jul 18 • Docker 0.5 Released
We've released version 0.5. Amongst other things, this release containes External Volumes, Advanced Networking and
    support for an Self Hosted Registry,
    <span class="read-more"><a href="http://blog.docker.io/2013/07/docker-0-5-0-external-volumes-advanced-networking-self-hosted-registry/">read more -></a></span>

#### Jul 11 • Featuring awesome projects
Everyday the Docker community is building awesome tools and projects with and for Docker. We want to share some of these with you.
    <span class="read-more"><a href="http://blog.docker.io/2013/07/docker-projects-from-the-docker-community/">read more -></a></span>

#### Jun 25 • dotCloud and Docker join the Linux Foundation
By joining the foundation, we are excited to support the amazing open source contributions that have come before us, and support those yet to come!
    <span class="read-more"><a href="http://blog.docker.io/2013/06/dotcloud-and-docker-join-the-linux-foundation/">read more -></a></span>

#### Jun 6 • Docker in Openstack
Sam Alba presents an article about the integration of Docker in OpenStack's cloud computing platform: NOVA. This integration
    allows users of OpenStack to seamlessly create Docker containers from the interface they are already using.
    <span class="read-more"><a href="http://blog.docker.io/2013/06/openstack-docker-manage-linux-containers-with-nova/">read more -></a></span>


### Docker in the news

#### Jul 31 • Docker on Linux.com
[<img width="80px" style="float:left;margin-right:10px;" src="{% static 'img/homepage/linux.com.jpg' %}" alt="Linux.com">](http://www.linux.com/news/enterprise/cloud-computing/731454-docker-a-shipping-container-for-linux-code/) Docker: A 'Shipping Container' for Linux Code <span class="read-more"><a href="http://www.linux.com/news/enterprise/cloud-computing/731454-docker-a-shipping-container-for-linux-code/" target="_blank">read more -></a></span>

#### Jul 28 • Techcrunch on Docker and "The Matrix of Hell"
[<img width="80px" style="float:left;margin-right:10px;" src="{% static 'img/homepage/techcrunch.png' %}" alt="techcrunch">](http://techcrunch.com/2013/07/28/the-matrix-of-hell-and-two-open-source-projects-for-the-emerging-agnostic-cloud/) The Matrix Of Hell And Two Open-Source Projects For The Emerging Agnostic Cloud
<span class="read-more"><a href="http://techcrunch.com/2013/07/28/the-matrix-of-hell-and-two-open-source-projects-for-the-emerging-agnostic-cloud/" target="_blank">read more -></a></span>


{% endblock %}


{% block copy_community %}
### Community events

### Upcoming events
#### Boston OpenStack Meetup • Aug 14
<a href="https://twitter.com/golubbe" target="_blank">Ben Golub</a>, <a href="https://twitter.com/solomonstre" target="_blank">Solomon Hykes</a> and <a href="https://twitter.com/KenCochrane" target="_blank">Ken Cochrane</a> will be attending the next Boston OpenStak Meetup to talk about **Application Deployment on Openstack Using Containers and Docker** <a href="http://www.meetup.com/Openstack-Boston/events/131949152/" target="_blank">read more -></a>

#### CoderCamp13 in Hamilton, Canada • Aug 14
<a href="https://twitter.com/adr" target="_blank">John Fink</a> will talk about **<a href="http://docker.io">docker</a>, a lightweight virtual machine system implemented as a wrapper around Linux containers** <a href="http://codercamp.eventbrite.com/" target="_blank">read more -></a>

#### New York Docker Meetup • Aug 21
Join us for the first Docker Meetup in NYC <a href="http://www.meetup.com/Docker-meetups/events/131005192/" target="_blank">read more -></a>

#### Our previous Hack Day • Jul 30 (past):
Our hackday #6 was a success, with over 60 participants and, amongst others, great talks about how how people are using
    it in **EBay**, **Mailgun (Rackspace)** and **CloudFlare**.
    <span class="read-more disabled"><a href="{% url 'live' %}">watch sessions -></a></span>

<img src="{% static 'img/homepage/ebay.png' %}" title="logo's of EBay, Mailgun and CloudFlare">
<img src="{% static 'img/homepage/mailgun.png' %}" title="logo's of EBay, Mailgun and CloudFlare">
<img src="{% static 'img/homepage/cloudflare.png' %}" title="logo's of EBay, Mailgun and CloudFlare">

<a href="/live"><img src="http://farm4.staticflickr.com/3763/9409768665_966d0c08d9.jpg" width="500" height="375" alt="Docker Hck Day #6"></a>

{% endblock %}


{% block copy_1 %}

# The title #

{% endblock %}


{% block tweets %}
{% list_tweets %}

{#Extra's since docker hackday #6#}
362628082345050114
{#362601233980211202#}
{#362538212519981056#}
362465372949069824
{#362455829347176449#}
362414011612008448
362579117482323968
362350303997210625
{#362471730448572418#}
362432830657150976
362426814708203520
362397723242135553
362366694259294208
{#362359971612078081#}
{#362355578141556737#}
{#362341799680946176#}
{#362338537728782337#}
362319091178029056
{#362285886177677314#}
362277568092704769
362238819577245697
362083256922935297

{#As of July 19#}
{#354781876730335233#}
359360716584665088
357948061202386946
347003250299531264
347559367652032513
347915284977418241
348249053332647936
348281405974925313
354368422328541187
{#354970275353329664#}
{#355024956763021312#}
354954990277758978
355172662873567233
{#355346670520770561#}
{#355761264670162944#}
355705492087119875
355623162551083008
355404525793841153
{#355756267224047616#}
355955060607430656
354829574980378624
354411184524500992
{#354715613337354241#}
355705492087119875
{#355792575988371456#}
357972314660405249
356280542892802050
{#356763917625724928#}

{% end_list_tweets %}
{% endblock %}

