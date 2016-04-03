from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'enquiry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^enquiry/', include('enquiryforms.urls', namespace="enquiry")),
    url(r'^admin/', include(admin.site.urls)),
]
