"""formset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from formsetapp.views import person_formset_view, PersonList, PersonEdit, PersonDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^add-person/$', person_formset_view, name='add-person'),
    # url(r'^list-people/$', PersonList.as_view(), name='list-people'),
    # url(r'^edit-person/(?P<pk>\d+)/$', PersonEdit.as_view(), name='edit-person'),
    # url(r'^delete-person/(?P<pk>\d+)/$', PersonDelete.as_view(), name='delete-person')
    url(r'^person/', include('formsetapp.urls', namespace='person'))
]
