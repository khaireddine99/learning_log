"""defines urls patterns for learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    # topic page
    url(r'^topics/$', views.topics, name='topics'),
    # details for a single topics
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # page for adding a topics
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
