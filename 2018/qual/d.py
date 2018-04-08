import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

from itertools import imap
import operator


def area(p):
  return 0.5 * abs(sum(x0*y1 - x1*y0
                                 for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
  return zip(p, p[1:] + [p[0]])


def convex_hull(points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]


def matrix_debug(name, m):
  return
  logging.debug('matrix {}:'.format(name))
  for row in m:
    logging.debug(row)
  logging.debug('------------------')

def dotproduct(vec1, vec2, sum=sum, imap=imap, mul=operator.mul):
  return sum(imap(mul, vec1, vec2))


def get_col(m, col):
  for y in xrange(len(m)):
    yield m[y][col]
  raise StopIteration()

def matrix_mul(m1, m2):
  m1_height = len(m1)
  m1_width = len(m1[0])
  m2_height = len(m2)
  m2_width = len(m2[0])
  assert m1_width == m2_height
  ret = []
  for y in xrange(m1_height):
    row = m1[y]
    row_ret = []
    for x in xrange(m2_width):
      col = get_col(m2, x)
      s = dotproduct(row, col)
      row_ret.append(s)
    ret.append(row_ret)
  return ret


def angle_range(start, end, steps):
  from math import cos, sin, pi, atan2, hypot
  if end == start:
    yield pi * start / 180.0
  else:
    for i in xrange(steps + 1):
      yield pi * (start + (end - start) * i / float(steps)) / 180.0

def solve(target_a):
  from math import cos, sin, pi, atan2, hypot
  steps = 10
  tmp = []
  theta_x = 0.0
  min_angle, max_angle = 40, 50
  for theta_x in angle_range(0, 0, 1):
    for theta_y in angle_range(30, 60, 10):
      for theta_z in angle_range(54.73250000, 54.73750000, 40):
        a = rotate_cube_area(theta_x, theta_y, theta_z)
        tmp.append((theta_x, theta_y, theta_z, a))
  for theta_x, theta_y, theta_z, a in tmp:
    if a > 1.732050:
      logging.debug('{}, {}, {:.8f}: {}'.format(
        180 * theta_x / pi,
        180 * theta_y / pi,
        180 * theta_z / pi,
        a))

def rotate_cube_area(theta_x, theta_y, theta_z):
  from math import cos, sin, pi, atan2, hypot
  # each corner is a col vector.
  corners = [
        [-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5],
        [-0.5, -0.5, -0.5, -0.5,  0.5,  0.5,  0.5,  0.5],
        [-0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5],
      ]

  r_x = [
      [1.0, 0.0, 0.0],
      [0.0, cos(theta_x), -sin(theta_x)],
      [0.0, sin(theta_x),  cos(theta_x)],
      ]

  r_y = [
      [ cos(theta_y), 0.0, sin(theta_y)],
      [          0.0, 1.0,          0.0],
      [-sin(theta_y), 0.0, cos(theta_y)],
      ]

  r_z = [
      [cos(theta_z), -sin(theta_z), 0.0],
      [sin(theta_z),  cos(theta_z), 0.0],
      [         0.0,           0.0, 1.0],
      ]

  r_zy = matrix_mul(r_z, r_y)
  matrix_debug('r_zy', r_zy)

  r = matrix_mul(r_zy, r_x)
  matrix_debug('r', r)

  rotated_corners = matrix_mul(r, corners)
  matrix_debug('r_corners', rotated_corners)

  # get the shadows. projections of the corners on the xz-plane by dropping the Y
  projections = [list(get_col(rotated_corners, c)) for c in xrange(8)]
  projections = [(p[0], p[2]) for p in projections]
  matrix_debug('projections', projections)

  ch = convex_hull(projections)
  #logging.debug(ch)

  a = area(ch)
  #logging.debug(a)
  return a

  #if abs(a - target_a) <= 0.000001:
  if True:
    planes =[
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 0.5],
        ]

    rotated_planes = matrix_mul(r, planes)
    matrix_debug('planes', rotated_planes)
    return rotated_planes

  else:
    return None



lines = list(fileinput.input())

n_tc = int(lines.pop(0))

for i in xrange(n_tc):
  a = float(lines[i].strip())
  if i + 1 > n_tc:
    break
  ret = solve(a)
  print 'Case #{}:'.format(i+1)
  for row in ret:
    print '{}'.format(' '.join(map(str, row)))

