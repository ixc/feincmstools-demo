from feincmstools.fields import HierarchicalSlugField
from feincmstools.base import HierarchicalFeinCMSDocument
from django.db import models
from djangosite.feincms_conf.models import default_content_types_by_region

class Article(HierarchicalFeinCMSDocument, HierarchicalSlugField):
    title = models.CharField(max_length=255)
    slug = models.SlugField('slug', max_length=255, unique=True, db_index=True, help_text="A slug is a unique, URL-friendly version of the title.")


    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'magazine:article', [self.slug]

    feincms_templates = [
        {
            'key': 'base',
            'title': 'Standard template',
            'path': 'magazine/article.html',
            'regions': (
                ('main', 'Main content area'),
                ('related', 'Related articles', 'inherited'),
            ),
        }, {
            'key': 'issue',
            'title': 'Issue template',
            'path': 'magazine/issue.html',
            'regions': (), #no content.
        }, {
            'key': '2col',
            'title': 'Template with two columns',
            'path': 'magazine/article_2col.html',
            'regions': (
                ('col1', 'Column one'),
                ('col2', 'Column two'),
                ('related', 'Related articles', 'inherited'),
            ),
        }
    ]

    @classmethod
    def content_types_by_region(cls, region):
        # just use the default content types. You could override this as necessary.
        return default_content_types_by_region(region)