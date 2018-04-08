import logging
logging.basicConfig(level=logging.DEBUG)
import fileinput

lines = list(fileinput.input())

n = int(lines.pop(0))
PARTIES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in xrange(n):
  steps = []
  n_parties = int(lines.pop(0))
  p = PARTIES[0:n]
  tmp = map(int, lines.pop(0).split())
  from collections import Counter
  c = Counter(dict(zip(p, tmp)))
  logging.debug(c)
  total = sum(c.values())
  while len(c) > 0:
    # after_removal, the counter should not be 1 person only.
    if total == 3:
      # remove one only
      kinds = len(c.keys())
      if kinds == 3:
        # remove anyone then the remaining two
        one = c.popitem()[0]
        steps.append(one)
        steps.append(''.join(c.keys()))
      elif kinds == 2:
        # remove one from the more and then remove both
        most_common = c.most_common(1)
        steps.append(most_common[0])
        c.pop(most_common[0])
        steps.append(''.join(c.keys()))
      else:
        raise ValueError('remaing 3 but only one kind... This ALGO sucks.')
      c.clear()
    elif total == 2:
      steps.append(''.join(c.keys()))
      c.clear()
    else:
      # try to remove 2
      most_common = c.most_common(2)
      logging.debug(most_common)
      # try removing the most common party first
      diff = most_common[0][1] - most_common[1][1]
      if diff > 0:
        div = diff / 2
        mod = diff % 2
        steps.extend([most_common[0][0] + most_common[0][0]] * div)
        if mod == 1:
          steps.append(most_common[0][0])
        c.subtract({most_common[0][0] : diff})
        total -= diff
      else:
        logging.debug('Remove one from the highest 2.')
        steps.append(most_common[0][0] + most_common[1][0])
        c.subtract({most_common[0][0]:1, most_common[1][0]:1})
        total -= 2
  print 'Case #{}: {}'.format(i+1, ' '.join(steps))
