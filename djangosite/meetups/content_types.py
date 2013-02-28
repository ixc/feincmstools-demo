from feincmstools.base import Content
from markitup.fields import MarkupField

class Text(Content):
    text = MarkupField(blank=True)

    class Meta:
        abstract=True