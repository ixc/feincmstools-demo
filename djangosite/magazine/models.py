from feincms.content.medialibrary.v2 import MediaFileContent
from feincmstools.fields import HierarchicalSlugField
from feincmstools.base import HierarchicalFeinCMSDocument
from django.db import models
from .content_types import RelatedArticle
from djangosite.meetups.content_types import Text, OEmbedContent, RawHTMLContent

class Article(HierarchicalFeinCMSDocument, HierarchicalSlugField):
    title = models.CharField(max_length=255)
    slug = models.SlugField('slug', max_length=255, unique=True, db_index=True, help_text="A slug is a unique, URL-friendly version of the title.")


    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'magazine:article', [self.slug]

    feincms_regions = (
        ('main', "Main"),
        ('related', "Related articles"),
    )

    @classmethod
    def content_types_by_region(cls, region):
        if region == 'related':
            return [
                (None, (RelatedArticle,)),
            ]

        # MediaFileContent is a built-in FeinCMS content type
        # hence the unwieldy initialisation.
        media_files = (MediaFileContent, dict(
                TYPE_CHOICES=(
                    ('default', 'default'),
                    ('lightbox', 'lightbox'),
                )
        ))

        return [
            (None, (Text,)),
            ('Media', ( media_files, OEmbedContent)),
            ('Advanced', (RawHTMLContent,)),
        ]