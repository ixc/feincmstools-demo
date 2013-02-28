from django.db import models

class Meetup(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return "%s on %s" % (self.title, self.date)

    @models.permalink
    def get_absolute_url(self):
       return 'meetups:meetup', [self.slug]
