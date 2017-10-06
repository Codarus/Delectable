from django.conf.urls import url, patterns, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
url(r'^$', views.CreateOrder, name='CreateOrder'),
url(r'^vieworder/', views.ViewOrder, name='ViewOrder'),
url(r'^confirmation/', views.ConfirmOrder, name='confirm'),
url(r'^find/', views.SearchOrder, name='search'),
url(r'^finddate/', views.SearchDateOrder, name='searchdate'),
url(r'^ledger/', views.SeeProfitOrder, name='ledger'),
url(r'^item/$', views.ItemList.as_view()),
url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
url(r'^order/$', views.OrderList.as_view()),
url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
url(r'^customer/$', views.CustomerList.as_view()),
url(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
url(r'^updateorder/(?P<pk>[0-9]+)/$', views.CancelOrder.as_view(), name='cancel'),
url(r'^updateitem/(?P<pk>[0-9]+)/$', views.UpdateItem.as_view(), name='update-item'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
