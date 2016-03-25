import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def find_answer(lines):
  ''' Find the answer for this question '''
  return 0

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    n_lines = int(lines[start_test])
    tc = lines[start_test+1:start_test+1+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += 1 + n_lines

if __name__ == '__main__':
  main()
