"""
Cascading settings.

* default.py contains settings that every deployment of this site will use. 
  It should be checked in to version control.

* local.py contains settings that vary from one deployment to the next, such 
  as DEBUG values. It should not be shared, though sample values can be 
  checked in as local.tmpl.py

TO USE:

The first line of local.py should be:

    from default import *

"""

try:
    # The first line of local.py should be "from default import *", then it 
    # can override those settings it sees fit.
    from .local import * 
except ImportError:
    from .default import *

# Settings that derive from other settings (e.g. DEBUG) go here.

TEMPLATE_CONSTANTS.update({
    'SITE_URL': SITE_URL,
    'SITE_NAME': SITE_NAME,
})


