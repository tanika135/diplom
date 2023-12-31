from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views import generic

from app_news.models import NewsItem, HousingItem


def get_news_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest
    data = serializers.serialize(format, NewsItem.objects.all())
    return HttpResponse(data)


class NewsItemDetailView(generic.DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'


class NewsListView(generic.ListView):
    model = NewsItem
    context_object_name = 'news'
    template_name = 'app_news/newsitem_list.html'


class HousingItemsListView(generic.ListView):
    model = HousingItem
    context_object_name = 'housingitems'
    template_name = 'app_news/housingitem_list.html'

