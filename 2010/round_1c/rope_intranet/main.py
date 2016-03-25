import fileinput
import logging
#logging.basicConfig(level=logging.DEBUG)

class Cable(object):
  def __init__(self, id, l, r):
    self.id = id
    self.l = l
    self.r = r
    self.slope = float(r)/l

  def __repr__(self):
    return '<Cable#{id} (l={l}, r={r}, slope={slope:.2f})>'.format(l=self.l, r=self.r, slope=self.slope, id=self.id)

def find_intersection(cables):
  logging.debug(cables)
  cables_to_loop = [c for c in cables if c.slope >= 0]
  cables_to_loop.sort(key=lambda c: c.l)
  #sorted_by_l = sorted(cables, key=lambda c:c.l)
  #sorted_by_r = sorted(cables, key=lambda c:c.r)
  logging.debug(cables_to_loop)
  ret = 0
  for c in cables_to_loop:
    intersected_cables = [cc for cc in cables if cc.l > c.l and cc.r < c.r]
    ret += len(intersected_cables)
  return ret

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  n_tests = int(lines[0])
  start_testcase = 1
  for i in xrange(0, n_tests):
    n_cables = int(lines[start_testcase])
    cables = [Cable(j, *map(int, l.split())) for j, l in enumerate(lines[start_testcase+1:start_testcase+1+n_cables])]
    n = find_intersection(cables)
    print 'Case #{}: {}'.format(i+1, n)
    start_testcase += n_cables + 1

if __name__ == '__main__':
  main()
