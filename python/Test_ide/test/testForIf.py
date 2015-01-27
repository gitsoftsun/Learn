__author__ = 'lzy'
# Error : http://www.oschina.net/code/snippet_581482_20892
values = [1, 2, 3]
for var in values:
    if var == 2:
        print 'I am :', var
        values.remove(var)
    print var