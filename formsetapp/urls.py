from django.conf.urls import url
from formsetapp.views import person_formset_view, PersonList, PersonEdit, PersonDelete, PersonDetail

urlpatterns = [
  url(r'^add/$', person_formset_view, name='add'),
  url(r'^list/$', PersonList.as_view(), name='list'),
  url(r'^edit/(?P<pk>\d+)/$', PersonEdit.as_view(), name='edit'),
  url(r'^detail/(?P<pk>\d+)/$', PersonDetail.as_view(), name='detail'),
  url(r'^delete/(?P<pk>\d+)/$', PersonDelete.as_view(), name='delete')
]