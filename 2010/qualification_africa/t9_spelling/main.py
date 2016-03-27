import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

mapping = {
  'a': '2', 'b': '22', 'c': '222',
  'd': '3', 'e': '33', 'f': '333',
  'g': '4', 'h': '44', 'i': '444',
  'j': '5', 'k': '55', 'l': '555',
  'm': '6', 'n': '66', 'o': '666',
  'p': '7', 'q': '77', 'r': '777', 's': '7777',
  't': '8', 'u': '88', 'v': '888',
  'w': '9', 'x': '99', 'y': '999', 'z': '9999',
  ' ': '0'
}

prev = None
def translate(c):
  global prev
  c_ = mapping[c]
  if prev == mapping[c][0]:
    return ' ' + mapping[c]
  else:
    prev = mapping[c][0]
    return mapping[c]

def find_answer(line):
  ''' Find the answer for this question '''
  return ''.join(map(translate, line))

def main():
  ''' Parse the input lines '''
  lines = [l.replace('\n', '') for l in fileinput.input()]
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
