from django.apps import AppConfig


class ProfileConfig(AppConfig):
    name = 'est_profile'
    verbose_name = 'Estmator Profile'

    def ready(self):
        from . import handlers
