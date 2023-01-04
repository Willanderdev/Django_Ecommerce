from django.apps import AppConfig
from watson import search as watson

class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
    
    def ready(self):
        Product = self.get_model("Product")
        watson.register(Product)
