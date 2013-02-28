from feincms.content.medialibrary.v2 import MediaFileContent
from .content_types import HorizontalRule
from djangosite.magazine.content_types import RelatedArticle
from djangosite.meetups.content_types import Text, RawHTMLContent, OEmbedContent

# A global/default content types function.
def default_content_types_by_region(region):
    """
    Return a list of content types that can be used in the given region.
    """

    # MediaFileContent is a built-in FeinCMS content type
    # hence the unwieldy parameter-passing.
    media_files = (MediaFileContent, dict(
        TYPE_CHOICES=(
            ('default', 'default'),
            ('lightbox', 'lightbox'),
        )
    ))

    standard_content_types = [
        (None, (Text, HorizontalRule)),
        ('Media', ( media_files, OEmbedContent)),
        ('Advanced', (RawHTMLContent,)),
    ]

    other_content_types = {
        'related': [ #from Magazine
            (None, (RelatedArticle,)),
        ],
        'left': [ # from Meetup.
            (None, (Text,)),
            ('Advanced', (RawHTMLContent,)),
        ]
    }

    return other_content_types.get(region, standard_content_types)


# If you're using FeinCMS's Page model or other external models, register extensions/templates here.
#from feincms.module.page.models import Page
#Page.register_extensions('datepublisher', 'changedate', ) # Example set of extensions
#
#Page.register_templates({
#    'title': _('Standard template'),
#    'path': 'pages/page.html',
#    'regions': (
#        ('main', _('Main content area')),
##        ('sidebar', _('Sidebar'), 'inherited'),
#        ),
#    })

#register these types for an external model.
#from feincmstools.models import create_content_types
#create_content_types(Page, default_content_types_by_region)


