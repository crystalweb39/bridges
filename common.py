from bridges.website.models import *
from django.conf import settings

def commondict(d,request):
    try:
        sitemeta = SiteMeta.objects.get(site__id=settings.SITE_ID)
    except:
        sitemeta = ''
        
    misc = MiscPage.objects.filter(active=True)
    
    data = {
            'site_meta':sitemeta,
            
            'misc':misc,
            
            }
    
    
    data.update(d)
    
    return data