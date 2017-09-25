from django.contrib.auth.urls import url
from . import views


urlpatterns = [
    url(r'^character/add$', views.addkyara, name='addkyara'),
]

# + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
