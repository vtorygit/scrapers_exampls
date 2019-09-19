from urllib.parse import urlparse

from newsfeeds.spiders.templates.static_categories_spider import StaticCategoriesSpider
from scrapy.linkextractors import LinkExtractor
from newsfeeds.items import ContentItems
from newsfeeds.item_functions import (clear_text,
                        process_item,
                        process_singular_item,
                        process_date_item,
                        process_array_item,
                        process_plural_texts,
                        process_external_links,
                        process_article_text,
                        process_text_array_from_string)

HEADER_XPATH = ['//h1/text()']
AUTHOR_XPATH = ['//span[@itemprop="name"]/text()']
PUBDATE_XPATH = ['//p[@class="single-header__meta"]/time/@datetime']
TAGS_XPATH = ['']#no
CATEGORY_XPATH = ['']#no 
TEXT_XPATH = ['//section[@itemprop="articleBody"]//text()']
INTERLINKS = ['//section[@itemprop="articleBody"]//@href']
#2019-07-23T07:56:44-04:00
DATE_FORMAT_STRING = '%Y-%m-%d'


class eosSpider(StaticCategoriesSpider):
    name = 's_eos'
    allowed_domains = ["eos.org"]
    start_urls = ['https://eos.org/articles', 'https://eos.org/science-updates', 'https://eos.org/meeting-reports', 'https://eos.org/agu-news']  
    next_page = LinkExtractor(restrict_xpaths=('//li/a[@class="next page-numbers"]'))
    article_links = LinkExtractor(restrict_xpaths=('//article/h3/a[@class="excerpt-item__link"]'))

    def parse_page(self, response):
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
