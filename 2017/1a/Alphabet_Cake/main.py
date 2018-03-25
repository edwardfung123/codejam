import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

max_x = 1
max_y = 1

def is_inside(x, y, w, h, tx, ty):
  if (x <= tx and tx <= (x + w) and 
      y <= ty and ty <= (y + h)):
    return True
  return False

class Kid(object):
  @classmethod
  def check_collide(cls, initial, x, y, w, h, kids):
    if x < 0 or y < 0:
      return True
    if x + w >= max_x:
      return True
    if y + h >= max_y:
      return True
    for kid in kids:
      if kid.initial == initial:
        continue
      # other kid
      if kid.is_inside_me(x, y):
        logging.debug('top-left inside')
        return True
      if kid.is_inside_me(x + w, y):
        logging.debug('top-right inside')
        return True
      if kid.is_inside_me(x, y + h):
        logging.debug('bottom-left inside')
        return True
      if kid.is_inside_me(x + w, y + h):
        logging.debug('bottom-right inside')
        return True
      if kid.w == 0 and kid.h == 0:
        if is_inside(x, y, w, h, kid.x, kid.y):
          return True
    return False

  def is_inside_me(self, x, y):
    if (self.x <= x and x <= (self.x + self.w) and 
        self.y <= y and y <= (self.y + self.h)):
      return True
    return False

  def __str__(self):
    return '<Kid {} {}, {}, {}, {}>'.format(
        self.initial, self.x, self.y, self.w, self.h)

  def __repr__(self):
    return self.__str__()

  def __init__(self, initial, y, x):
    self.initial = initial
    self.y = y
    self.x = x
    self.w = 0
    self.h = 0

  def expand_toward(self, kids, dx, dy):
    if dx == -1 and dy == -1:
      dx, dy, dw, dh = -1, -1, 1, 1
    elif dx == -1 and dy == 0:
      dx, dy, dw, dh = -1, 0, 1, 0
    elif dx == -1 and dy == 1:
      dx, dy, dw, dh = -1, 0, 1, 1
    elif dx == 0 and dy == -1:
      dx, dy, dw, dh = 0, -1, 0, 1
    elif dx == 0 and dy == 0:
      return
    elif dx == 0 and dy == 1:
      dx, dy, dw, dh = 0, 0, 0, 1
    elif dx == 1 and dy == -1:
      dx, dy, dw, dh = 0, -1, 0, 1
    elif dx == 1 and dy == 0:
      dx, dy, dw, dh = 0, 0, 1, 0
    elif dx == 1 and dy == 1:
      dx, dy, dw, dh = 0, 0, 1, 1

    logging.debug('Kid {} original at {}, {}, {}, {}'.format(
      self.initial, self.x, self.y, self.w, self.h))

    x = self.x + dx
    w = self.w + dw
    y = self.y + dy
    h = self.h + dh
    while True:
      logging.debug('Kid {} want to expand as {}, {}, {}, {}'.format(self.initial, x, y, w, h))
      if Kid.check_collide(self.initial, x, y, w, h, kids) is False:
        logging.debug('And it works!.')
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        x += dx
        y += dy
        w += dw
        h += dh
      else:
        break

  def expand_corners(self, kids):
    self.expand_toward(kids, -1, -1)  # top-left
    self.expand_toward(kids,  1, -1)  # top-right
    self.expand_toward(kids, -1, 1) # bottom-left
    self.expand_toward(kids,  1, 1) # bottom-right
    self.expand_toward(kids, -1, 0) # left
    self.expand_toward(kids, 1, 0) # right
    self.expand_toward(kids, 0, -1) # top
    self.expand_toward(kids, 0, 1) # bottom
    logging.debug('Kid {} is now as {}, {}, {}, {}'.format(
      self.initial, self.x, self.y, self.w, self.h))

def find_answer(lines, r, c):
  ''' Find the answer for this question '''
  global max_x
  max_x = c
  global max_y
  max_y = r
  kids = []
  grid = [list(l) for l in lines]
  for y in xrange(r):
    for x in xrange(c):
      if grid[y][x] != '?':
        # a kid
        kids.append(Kid(grid[y][x], y, x))
  logging.debug(kids)
  # expand to 4 corners
  for kid in kids:
    kid.expand_corners(kids)
  #kids[0].expand_corners(kids)
  fill_grid_with_kids(kids, grid)
  logging.debug(kids)
  return '\n'.join([''.join(l) for l in grid])

def fill_grid_with_kids(kids, grid):
  for k in kids:
    for y in xrange(k.y, k.y + k.h + 1):
      for x in xrange(k.x, k.x + k.w + 1):
        grid[y][x] = k.initial

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    r, c = map(int, lines[start_test].split(' '))
    tc = lines[start_test+1:start_test+1+r]
    logging.debug(tc)
    n = find_answer(tc, r, c)
    print 'Case #{}:\n{}'.format(i+1, n)
    start_test += 1 + r

if __name__ == '__main__':
  main()
