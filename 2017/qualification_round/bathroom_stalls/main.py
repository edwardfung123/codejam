import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

class lr(object):
  i = 0
  l = None
  r = None
  def __init__(self, i, l, r):
    self.i = i
    self.l = l
    self.r = r

  @property
  def min(self):
    return min(self.l, self.r)

  @property
  def max(self):
    return max(self.l, self.r)

  def is_free(self):
    return self.l != None

  def __str__(self):
    return '{} ({}, {})'.format(self.i, self.l, self.r)

  def __repr__(self):
    return self.__str__()

def find_lrs_from_config(stalls_config):
  lrs = []
  for i in xrange(1, len(stalls_config) - 1):
    if stalls_config[i] == 'o':
      lrs.append(lr(i=i, l=None, r=None))
      continue
    l = 1
    r = 1
    while (i - l) >= 0 and stalls_config[i - l] == '.':
      l += 1
    while i + r < len(stalls_config) and stalls_config[i + r] == '.':
      r += 1
    logging.debug('i = {}   l = {}   r = {}'.format(i, l, r))
    lrs.append(lr(i=i, l=l - 1, r=r - 1))
  return lrs

def find_answer1(line):
  ''' Find the answer for this question '''
  n, k = map(int,line.split(' '))
  stalls_config = list('o' + '.' * n + 'o')
  for ppl in xrange(0, k):
    logging.debug(stalls_config)
    lrs = find_lrs_from_config(stalls_config)
    logging.debug(lrs)
    min_lrs_list = [lr.min for lr in lrs if lr.is_free()]
    max_min_lrs = max(min_lrs_list)
    logging.debug('min_lrs_list = {}    max_min_lrs = {}'.format(min_lrs_list, max_min_lrs))
    stalls_with_min_lrs = [lr for i, lr in enumerate(lrs) if lr.min == max_min_lrs]
    if len(stalls_with_min_lrs) == 1:
      # If there is only one such stall, they choose it
      choice = stalls_with_min_lrs[0].i
    else:
      # otherwise, they choose the one among those where max(LS, RS) is maximal.
      max_lrs_list = [lr.max for lr in stalls_with_min_lrs]
      max_max_lrs = max(max_lrs_list)
      logging.debug('max_lrs_list = {}    max_max_lrs = {}'.format(max_lrs_list, max_max_lrs))
      stalls_with_max_lrs = [lr for i, lr in enumerate(stalls_with_min_lrs) if lr.max == max_max_lrs]
      choice = stalls_with_max_lrs[0].i
    logging.debug(choice) 
    # mark the stalls is chosen
    stalls_config[choice] = 'o'
  logging.debug(stalls_config)
  return 0, 0

class Config(object):
  length = 0
  def __init__(self, l):
    self.length = l

  def split(self):
    l = self.length / 2 
    c1 = self.__class__(l - 1 if self.length % 2 == 0 else l)
    c2 = self.__class__(l)
    return [c1, c2]

  def __str__(self):
    return '<Config length={}>'.format(self.length)

  def __repr__(self):
    return self.__str__()

def find_answer2(line):
  n, k = map(int,line.split(' '))
  configs = [Config(n)]
  for ppl in xrange(k):
    max_length = max([c.length for c in configs])
    for i, config in enumerate(configs):
      if config.length == max_length:
        new_configs = config.split()
        if len(configs) == 1:
          configs = new_configs
        else:
          configs = configs[:i] + new_configs + configs[i+1:]
        break
    logging.debug(configs)
  return 0, 0

cached_configs = {}

from functools import total_ordering

@total_ordering
class Pattern(object):
  max = 0
  min = 0
  def __init__(self, max, min):
    self.max = max
    self.min = min

  def __lt__(self, other):
    return (self.max, self.min) < (other.max, other.min)

  def __eq__(self, other):
    return (self.max, self.min) == (other.max, other.min)

  def __str__(self):
    return '({}, {})'.format(self.max, self.min)

  def __repr__(self):
    return self.__str__()

  def __hash__(self):
    return hash(repr(self))

from collections import OrderedDict

class Config2(object):
  def __init__(self, n):
    self.configs = OrderedDict()
    self.n = n
    if n == 1:
      self.configs[Pattern(0, 0)] = 1
      self.sorted_configs = [(Pattern(0, 0), 1)]
    elif n == 2:
      self.configs[Pattern(1, 0)] = 1
      self.configs[Pattern(0, 0)] = 1
    else:
      max_lr = n / 2
      min_lr = max_lr - 1 if n % 2 == 0  else max_lr
      self.configs[Pattern(max_lr, min_lr)] = 1
      if min_lr == 0:
        self.combine(max_lr)
      else:
        self.combine(max_lr, min_lr)

  def combine(self, *args):
    logging.debug('combine')
    tmp_configs = {}
    for n in args:
      if n not in cached_configs:
        config = self.__class__(n)
        cached_configs[n] = config
      config = cached_configs[n]
      #logging.debug('configs of {}'.format(n))
      #logging.debug(config.configs)
      for t, count in config.configs.iteritems():
        if t in tmp_configs:
          tmp_configs[t] += count
        else:
          tmp_configs[t] = count
      #logging.debug('tmp = {}'.format(tmp_configs))
    def fn(t):
      p, c = t
      #logging.debug(p)
      #logging.debug(c)
      return p
    sorted_configs = sorted(list(tmp_configs.viewitems()), key=fn, reverse=True)
    for p, c in sorted_configs:
      self.configs[p] = c
    #logging.debug(self.configs)

  def find_lr(self, k):
    i = 0
    n = self.n
    for p, counter in self.configs.iteritems():
      if i + counter >= k:
        return p
      else:
        i += counter
    return 0, 0

  def get_key(self, n):
    max_lr = n / 2
    min_lr = max_lr - 1 if n % 2 == 0  else max_lr
    return Pattern(max_lr, min_lr)

  @classmethod
  def get_config(cls, n):
    if n not in cached_configs:
      cached_configs[n] = cls(n)
    return cached_configs[n]

cached_configs[1] = Config2(1)
cached_configs[2] = Config2(2)
cached_configs[3] = Config2(3)

def find_answer(line):
  n, k = map(int,line.split(' '))
  lr = Config2.get_config(n).find_lr(k)
  return lr

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    tc = lines[start_test]
    logging.debug(tc)
    p = find_answer(tc)
    print 'Case #{}: {} {}'.format(i+1, p.max, p.min)
    start_test += 1

if __name__ == '__main__':
  main()
