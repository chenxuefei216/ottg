"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url

from lists import views

urlpatterns = [
    #^means begin, $ means end
    url(r'^new$', views.new_list, name="new_list"),
    url(r'^(\d+)/add_item$', views.add_item, name="add_item"),
    url(r'^items/(\d+)/delete_item$', views.delete_item, name='delete_item'),
    # "()" means to capture what is between the "/ /"
    url(r'^(\d+)/$', views.view_list, name="view_list"),

]
