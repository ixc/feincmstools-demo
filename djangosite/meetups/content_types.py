from django.db import models
from feincmstools.base import Content
from markitup.fields import MarkupField
from oembed.fields import OEmbedField

class Text(Content):
    text = MarkupField(blank=True)

    class Meta:
        abstract=True

class OEmbedContent(Content):
    url = OEmbedField()
    width = models.PositiveIntegerField(default=960, null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True, default=540, help_text="if left blank, a 16:9 aspect ratio is used")

    class Meta:
        abstract = True
        verbose_name = 'media from another site (OEmbed)'
        verbose_name_plural = 'media from another site (OEmbed)'

    def extra_context(self, request):
        if self.width:
            return {'dimensions': '%sx%s' % (
                self.width,
                self.height or int(self.width/16.0*9.0)
            ),}
        return {'dimensions': '0x0'}

class RawHTMLContent(Content):
    html = models.TextField(blank=True,
        help_text=('Renders the content as HTML.'))

    class Meta:
        abstract = True
        verbose_name = 'raw HTML'
        verbose_name_plural = 'raw HTML'
