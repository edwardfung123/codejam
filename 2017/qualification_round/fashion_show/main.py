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

def check_row(row, n):
  '''Empty row is OK. If no '+' in any pair of model. it failed.'''
  models = [m for m in row if m != '.']
  if len(models) <= 1:
    return True
  else:
    from itertools import combinations
    comb = combinations(models, 2)
    for m1, m2 in comb:
      if m1 != '+' and m2 != '+':
        return False
    return True

def check_diagonal(line):
  models = [m for m in line if m != '.']
  if len(models) <= 1:
    return True
  else:
    from itertools import combinations
    comb = combinations(models, 2)
    for m1, m2 in comb:
      if m1 != 'x' and m2 != 'x':
        return False
    return True

def check_grid(grid, n):
  logging.debug('checking row')
  for r in grid:
    if check_row(r, n) is False:
      logging.debug('Failed in checking row {}'.format(r))
      return False
  logging.debug('checking col')
  r_grid = rotate_grid(grid, n)
  for r in r_grid:
    if check_row(r, n) is False:
      logging.debug('Failed in checking col {}'.format(r))
      return False
  logging.debug('checking digonal')
  for d in get_diagonal(grid, n):
    if check_diagonal(d) is False:
      logging.debug('Failed in checking diagonal {}'.format(d))
      return False
  return True

def get_diagonal(grid, n):
  # the +1, +1 direction
  start_points = [(i, 0) for i in xrange(n)] + [(0, i) for i in xrange(1, n)]
  for pt in start_points:
    y = pt[1]
    x = pt[0]
    line = []
    for i in xrange(n):
      if y + i < n and x + i < n:
        line.append(grid[y+i][x+i])
    logging.debug(line)
    yield line
  logging.debug('change direction')
  start_points = [(i, 0) for i in xrange(n)] + [(n-1, i) for i in xrange(1, n)]
  for pt in start_points:
    y = pt[1]
    x = pt[0]
    line = []
    for i in xrange(n):
      if y + i < n and x - i >= 0:
        line.append(grid[y+i][x-i])
    logging.debug(line)
    yield line

def eval_grid(grid):
  from collections import Counter
  c = Counter()
  for row in grid:
    c += Counter(row)
  return 1 * c['+'] + 1 * c['x'] + 2 * c['o']

def rotate_grid(grid, n):
  logging.debug(grid)
  new_grid = []
  for x in xrange(n):
    new_row = [grid[y][x] for y in xrange(n)]
    new_grid.append(new_row)
  return new_grid

if __name__ == '__main__':
  main()
