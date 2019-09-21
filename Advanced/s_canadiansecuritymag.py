
HEADER_XPATH = ['(//h1/text())[2]']
AUTHOR_XPATH = ['//p[@class="muted"]/a/text()']
PUBDATE_XPATH = ['//meta[@property="article:published_time"]/@content']
TAGS_XPATH = ['//meta[@property="article:tag"]/@content'] #were not seen
CATEGORY_XPATH = ['']#no 
TEXT_XPATH = ['//div[@class="the-content"]/p//text()']
INTERLINKS = ['//div[@class="the-content"]/p//@href']
#2009-01-14T19:54:26+00:00
DATE_FORMAT_STRING = '%Y-%m-%d'
