import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def find_answer(line):
  ''' Find the answer for this question '''
  target = line[0]
  count = 0
  for c in line:
    if c == target:
      continue
    else:
      count += 1
      target = c
  logging.debug(count)
  return count if line[-1] == '+' else count + 1

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    n_lines = 0
    tc = lines[start_test]
    logging.debug(tc)
    n = find_answer(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += 1 + n_lines

if __name__ == '__main__':
  main()
