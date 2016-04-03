from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	# ex: /enquiry/
    url(r'^$', views.index, name='index'),
    # ex: /enquiry/5/
    #url(r'^(?P<form_id>[0-9]+)/$', views.save_data, name='save_data'),
    # ex: /enquiry/5/info/
    url(r'^(?P<contact_no>[0-9]+)/info/$', views.info, name='info'),
	# ex: /enquiry/save_data
    url(r'^save_data/$', views.save_data, name='save_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)