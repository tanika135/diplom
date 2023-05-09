from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime


class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [
            SitemapStaticItem(reverse('app_static:contacts')),
            SitemapStaticItem(reverse('app_static:about-us')),
        ]

    def lastmod(self, obj):
        return datetime.now()


class SitemapStaticItem:

    def __init__(self, url):
        self.url = url

    def get_absolute_url(self):
        return self.url
