from django.conf.urls import url, patterns, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
url(r'^$', views.index, name='index'),
url(r'^api/$', views.OrderList.as_view()),
url(r'^api/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)