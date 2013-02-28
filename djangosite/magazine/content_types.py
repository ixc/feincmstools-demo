from feincmstools.base import Content
from django.db import models
from feincmstools.forms import FormWithRawIDFields

class RelatedArticleForm(FormWithRawIDFields):
    raw_id_fields = ('article', )

class RelatedArticle(Content):
    article = models.ForeignKey('Article', related_name="+")

    feincms_item_editor_form = RelatedArticleForm

    class Meta:
        abstract = True