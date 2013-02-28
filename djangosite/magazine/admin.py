from django.contrib import admin
from feincmstools.admin import HierarchicalFeinCMSDocumentAdmin
from .models import Article

class ArticleAdmin(HierarchicalFeinCMSDocumentAdmin):
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(Article, ArticleAdmin)