
HEADER_XPATH = ['//h1[@class="title"]/a/text()']
AUTHOR_XPATH = [''] #no
PUBDATE_XPATH = ['//span[@class="articlecreatedon"]/text()']
TAGS_XPATH = [''] #no
CATEGORY_XPATH = ['']#no 
TEXT_XPATH = ['//div[@class="articletext"]//p//text() | //div[@class="articletext"]/ul/li/text()']
INTERLINKS = ['//div[@class="articletext"]//p//@href']
#Published on 15 July 2019
DATE_FORMAT_STRING = 'Published on %d %B %Y'

    allowed_domains = ["progressiveforage.com"]

