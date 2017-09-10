from django.contrib.auth.urls import url
from config.settings import base
from . import views
from django.conf.urls import static

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^userprofile/(?P<owner>[\w\-]+)$', views.displayprofile, name='displayprofile'),
    url(r'^character/new/$', views.addkyara, name='addkyara'),
    url(r'^friends/add/$', views.addfriend, name='addfriend'),
    url(r'^profile/edit$', views.displayProfileForm, name="editUserProfile"),
    url(r'^group/(?P<groupID>[\w\-]+)$', views.displaychat, name='displaychat'),

]

# + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
