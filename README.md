# Scrapers examples
The repo consists of 2 forlders:

`1` - <b> Basic examples </b> with most typical spiders <br>
`2` - <b> Advanced examples </b> with still typical, but no so obvoius solutions to extract necessary data


__________________________________________________________________________________________________________________

## Настройка окружения
Открыть терминал
<b>mac</b>: проблем, насколько знаю, быть не должно
<b>windows</b>: 
WIN+R (нажать сочетание клавиш)
вбить cmd и нажать кнопку ОК

или просто ищете во всех программах “командную строку”, она должна быть в стандартных программах


Установить питон

mac: 
на маках по умолчанию должен ставиться 3, ничего указывать не надо
в терминале делаете:
`brew install python`
`export PATH="/usr/local/opt/python/libexec/bin:/usr/local/bin:$PATH"`
закрыть терминал и снова его открыть, чтобы изменения применились
в терминале пишете:
`python --version`
если не возникает ошибок, питон поставился нормально

windows: скачиваете с официального сайта и устанавливаете как обычную программу. Нужен python 3. https://www.python.org/downloads/

и для удобства установить pip как тут написано:
https://www.liquidweb.com/kb/install-pip-windows/

1. Download get-pip.py to a folder on your computer.
2. Open a command prompt and navigate to the folder containing get-pip.py.
3. Run the following command:python get-pip.py
4. Pip is now installed!


Виртуальная среда

mac:
в терминале:
`pip install virtualenv`
`pip install virtualenvwrapper`
`export WORKON_HOME=~/.virtualenvs`
`[ -f /usr/local/bin/virtualenvwrapper.sh ] && source /usr/local/bin/virtualenvwrapper.sh`
закрыть терминал и открыть снова
создать виртуальную среду командой (вместо теста название среды - какое хотите)

`mkvirtualenv scrapim`

активировать среду командами:
`source venv/bin/activate`    тут venv - имя, которое вы задали выше (scrapim)
к имени пользователя и названию компьютера должно добавиться имя среды - это значит, что вы активировали среду и все ок.

Когда вы заканчиваете работу со средой, отключить ее нужно командой deactivate
________________________
windows:
в терминале написать `pip list` и найти в конце списка vitrualenv - он должен стоять по умолчанию

`python -m venv scrapim`  (вместо scrapim можно написать любое другое название, но нужно его запомнить)

если написать `dir` и нажать enter, среди списка должно появиться введенное имя

запустить в терминале:
`scrapim\Scripts\activate.bat`
в самом начале строки (где указан путь к папке, диск и пр.) должно добавиться имя среды в круглых кавычках

как деактивировать видно на видео

Скрэпи

при активированной среде:

mac: `pip install Scrapy`
windows: `pip install Scrapy`

такие команды нашлись в интернете. Если не запустится, попробуйте написать scrapy вместо Scrapy


Запустить шэлл командой `scrapy shell` и попробовать подключиться к любому сайту командой `fetch(‘www.ya.ru’)`


