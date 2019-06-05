

import urllib

from urllib import request
ret = request.urlopen('https://movie.douban.com/top250?start=%s&filter=')
print(ret.read().decode('utf-8'))