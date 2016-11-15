from django.conf.urls import url
from grace.members_area.views import MembersView, LoginFormView, RegisterFormView, detail

urlpatterns = [
    url(r'^membros/$', MembersView.as_view(), name='members_area'),
    url(r'^success/(\d+)/$', detail, name='success'),
    url(r'^login/', LoginFormView.as_view(), name='login'),
    url(r'^register/', RegisterFormView.as_view(), name='register'),
]


