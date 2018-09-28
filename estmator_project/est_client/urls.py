from django.conf.urls import url
from . import views

urlpatterns = [
    # urls begin with /client/

    url(r'^$', views.client_view, name='api_client'), # not sure what the api urls are doing currently

    url(
        r'^form$',
        views.client_form_view,
        name='client_form'
    ),
    url(
        r'^form/edit$',
        views.client_edit_form_view,
        name='client_edit_form'
    ),
    url(
        r'^listform$',
        views.client_list_form_view,
        name='client_list_form'
    ),
    url(r'^company/$', views.company_view, name='api_company'),
    url(
        r'^company/form$',
        views.company_form_view,
        name='company_form'
    ),
    url(
        r'^company/form/edit$',
        views.company_edit_form_view,
        name='company_edit_form'
    ),
    url(
        r'^company/listform$',
        views.company_list_form_view,
        name='company_list_form'
    )

]
