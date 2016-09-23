from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^api/$', views.PostList.as_view()),
    url(r'^api/(?P<pk>\d+)/$', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
