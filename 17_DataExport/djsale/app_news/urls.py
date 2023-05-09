from django.urls import path
from app_news.views import NewsItemDetailView, NewsListView, HousingItemsListView

app_name = 'app_news'

urlpatterns = [
    path('housing_items/', HousingItemsListView.as_view(), name='housing-list'),
    path('<int:pk>/', NewsItemDetailView.as_view(), name='news-item'),
    path('', NewsListView.as_view(), name='news-list'),
]
