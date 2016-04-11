import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def find_answer(k, c, s):
  ''' Find the answer for this question '''
  logging.debug('k = %d, c = %d, s = %d' % (k, c, s))
  if c == 1:
    if s < k:
      return None
    elif k == 1:
      return [1]
    else:
      return range(1, k+1, 1)
  else:
    if s < k - 1:
      return None
    elif k == 1:
      return [1]
    elif s == k - 1:
      return range(2, k+1, 1)
    else: # s == k
      return range(1, k+1, 1)

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
    n = find_answer(*map(int, tc.split()))
    if n is None:
      print 'Case #{}: IMPOSSIBLE'.format(i+1)
    else:
      print 'Case #{}: {}'.format(i+1, ' '.join(map(str, n)))
    start_test += 1

if __name__ == '__main__':
  main()
