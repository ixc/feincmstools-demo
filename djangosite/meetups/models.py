from django.db import models
from feincms.content.medialibrary.v2 import MediaFileContent
from feincmstools.base import FeinCMSDocument
from .content_types import Text, OEmbedContent, RawHTMLContent

class Meetup(FeinCMSDocument):
    date = models.DateField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return "%s on %s" % (self.title, self.date)

    @models.permalink
    def get_absolute_url(self):
       return 'meetups:meetup', [self.slug]

    feincms_regions = (
            ('main', 'Main'),
            ('left', 'Left sidebar'),
    )

    @classmethod
    def content_types_by_region(cls, region):
        if region == 'left':
            return [
                (None, (Text,)),
                ('Advanced', (RawHTMLContent,)),
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