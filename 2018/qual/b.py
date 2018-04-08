import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)


def trouble_sort(numbers):
  clone = list(numbers)
  done = False
  while not done:
    done = True
    for i in xrange(len(clone) - 2):
      if clone[i] > clone[i+2]:
        logging.debug('swap')
        done = False
        clone[i], clone[i+2] = clone[i+2], clone[i]
  return clone


def solve(numbers):
  ret = trouble_sort(numbers)
  logging.debug(ret)
  ret2 = sorted(numbers)

  from itertools import izip
  for i, (a, b) in enumerate(izip(ret, ret2)):
    if a != b:
      return i
  return 'OK'


lines = list(fileinput.input())

n_tc = int(lines.pop(0))

for i in xrange(n_tc):
  n_int = lines[2*i]
  numbers = map(int, lines[2*i+1].strip().split())
  if i + 1 > n_tc:
    break
  ret = solve(numbers)
  print 'Case #{}: {}'.format(i+1, ret)
