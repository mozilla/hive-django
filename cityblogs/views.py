import datetime
from urlparse import urljoin
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
import feedparser

from .models import CityBlog
from directory.models import Organization

CACHE_SECONDS = 60 * 3

def organization_posts(request, organization_slug):
    '''
    Return a list of blog posts associated with the given
    organization. This returns an HTML snippet that should be
    included asynchronously via ajax.
    '''

    org = get_object_or_404(Organization, slug=organization_slug,
                            is_active=True)
    cityblog = get_object_or_404(CityBlog, city=org.city)
    url = urljoin(cityblog.url, '/tag/%s/feed/' % organization_slug)
    key = 'cityblog_%s' % url
    feed = cache.get(key)
    if feed is None:
        feed = feedparser.parse(url)
        cache.set(key, feed, CACHE_SECONDS)
    for entry in feed['entries']:
        year, month, day = entry['published_parsed'][:3]
        entry['published_datetime'] = datetime.date(year, month, day)
    return render(request, 'cityblogs/organization_posts.html', {
        'org': org,
        'entries': feed['entries']
    })
