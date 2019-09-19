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

HEADER_XPATH = ['(//h1/text())[2]']
AUTHOR_XPATH = ['']
PUBDATE_XPATH = ['//meta[@property="article:published_time"]/@content']
TAGS_XPATH = ['//meta[@property="article:tag"]/@content']
CATEGORY_XPATH = ['']#no 
TEXT_XPATH = ['//div[@class="the-content"]/p//text()']
INTERLINKS = ['//div[@class="the-content"]/p//@href']
#2009-11-16T15:11:30+00:00
DATE_FORMAT_STRING = '%Y-%m-%d'


class helicoptersMagazineSpider(StaticCategoriesSpider):
    name = 's_helicoptersmagazine'
    allowed_domains = ["helicoptersmagazine.com"]
    start_urls = ['https://www.helicoptersmagazine.com/category/news/']  
    next_page = LinkExtractor(restrict_xpaths=('//li//a[text()="Next →"]'))
    article_links = LinkExtractor(restrict_xpaths=('//a[@class="thumbnail headline clearfix media"]'))

    def parse_page(self, response):
        items = []
        item = ContentItems()
        item['title'] = process_singular_item(self, response, HEADER_XPATH, single=True)
        item['resource'] = urlparse(response.url).hostname
        item['author'] = process_array_item(self, response, AUTHOR_XPATH, single=False)
        authors = []
        if item['author'] is not None:            
            for name in item['author']:
                authors.append(clear_text(name).replace('by', ''))
        item['pubdate'] = process_date_item(self, response, PUBDATE_XPATH, DATE_FORMAT_STRING, single=True)
        item['tags'] = process_plural_texts(self, response, TAGS_XPATH, single=False)
        item['category'] = process_plural_texts(self, response, CATEGORY_XPATH, single=False)
        item['article_text'] = process_article_text(self, response, TEXT_XPATH)
        item['external_links'] = process_external_links(self, response, INTERLINKS, single=False)
        item['link'] = response.url
        items.append(item)
        return items
