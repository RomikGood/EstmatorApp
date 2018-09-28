from django.conf.urls import url
from . import views

urlpatterns = [
    # urls begin with /quote/

    # url(r'^$', views.quote_view, name='api_quote'), # not sure what the api urls are doing currently

    url(r'^$', views.quote_view, name='quote'),
    url(r'^review$', views.review_quote_view, name='review'),
    url(r'^form$', views.quote_form_view, name='quote_form'),
    url(r'^send/(?P<pk>\d+)', views.send_quote, name='send_quote'),
    url(
        r'^(?P<token>[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12})$',
        views.quote_from_token,
        name='quote_from_token'
    ),
    url(
        r'^form/edit$',
        views.quote_edit_form_view,
        name='quote_edit_form'
    )

]
