from .models import SiteConfiguration

def site_config(request):
    try:
        config = SiteConfiguration.load()
        return {'site_config': config}
    except Exception:
        return {'site_config': None}
