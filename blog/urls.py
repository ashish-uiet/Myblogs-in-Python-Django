from django.conf.urls import url
from django.contrib import admin
from .views import *

# app_name = 'blog'
urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^add-keyword/$', add_keyword, name='add_keyword'),
    url(r'^add-code/$', add_code, name='add_code'),
    url(r'^keyword-opportunities/$', profile, name='profile'),
    url(r'^code-opportunities/$', code_opportunities, name='code_opportunities'),
    url(r'^opportunities/$', list_user_opportunities, name='list_user_opportunities'),
    url(r'^add-opportunity-request/$', add_opportunity_request, name='add_opportunity_request'),
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r'^test/$', test, name='test'),
    url(r'^', home, name='home'),
    url(r'^admin/', admin.site.urls),
]

