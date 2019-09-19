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
AUTHOR_XPATH = ['//span[@itemprop="author"]/a/text()']
PUBDATE_XPATH = ['//time[@class="value-title"]/@datetime']
CATEGORY_XPATH = ['']#no
TAGS_XPATH = ['']#no
TEXT_XPATH = ['//div[@itemprop="articleBody"]/p//text()']
INTERLINKS = [''] #were not found
#2019-08-02T06:35:33+01:00
DATE_FORMAT_STRING = '%Y-%m-%d'

class farmBusinessSpider(ModSitemapSpider):
    name = 'sm_farmbusiness'
    allowed_domains = ["farmbusiness.co.uk"]
    sitemap_urls = ['http://www.farmbusiness.co.uk/sitemap.xml']

        
    def parse(self, response):
        items = []
        item = ContentItems()
        item['title'] = process_singular_item(self, response, HEADER_XPATH, single=True)
        item['resource'] = urlparse(response.url).hostname
        item['author'] = process_array_item(self, response, AUTHOR_XPATH, single=False)
        item['pubdate'] = process_date_item(self, response, PUBDATE_XPATH, DATE_FORMAT_STRING, single=True)
        item['tags'] = process_plural_texts(self, response, TAGS_XPATH, single=False)
        item['category'] = process_plural_texts(self, response, CATEGORY_XPATH, single=False)
        item['article_text'] = process_article_text(self, response, TEXT_XPATH)
        item['external_links'] = process_external_links(self, response, INTERLINKS, single=False)
        item['link'] = response.url
        items.append(item)
        return items
