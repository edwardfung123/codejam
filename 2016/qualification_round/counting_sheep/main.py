import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def find_answer(n):
  ''' Find the answer for this question '''
  history = set()
  digits = set()
  all_digits = set(xrange(0, 10))
  cur_n = n
  while digits != all_digits:
    if cur_n in history:
      return 'INSOMNIA'
    logging.debug(cur_n)
    history.add(cur_n)
    digits |= set(map(int, str(cur_n)))
    logging.debug(history)
    logging.debug(digits)
    cur_n += n
  return cur_n - n

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    n_lines = 0
    n = int(lines[start_test])
    logging.debug(n)
    last_n = find_answer(n)
    print 'Case #{}: {}'.format(i+1, last_n)
    start_test += 1 + n_lines

if __name__ == '__main__':
  main()
