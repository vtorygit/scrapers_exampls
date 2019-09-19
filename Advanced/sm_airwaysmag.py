from urllib.parse import urlparse

from newsfeeds.spiders.templates.sitemap_template import ModSitemapSpider
from newsfeeds.items import ContentItems
from newsfeeds.item_functions import (clear_text, process_item,
                                      process_singular_item,
                                      process_date_item,
                                      process_array_item,
                                      process_plural_texts,
                                      process_external_links,
                                      process_article_text)

HEADER_XPATH = ['//title/text()']
AUTHOR_XPATH = ['//div//a[@rel="author"]/text()']
PUBDATE_XPATH = ['//meta[@property="article:published_time"]/@content']
TAGS_XPATH = ['']#no
CATEGORY_XPATH = ['']#no 
TEXT_XPATH = ['//div[@class="shortcode-content"]//p//text()']
INTERLINKS = ['']#no
DATE_FORMAT_STRING = '%Y-%m-%d'


class airwaysmagSpider(ModSitemapSpider):
    name = 'sm_airwaysmag'
    allowed_domains = ["airwaysmag.com"]
    sitemap_urls = ['https://airwaysmag.com/post-sitemap1.xml', 'https://airwaysmag.com/post-sitemap2.xml', 'https://airwaysmag.com/post-sitemap3.xml', 'https://airwaysmag.com/post-sitemap4.xml', 'https://airwaysmag.com/post-sitemap5.xml', 'https://airwaysmag.com/post-sitemap6.xml']

    def parse(self, response):
        items = []
        item = ContentItems()
        item['title'] = process_singular_item(self, response, HEADER_XPATH, single=True)
        item['resource'] = urlparse(response.url).hostname
        item['author'] = process_array_item(self, response, AUTHOR_XPATH, single=False)
        if item['author'] is not None:
            authors = []
            for author in item['author']:
                authors.append(clear_text(author).replace(' by  ', ''))
                
        item['pubdate'] = process_date_item(self, response, PUBDATE_XPATH, DATE_FORMAT_STRING, single=True)
        item['tags'] = process_plural_texts(self, response, TAGS_XPATH, single=False)
        item['category'] = process_plural_texts(self, response, CATEGORY_XPATH, single=False)
        item['article_text'] = process_article_text(self, response, TEXT_XPATH)
        item['external_links'] = process_external_links(self, response, INTERLINKS, single=False)
        item['link'] = response.url
        items.append(item)
        return items
