import fileinput
import math


from collections import Counter

class Cached(object):
  def __init__(self):
    self.cache = {}
    self.stats = Counter()

  def __call__(self, fn):
    def wrapped(*args):
      self.stats[args] += 1
      if args not in self.cache:
        self.cache[args] = fn(*args)
      return self.cache[args]

    setattr(wrapped, 'stats', self.stats)
    return wrapped


@Cached()
def nCr(n,r):
  f = math.factorial
  return f(n) / f(r) / f(n-r)


def solve2(n, m):
  l = [1] * n + [0] * m
  from itertools import permutations
  stats = [0, 0]
  visited = set()
  for p in permutations(l):
    if p not in visited:
      visited.add(p)
      s = [0, 0]
      for x in p:
        s[x] += 1
        if s[0] >= s[1]:
          stats[0] += 1
          print str(p) + ' is fail.'
          break
      else:
        stats[1] += 1
        print str(p) + ' is OK.'
  return stats[1] / float(stats[0] + stats[1])


@Cached()
def fail(n, m):
  if m == 0:
    return 0

  failed_cases = 0
  
  # first prefixed with 0
  failed_cases += nCr(n+m-1, n)

  # then 10, 1100, 111000
  for m_ in xrange(1, m+1, 1):
    if m_ > 2:
      failed_cases += win(m_, m_ - 2) * nCr(n+m-2*m_, n-m_)
    else:
      failed_cases += nCr(n+m-2*m_, n-m_)

  return failed_cases


@Cached()
def win(n, m):
  total_cases = nCr(n+m, n)
  return total_cases - fail(n, m)


def solve(n, m):
  total_cases = nCr(n+m, n)
  failed_cases = fail(n, m)
  
  from fractions import Fraction
  f = Fraction(total_cases - failed_cases, total_cases)
  f.limit_denominator()
  return float(f)

lines = list(fileinput.input())
lines.pop(0)
for i, l in enumerate(lines):
  n, m = map(int, l.split())
  #print 'Case' + str((n, m))
  #s1, s2 = solve(n, m), solve2(n, m)
  #if s1 != s2:
  #  print "Case #{}: {:.8f} vs {:.8f}".format(i+1, s1, s2)
  s1 = solve(n, m)
  print "Case #{}: {:.8f}".format(i+1, s1)

#print getattr(nCr, 'stats')
#print getattr(fail, 'stats')
#print getattr(win, 'stats')
