from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webponto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'accounts.views.register'),
    url(r'^login/$', 'accounts.views.user_login'),
    url(r'^logout/$', 'accounts.views.user_logout'),
)
