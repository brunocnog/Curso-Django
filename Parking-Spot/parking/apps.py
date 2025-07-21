from django.apps import AppConfig


class ParkingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parking'
    verbose_name = 'Vagas'

    def ready(self):
        import parking.signals # noqa F401
