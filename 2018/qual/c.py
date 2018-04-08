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
finished = 0
rows = None
cols = None
prepared = None
corners = None
offset = None

unfinished_3x3_grids = None

def make_move(a, prepared):
  # from the prepared, find the next col to be filled.
  import random
  global unfinished_3x3_grids
  x = random.sample(unfinished_3x3_grids, 1)[0]
  p = offset[0] + x, offset[1] + 1
  s = '{} {}'.format(p[1], p[0])
  print s
  sys.stdout.flush()
  logging.debug(s)
  return p


def debug_prepared(prepared):
  for row in prepared:
    logging.debug(''.join(row))


def mark_prepared(prepared, y, x):
  x_, y_ = x - offset[0], y - offset[1]
  try:
    prepared[y_][x_] = 'x'
  except IndexError as e:
    logging.exception(e)
    logging.error('x, y = {}, {}'.format(x, y))
    sys.exit(-1)
  debug_prepared(prepared)
  next_unfinished = []
  global unfinished_3x3_grids

  for x in unfinished_3x3_grids:
    for y in xrange(3):
      if prepared[y][x-1] == '.' or prepared[y][x] == '.' or prepared[y][x+1] == '.':
        next_unfinished.append(x)
        break
  unfinished_3x3_grids = next_unfinished
  logging.debug(unfinished_3x3_grids)


if __name__ == '__main__':
  for l in fileinput.input():
    l = l.strip()
    logging.debug(state)
    if state == 'init':
      num_test_cases = int(l)
      state = 'read_a'
    elif state == 'read_a':
      a = int(l)
      logging.debug('a = {}'.format(a))
      state = 'make_move'
      # initialize
      # from the question statement, a = 20 or a = 200
      from math import ceil
      rows = 3
      cols = int(ceil(a / 3.0))
      corners = (0, 0), (0, cols-1), (rows-1, 0), (rows, cols-1)
      offset = (1, 1)
      prepared = []
      for _ in xrange(rows):
        prepared.append(['.'] * cols)
      debug_prepared(prepared)
      unfinished_3x3_grids = range(1, cols-1, 1)
      logging.debug(unfinished_3x3_grids)
      # it would be
      # make the first move here
      last_move = make_move(a, prepared)
    elif state == 'make_move':
      i_, j_ = map(int, l.split())
      state = 'make_move'
      logging.debug("i', j' = {}, {}".format(i_, j_))
      if i_ == -1 or j_ == -1:
        # we did sth wrong
        sys.exit(-1)

      if i_ == 0 and j_ == 0:
        # we finish this test_case
        finished += 1
        if finished == num_test_cases:
          sys.exit(0)
        
        state = 'read_a'
        continue

      # not done yet.
      mark_prepared(prepared, i_, j_)
      # make the first guess here
      last_move = make_move(a, prepared)
          
    # end of loop
    lineno += 1
