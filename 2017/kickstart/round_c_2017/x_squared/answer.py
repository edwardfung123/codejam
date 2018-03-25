def transpose(grid):
  size = len(grid)
  g = []
  for x in xrange(size):
    r = [grid[y][x] for y in xrange(size)]
    g.append(r)
  #import pprint
  #pprint.pprint(grid)
  #pprint.pprint(g)
  return g


def count_row(row):
  s = reduce(lambda acc, c: acc + 1 if c == 'X' else acc, row, 0)
  return s


def count_rows(grid):
  size = len(grid)
  return [count_row(row) for row in grid]


def count(grid):
  size = len(grid)
  row_counts = count_rows(grid)
  for c in row_counts:
    if c > 2:
      return 'IMPOSSIBLE'

  row_strings = []
  for row in grid:
    if isinstance(row, basestring):
      row_strings.append(row)
    elif isinstance(row, (tuple, list)):
      row_strings.append(''.join(row))
    else:
      raise TypeError()
  from collections import Counter
  row_pattern_counts = Counter(row_strings)
  if len(filter(lambda x: x == 1, row_pattern_counts.values())) > 1:
    return 'IMPOSSIBLE'
  
  #for r, count in enumerate(row_counts):
  #  if count == 1:
  #    for c, cell in enumerate(grid[r]):
  #      if cell == 'X':
  #        col = [grid[i][c] for i in xrange(size)]
  #        s = reduce(lambda acc, i: acc + 1 if i == 'X' else acc, col, 0)
  #        if s != 1:
  #          return 'IMPOSSIBLE'
  return 'POSSIBLE'


def answer(grid):
  if count(grid) == 'IMPOSSIBLE' or count(transpose(grid)) == 'IMPOSSIBLE':
    return 'IMPOSSIBLE'
  return 'POSSIBLE'


def swap_row(grid, r0, r1):
  grid = [list(r) for r in grid]
  for x in xrange(len(grid)):
    grid[r0][x], grid[r1][x] = grid[r1][x], grid[r0][x]
  return grid


def swap_col(grid, c0, c1):
  grid = [list(r) for r in grid]
  for y in xrange(len(grid)):
    grid[y][c0], grid[y][c1] = grid[y][c1], grid[y][c0]
  return grid


if __name__ == '__main__':
  import logging
  import pprint
  logging.basicConfig(level=logging.DEBUG)

  g = [
      'X.....X',
      '.X...X.',
      '..X.X..',
      '...X...',
      '..X.X..',
      '.X...X.',
      'X.....X']
  ra = range(len(g))
  import random
  for c in xrange(50):
    op = random.choice([swap_col, swap_row])
    x, y = random.sample(ra, 2)
    logging.debug('{} {} {}'.format(op, x, y))
    g = op(g, x, y)
    for r in g:
      print '{}  :  {}'.format(r, count_row(r))
    print '=' * 80


  cases = [
      (['..X', 'XX.', 'XX.'], 'POSSIBLE'),
      (['...', 'XXX', 'XX.'], 'IMPOSSIBLE'),
      ]

  for i, tc in enumerate(cases):
    try:
      expected = tc[-1]
      args = tc[:-1]
      assert answer(*args) == expected
      logging.debug('Case {}: Passed'.format(i+1))
    except AssertionError:
      logging.debug('Case {}: Failed'.format(i+1))
