HEADER_XPATH = ['(//h1/text())[2]']
AUTHOR_XPATH = ['']
PUBDATE_XPATH = ['//meta[@property="article:published_time"]/@content']
TAGS_XPATH = ['//meta[@property="article:tag"]/@content']
CATEGORY_XPATH = ['']#no 
TEXT_XPATH = ['//div[@class="the-content"]/p//text()']
INTERLINKS = ['//div[@class="the-content"]/p//@href']
#2009-11-16T15:11:30+00:00
DATE_FORMAT_STRING = '%Y-%m-%d'

    allowed_domains = ["helicoptersmagazine.com"]
