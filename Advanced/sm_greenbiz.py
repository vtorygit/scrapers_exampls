
HEADER_XPATH = ['//title/text()']
AUTHOR_XPATH = ['//meta[@name="dcterms.creator"]/@content']
PUBDATE_XPATH = ['//meta[@name="dcterms.date"]/@content']
CATEGORY_XPATH = ['']#no
TAGS_XPATH = ['']#no
TEXT_XPATH = ['(//div[@class="field-item even"]//p//text()) | (//div[@class="field-items"]//div/text())']
INTERLINKS = ['(//div[@class="field-item even"]//p/a/@href) | (//div[@class="field-items"]//div//@href)'] 
#2017-06-09T02:25-07:00
DATE_FORMAT_STRING = '%Y-%m-%d'

# greenbiz.com
