from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from app_news.models import NewsItem


class LatestNewsFeed(Feed):
    title = "News"
    link = "/sitenews/"
    description = "Most latest news."

    def items(self) -> QuerySet:
        return NewsItem.objects.order_by('-published_at')[:5]

    def item_title(self, item: NewsItem) -> str:
        return item.title

    def item_description(self, item: NewsItem) -> str:
        return item.description

    def item_link(self, item: NewsItem) -> str:
        return reverse('app_news:news-item', args=[item.pk])
