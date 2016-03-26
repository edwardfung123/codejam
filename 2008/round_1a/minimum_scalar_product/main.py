import fileinput
import logging
#logging.basicConfig(level=logging.DEBUG)

def find_answer(v1, v2):
  ''' Find the answer for this question '''
  v1_minmax = sorted(v1)
  v2_maxmin = sorted(v2, reverse=True)
  return reduce(lambda x, t: x + t[0] * t[1], zip(v1_minmax, v2_maxmin), 0)

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    size = int(lines[start_test])
    v1 = map(int, lines[start_test+1].split())
    v2 = map(int, lines[start_test+2].split())
    logging.debug(v1)
    logging.debug(v2)
    n = find_answer(v1, v2)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += 1 + 2

if __name__ == '__main__':
  main()
