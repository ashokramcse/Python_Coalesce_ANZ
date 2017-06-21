'''
Created on 21-Jun-2017

@author: BALASUBRAMANIAM
'''
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

import os
import zipfile

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print ('zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname))
            zf.write(absname, arcname)
    zf.close()

zip("G:/NIIT-TECH", "g:/niitzip")





from collections import deque
d = deque()
d.append(1)
print (d)
deque([1])
d.appendleft(2)
print (d)
deque([2, 1])
d.clear()
print (d)
deque([])
d.extend('1')
print (d)
deque(['1'])
d.extendleft('234')
print (d)
deque(['4', '3', '2', '1'])
d.count('1')
1


