#!/usr/bin/python

print "Content-Type: text/plain;charset=utf-8"
print

import urllib
from xml.etree.ElementTree import fromstring, dump

data = urllib.urlopen("http://www.goodreads.com/review/list/5380877.xml?key=TdsodGqnEh1lPXWEv7Z6HA&shelf=currently-reading").read();

tree = fromstring(data)
books = tree.findall('books/book')

for b in books:
    print "<div class='book'><table><tr><td>&ndash;&nbsp;</td><td><a class='title' href='%s'>%s</a><br/>&nbsp;by <a class='author' href='%s'>%s</a><a href='http://www.amazon.com/dp/%s/?tag=spencero-20'></a></td></tr></table></div>" % ( 
        b.find('link').text,
        b.find('title').text,
        b.find('authors/author/link').text,
        b.find('authors/author/name').text,
        b.find('isbn').text
        )


#        print "<div class='book'><a class='title' href='%s'>%s</a><br/>&nbsp;by <a class='author' href='%s'>%s</a><a href='http://www.amazon.com/dp/%s/?tag=spencero-20'><img class='icon' width=16 height=16 src='/img/amazon_icon.png'/></a></div>" % (
