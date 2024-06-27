from itertools import groupby
word = "aaabbbcccaabbbbb"
for key, group in groupby(word):
    print(key, list(group))

from itertools import groupby
a_list = [("Animal", "cat"),
          ("Animal", "dog"),
          ("Bird", "peacock"),
          ("Bird", "pigeon")]
an_iterator = groupby(a_list, lambda x : x[0])
for key, group in an_iterator:
    key_and_group = {key : list(group)}
    print(key_and_group)