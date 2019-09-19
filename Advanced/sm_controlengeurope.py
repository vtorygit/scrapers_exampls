from urllib.parse import urlparse

from newsfeeds.spiders.templates.sitemap_template import ModSitemapSpider
from newsfeeds.items import ContentItems
from newsfeeds.item_functions import (process_item,
                                      process_singular_item,
                                      process_date_item,
                                      process_array_item,
                                      process_plural_texts,
                                      process_external_links,
                                      process_article_text)


HEADER_XPATH = ['//h1/text()']
AUTHOR_XPATH = [''] #no
PUBDATE_XPATH = ['//div[@id="article"]//p[@id="articledate"]/text()']
CATEGORY_XPATH = ['']#no
TAGS_XPATH = ['']#no
TEXT_XPATH = ['//div[@id="article"]//p[not(@id="articledate")]//text()[not(ancestor::style)]']
INTERLINKS = ['//div[@id="article"]//p[not(@id="articledate")]//a[not(ancestor::style)]/@href'] 
#09 July 2013
DATE_FORMAT_STRING = '%d %B %Y'

class controlEngeuropeSpider(ModSitemapSpider):
    name = 'sm_controlengeurope'
    allowed_domains = ["controlengeurope.com"]
    sitemap_urls = ["https://www.controlengeurope.com/sitemap.xml"]

    def parse(self, response):
        items = []
        item = ContentItems()
        item['title'] = process_singular_item(self, response, HEADER_XPATH, single=True)
        item['resource'] = urlparse(response.url).hostname
        item['author'] = process_array_item(self, response, AUTHOR_XPATH, single=False)
        item['pubdate'] = process_date_item(self, response, PUBDATE_XPATH, DATE_FORMAT_STRING, single=True)
        item['tags'] = process_plural_texts(self, response, TAGS_XPATH, single=False)
        item['category'] = process_plural_texts(self, response, CATEGORY_XPATH, single=False)
        item['article_text'] = process_article_text(self, response, TEXT)
        item['external_links'] = process_external_links(self, response, INTERLINKS, single=False)
        item['link'] = response.url
        items.append(item)
        return items
