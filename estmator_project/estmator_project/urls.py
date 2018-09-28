from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [

    # built-in or installed packages
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # root project urls
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^menu/$', views.menu_view, name='menu'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^connection-test$', views.connection_test, name='connection_test'),

    # estmator apps (all app urls are included through the api)
    url(r'^api/v1/', include('est_api.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
