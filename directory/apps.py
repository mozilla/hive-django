from django.apps import AppConfig

class HiveDirectoryConfig(AppConfig):
    name = 'directory'
    verbose_name = 'Hive Directory'

    def ready(self):
        from . import signals
