from django.apps import AppConfig
from django.db.models.signals import post_migrate


class NetflixConfig(AppConfig):
    name = 'netflix'

    def ready(self):
        from netflix import signals
        post_migrate.connect(signals.init_categories, sender=self)
