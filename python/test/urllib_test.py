# -*- coding: utf- -*-

import urllib2,urllib
import random

# url = r'http://jrtest.az00a.devstable.net/ecif/member/initializeMember.json'
# data ={
#     'usrid': '2088054635626814',
#     'resource': '0000000000000062'
# }
# full_url = url + urllib.urlencode(data)
ran = str(random.random())
url = r'http://www.hzti.com/government/CreateCheckCode.aspx?'+ran

try:
    print('url : ', url)
    req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36'})

    resp = urllib2.urlopen(req)
    print 'resp code is: ', resp.getcode()
    data = resp.read()
    print data
    fw = open(ran+'.png', 'wb')
    fw.write(data)
    fw.close()
except urllib2.URLError, e:
        print('reason : ', e.reason)
else:
    pass
finally:
    pass