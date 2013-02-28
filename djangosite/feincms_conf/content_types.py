from feincmstools.base import Content

class HorizontalRule(Content): #No need to use any fields
    class Meta:
        abstract = True

    def __unicode__(self):
        return "Horizontal Rule"