from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # overriding signals to customer dispatcher
    def ready(self):
        # from resume.main import signals
        import main.signals