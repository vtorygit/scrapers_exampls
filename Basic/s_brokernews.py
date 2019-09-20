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

HEADER_XPATH = ['//h1[@class="page_title"]/text()']
AUTHOR_XPATH = ['//span[@class="author"]/a/text()']
PUBDATE_XPATH = ['//span[@class="date"]/text()']
TAGS_XPATH = ['']#no
CATEGORY_XPATH = ['']#no 
TEXT_XPATH = ['//div[@class="article_body"]/p//text()']
INTERLINKS = ['//div[@class="article_body"]//p//a/@href']
#13 Jul 2019
DATE_FORMAT_STRING = '%d %b %Y'


class insuranceBusinessMagSpider(StaticCategoriesSpider):
    name = 's_brokernews'
    allowed_domains = ["brokernews.com.au"]
    start_urls = ['https://www.brokernews.com.au/news/breaking-news/']  
    next_page = LinkExtractor(restrict_xpaths=('//div[@class="pager"]/a[@class="current"]/following-sibling::a[1]'))
    article_links = LinkExtractor(restrict_xpaths=('//div[@class="latest_news"]//li//a'))

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

      
# //div[@class="pager"]/a[@class="current"]/following-sibling::a[1]/@href
