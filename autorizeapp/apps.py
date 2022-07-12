from django.apps import AppConfig


class AutorizeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autorizeapp'
    def ready(self):
        import autorizeapp.signals