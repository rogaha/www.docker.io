{% extends 'about/press.html' %}
{% load static %}
{% block title %}Press - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}

{% block copy_headline %}
# What people are saying and writing about Docker #
{% endblock %}

{% block copy_introduction %}

## Docker in the news

Docker is an open source project that relies on the support of a great community of contributors worldwide.


* #### Jul 31 • Docker on Linux.com

    Docker: A 'Shipping Container' for Linux Code <span class="read-more"><a href="http://www.linux.com/news/enterprise/cloud-computing/731454-docker-a-shipping-container-for-linux-code/" target="_blank">read more -></a></span>

    <img width="160px" src="{% static 'img/press-logos/linux.com_150.png' %}" alt="Linux.com">

* #### Jul 28 • Techcrunch on Docker and "The Matrix of Hell"

    The Matrix Of Hell And Two Open-Source Projects For The Emerging Agnostic Cloud
    <span class="read-more"><a href="http://techcrunch.com/2013/07/28/the-matrix-of-hell-and-two-open-source-projects-for-the-emerging-agnostic-cloud/" target="_blank">read more -></a></span>

    <img width="80px" style="margin:15px;" src="{% static 'img/homepage/techcrunch.png' %}" alt="techcrunch">


{### Projects using Docker#}

{#* projects using docker#}
{#    **Deis**#}
{#    Deis #}
{##}
{#   - http://www.memcachedasaservice.com#}
{#   - http://blog.frozenridge.co/next-generation-continuous-integration-deployment-with-dotclouds-docker-and-strider/#}
{##}
{#  - Web Interface for docker DockerUI:#}
{#        * Link: https://github.com/crosbymichael/dockerui#}
{#        * Video: https://www.youtube.com/watch?v=d4CCClXB_fs#}
{#        * HN: https://news.ycombinator.com/item?id=5853033#}

## Blogposts on Docker

1. Blog posts on how to work with Docker

   - [Rob Knight        - Drupal on Docker                                              - May 13        ](http://robknight.org.uk/blog/2013/05/drupal-on-docker/)
   - [Puppet forge      - Puppet module for installing Docker from the official PPA.    - May 12, 2013  ](http://forge.puppetlabs.com/garethr/docker)
   - [Ken Cochrane      - Running docker on Rackspace cloud                             - May 2013      ](http://kencochrane.net/blog/2013/05/running-docker-on-rackspace-cloud/)
   - [John Costa        - Installing redis on Docker                                    - Apr 7, 2013   ](http://www.johnmcostaiii.net/2013/installing-redis-on-docker/)
   - [Slideshare        - Building a SaaS using Docker                                  - Arp 14, 2013  ](http://www.slideshare.net/julienbarbier42/building-a-saas-using-docker)
   - [Flavio Castelli   - Docker and OpenSuse                                           - Arp 12, 2013  ](http://flavio.castelli.name/2013/04/12/docker-and-opensuse/)
   - [Atlassion:        - Deploy Java Apps With Docker = Awesome                        - June 13, 2013 ](http://blogs.atlassian.com/2013/06/deploy-java-apps-with-docker-awesome/)


{#    http://www.rackspace.com/blog/get-faster-more-affordable-cloud-applications-with-os-virtualization-containers/#}


{#2. podcasts, and videos#}
{##}
{#  - http://thechangelog.com/89/#}
{#  - http://foodfightshow.org/2013/04/docker-the-linux-container-runtime.html#}
{#  - http://trafficandweather.io/posts/2013/5/12/episode-11-#}
{#  - http://www.youtube.com/watch?v=3N3n9FzebAA dotScale 2013 - Solomon Hykes - Why we built Docker#}
{##}
{#6. presentations and lightning talks (slides + videos)#}
{#   - Solomon pycon lightning talk (already have, but link as well?)#}
{#   - videos of the docker hack day presentations?#}
{#   - Brian McCallister at atmosphereconf https://atmosphere-conference.com/en/lecture/48/#}
{#   - Jef Lindsay & Solomon	Hykes Building Your Own PaaS with Docker at GlueCon 2013 (video: http://vimeo.com/67284401)#}
{##}
{#7. API and other libs for docker#}
{#   - http://rubygems.org/gems/kitchen-docker#}
{#   - https://github.com/brianm/docker-play#}
{##}
{#8. Other articles#}
{#   - http://www.infoq.com/news/2013/03/Docker#}
{#   - http://kuhnza.com/2013/03/27/docker-makes-creating-secure-sandboxes-easier-than-ever/#}
{#   - http://thechangelog.com/docker-from-dotcloud-is-now-open-source-the-future-of-linux-containers/#}


**If you find an interesting article is missing.. Please make a pull request to [this page](https://github.com/dotcloud/www.docker.io/blob/master/_pages/about/press.md)**

{% endblock %}

