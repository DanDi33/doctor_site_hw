from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminPanel'

    def ready(self):
        import adminPanel.signals