from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from views import uploadgrade, current_courselist, all_courselist

urlpatterns = patterns('',
    url(r'^uploadgrade/(\d+)/$',uploadgrade, name='uploadgrade'),
    url(r'currentlist/$', current_courselist, name="currentlist"),
    url(r'alllist/$', all_courselist, name="alllist"),
)