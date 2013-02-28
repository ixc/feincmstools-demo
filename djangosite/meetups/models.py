from django.db import models
from feincmstools.base import FeinCMSDocument
from djangosite.feincms_conf.models import default_content_types_by_region

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
        # just use the default content types. You could override this as necessary.
        return default_content_types_by_region(region)