"""
ignore . ! '

N: length of document
split by space O(N)
iterate  O(N)
  if there is a punctuation, remove it
  lower the case

count and sort and convert the count from int to string O(NlogN) -> O(WlogW)
W: length of word

cnt = Counter()
sorted(cnt, lambda: )

word: (cnt, position)
"""
from collections import Counter
def word_count_engine(document):
  cnt = {}
  for i, w in enumerate(document.split()):
    w = ''.join([c for c in w if c.isalpha()])
    w = w.lower()
    if w not in cnt:
      cnt[w] = [1, i]
    else:
      cnt[w][0] += 1 # add count

  res = []
  for w, (count, _) in sorted(cnt.items(), key=lambda x: (-x[1][0], x[1][1])):
    res.append([w, str(count)])
  return res
