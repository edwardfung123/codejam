import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def find_answer(credit, prices):
  ''' Find the answer for this question '''
  indices = xrange(0, len(prices))
  import itertools
  combinations = itertools.combinations(indices, 2)
  for c in combinations:
    if prices[c[0]] + prices[c[1]] == credit:
      return c
  return 0

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    credit = int(lines[start_test])
    list_length = int(lines[start_test+1])
    prices = map(int, lines[start_test+2].split())
    n = find_answer(credit, prices)
    print 'Case #{}: {} {}'.format(i+1, n[0]+1, n[1]+1)
    start_test += 3

if __name__ == '__main__':
  main()
