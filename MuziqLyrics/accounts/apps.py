from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MuziqLyrics.accounts'

    def ready(self):
        import MuziqLyrics.accounts.signals
