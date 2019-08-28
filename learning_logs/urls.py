from django.conf.urls import url
from learning_logs import views

urlpatterns = [

    url(r'^index/$', views.index),
    url(r'^topics/$', views.topics),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic,name='topic'),
    url(r'^new_topic/$', views.new_topic),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry),




]