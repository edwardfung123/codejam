import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def find_answer(s):
  #logging.debug(s)
  #logging.debug(s[1:])
  result = s[0]
  for c in s[1:]:
    #logging.debug(c)
    if c < result[0]:
      result = result + c
    else:
      result = c + result
  return result

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
