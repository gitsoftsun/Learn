# -*- coding: utf-8 -*-
__author__ = 'Lzy_pc'
# 抓取上海不限地区抓取50页就不再抓取
import urllib2
import time
from pyquery import PyQuery


class dianping:
    """
        点评数据抓取
    """
    page_index = 1
    def process_url(self, url):
        print "url %s starting" % url
        url_req = urllib2.Request(url)
        url_req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36')
        try:
            resp = urllib2.urlopen(url_req)
            print('this url %s response status code is : %d' % (url, resp.getcode()))
            html = resp.read()
            # call html_process method
            self.html_process(html)
            # judge hasNextPage
		
            next_url = self.hasNextPage(html)
            if next_url:
                time.sleep(1)
                self.process_url(next_url)
            else:
                return
        except urllib2.URLError, e:
            print(e.reason)
    print "process url end"

    def hasNextPage(self, html):
        """
        判断是否有下一页
	判断条件是： page_index == 49 终止
        :param html:
        :return: next_url / None
        """
	part_next_url = r'http://t.dianping.com/list/shanghai-category_1?pageIndex='
	#pq_obj = PyQuery(html)('.tg-paginator-next')
	#tag_a_len = len(pq_obj)
	#print 'length of tag : %d' % tag_a_len
	if page_index == 49:
          return False
	else:
	  next_url = part_next_url + str(page_index)
	  page_index += 1
	  return next_url

    def html_process(self, html):
        """
         抓取list页信息， 并持久化
        :return:
        """

    @classmethod
    def main(cls):
        pass

if __name__ == '__main__':
    # dianping.main()  # call static method
    target_url = r'http://t.dianping.com/list/shanghai-category_1'
    dp = dianping()
    dp.process_url(target_url)
