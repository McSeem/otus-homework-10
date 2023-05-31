"""
Модуль настройки приложений проекта.
"""
from django.apps import AppConfig


class LmsbaikalConfig(AppConfig): # pylint: disable=too-few-public-methods
    """
    Класс настроек приложения lmsbaikal.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lmsbaikal'
