import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def is_tidy(n):
  for i in xrange(0, len(n) - 1):
    if n[i] > n[i+1]:
      return False
  return True

def tidy_up(n):
  for i in xrange(len(n) - 1, 0, -1):
    current_digit = n[i-1]
    last_digit = n[i]
    logging.debug('cur = {}   last = {}'.format(current_digit, last_digit))
    if current_digit > last_digit:
      current_digit -= 1
      for j in xrange(i, len(n)):
        n[j] = 9
      n[i-1] = current_digit
      logging.debug('{}'.format(n))
      # if current_digit == -1:
  while n[0] == 0:
    n.pop(0)
  return ''.join(map(str, n))

def find_answer(line):
  ''' Find the answer for this question '''
  n = map(int, line)
  if is_tidy(n):
    return line
  else:
    logging.debug('Tidying up the number.')
    return tidy_up(n)

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
    n = find_answer(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += 1

if __name__ == '__main__':
  main()
