import os, sys
import logging
import fileinput

logging.basicConfig(level=logging.DEBUG)

lineno = 0
state = 'init'
num_test_cases = 0
done = 0
n = 0
a, b = 0, 0
guess = 0

def make_guess(a, b):
  ''' The guess must be in (a, b]'''
  g = 0
  if (b - a) == 1:
    logging.debug('only one choice')
    logging.debug(type(b))
    print '{}'.format(b)
    sys.stdout.flush()
    return b
  #  g = b
  #else:
  g = (a + b) / 2
  #g = b if b - a == 1 else (a + b) / 2
  logging.debug('Given a, b = {}, guessing {}'.format((a, b), g))
  print str(g)
  sys.stdout.flush()
  return g

if __name__ == '__main__':
  for l in fileinput.input():
    l = l.strip()
    logging.debug(state)
    if state == 'init':
      num_test_cases = int(l)
      state = 'read_ab'
    elif state == 'read_ab':
      a, b = map(int, l.split())
      logging.debug('a, b = {}'.format((a, b)))
      state = 'read_n'
    elif state == 'read_n':
      n = int(l)
      state = 'make_guess'
      logging.debug('n = {}'.format(n))
      # make the first guess here
      guess = make_guess(a, b)
    elif state == 'make_guess':
      # get the last guess result and make another guess
      logging.debug('In guess state, got {}'.format(l))
      if l == 'WRONG_ANSWER':
        raise ValueError(l)
      elif l == 'CORRECT':
        done += 1
        if done == num_test_cases:
          sys.exit(0)
        state = 'read_ab'
        continue
      elif l == 'TOO_SMALL':
        a = guess
      elif l == 'TOO_BIG':
        b = guess - 1
      else:
        raise ValueError(l)

      # make another guess
      guess = make_guess(a, b)
          
    # end of loop
    lineno += 1
