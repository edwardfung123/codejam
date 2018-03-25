import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

lines = list(fileinput.input())
n_tc = int(lines.pop(0))

tcs = []
for i in xrange(n_tc):
  n, numbers = int(lines.pop(0), 10), map(int, lines.pop(0).split())
  tcs.append((n, numbers))

def solve(n, numbers):
  numbers.sort()
  logging.debug(numbers)
  seq = numbers[::2] + list(reversed(numbers[1::2]))
  logging.debug(seq)
  if n % 2 == 0:
    lvl = range(n/2)
    lvl += list(reversed(lvl))
  else:
    lvl = range(n/2 + 1)
    lvl += list(reversed(xrange(n/2)))
  logging.debug(lvl)
  ret = sum(map(lambda (x, y): (x-y)*(x-y), zip(seq, lvl)))
  return ret

for i, args in enumerate(tcs):
  print 'Case #{}: {}'.format(i+1, solve(*args))
