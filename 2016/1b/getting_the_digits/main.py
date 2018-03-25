import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

from collections import Counter
from itertools import product

digits = {
    0: 'ZERO',
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE',
}

digit_counters = {k: Counter(v) for k, v in digits.iteritems()}

def find_answer(s):
    c = Counter(s)
    logging.debug(c)
    ret = []
    for digit, counter in digit_counters.iteritems():
        isAllChar = True
        for char, count in counter.iteritems():
            if char not in c or c[char] < count:
                isAllChar = False
                break
        if isAllChar:
            logging.debug(digit)
            # check how many this digit in s
            possible_n = min([c[char]/count for char, count in counter.iteritems()])
            #possible_n = min([int(round(c[char]/float(count))) for char, count in counter.iteritems()])
            n = max(1, possible_n)
            logging.debug(n)
            ret.append(str(digit) * n)
            d = {char: count * n for char, count in counter.iteritems()}
            c.subtract(d)
            logging.debug(c)
            logging.debug('----')
    return ''.join(ret)
    
def haveDigit(c, counter):
  for char, count in counter.iteritems():
    if char not in c or c[char] < count:
      return False
  return True

def find_answer2(s):
    c = Counter(s)
    logging.debug(c)
    ret = []
    for digit, counter in digit_counters.iteritems():
      while haveDigit(c, counter):
        logging.debug(digit)
        ret.append(str(digit))
        c -= counter
        logging.debug(c)
    return ''.join(ret)

def haveDigit(c, counter):
  for char, count in counter.iteritems():
    if char not in c or c[char] < count:
      return False
  return True

def getCount(c, counter):
  possible_n = min([c[char]/count for char, count in counter.iteritems()])
  n = max(1, possible_n)
  return n

def find_answer3(s):
  c = Counter(s)
  # pp(c)
  ret = []
  possible_digit_and_count = [(digit, getCount(c, counter)) for digit, counter in digit_counters.iteritems() if haveDigit(c, counter)]
  logging.debug(possible_digit_and_count)
  ret = [str(d) for d,count in possible_digit_and_count]
  answer = ''.join(ret)
  ss = ''.join([digits[d] for d,count in possible_digit_and_count])
  c -= Counter(ss)
  logging.debug(c)
  return answer

def allZeroes(counter):
  for k, v in counter.iteritems():
    if v != 0:
      return False
  return True

def find_answer4(s):
  c = Counter(s)
  # pp(c)
  ret = []
  possible_digit_and_count = [(digit, range(getCount(c, counter), -1, -1)) for digit, counter in digit_counters.iteritems() if haveDigit(c, counter)]
  logging.debug(possible_digit_and_count)
  all_ranges = [r for digit, r, in possible_digit_and_count]
  pr = product(*all_ranges)
  for p in pr:
    digits_str = [str(possible_digit_and_count[i][0]) * count for i, count in enumerate(p) if count > 0]
    ss = ''.join([digits[possible_digit_and_count[i][0]] * count for i, count in enumerate(p) if count > 0])
    logging.debug(ss)
    counter_ss = Counter(ss)
    counter_ss.subtract(c)
    logging.debug(counter_ss)
    if allZeroes(counter_ss):
      ret = digits_str
      return ''.join(ret)
      logging.debug('----')
    return ret

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
    n = find_answer4(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += 1

if __name__ == '__main__':
  main()
