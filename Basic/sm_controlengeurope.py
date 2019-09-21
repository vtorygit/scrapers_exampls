
HEADER_XPATH = ['//h1/text()']
AUTHOR_XPATH = [''] #no
PUBDATE_XPATH = ['//div[@id="article"]//p[@id="articledate"]/text()']
CATEGORY_XPATH = ['']#no
TAGS_XPATH = ['']#no
TEXT_XPATH = ['//div[@id="article"]//p[not(@id="articledate")]//text()[not(ancestor::style)]']
INTERLINKS = ['//div[@id="article"]//p[not(@id="articledate")]//a[not(ancestor::style)]/@href'] 
#09 July 2013
DATE_FORMAT_STRING = '%d %B %Y'

# controlengeurope.com
