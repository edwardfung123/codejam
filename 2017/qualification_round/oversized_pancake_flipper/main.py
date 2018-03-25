import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

def parse(line):
  pancakes, k = line.split(' ')
  return list(pancakes), int(k)

def find_answer(pancakes, k):
  ''' Find the answer for this question '''
  flips = 0
  for i in xrange(len(pancakes)):
    current_pancake = pancakes[i]
    if current_pancake == '+':
      # it is a happy face, no need to flip
      pass
    else:
      # flip k pancakes. raise exception if does not have enough room.
      logging.debug('the {} pancake is "-". flip it'.format(i))
      if i + k > len(pancakes):
        raise ValueError('not enough room')
      else:
        for j in xrange(i, i + k):
          pancakes[j] = '-' if pancakes[j] == '+' else '+'
        flips += 1
        logging.debug('flipped to: {}'.format(pancakes))
  return flips

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    pancakes, k = parse(lines[start_test])
    logging.debug(pancakes)
    logging.debug(k)
    try:
      n = find_answer(pancakes, k)
      print 'Case #{}: {}'.format(i+1, n)
    except:
      print 'Case #{}: IMPOSSIBLE'.format(i+1)
    start_test += 1

if __name__ == '__main__':
  main()
