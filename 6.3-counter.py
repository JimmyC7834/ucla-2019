#Given a string containing a bunch of words
#separated by spaces, e.g.
# s = "bear dog cat bear bear tree bush cat tree bear"
#
# print each unique word in that string once, followed by
# the number of times it appeared, sorted so that the most
# frequent words are printed first
#
# Using the example string s above, you should get:
#   bear 4
#   cat 2
#   tree 2
#   dog 1
#   bush 1

import collections

s = "bear dog cat bear bear tree bush cat tree bear"

c = collections.Counter()

for w in s.split(' '):
    c[w] += 1
print(c)
for k,v in sorted(c.items(), key=lambda item: item[1], reverse = True):
    print(k,v)