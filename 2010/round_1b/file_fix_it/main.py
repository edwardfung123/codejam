import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)
import pprint
import re

def find_mkdir(exist_dirs, target_dirs):
  ret = 0
  dirs = set(['/'] + exist_dirs)
  for d in target_dirs:
    if d in dirs:
      continue
    logging.debug('target = ' + d)
    to_mkdir = [d]
    current = d
    parent, tail = current.rsplit('/', 1)
    logging.debug('parent = ' + parent)
    while parent != '' and parent not in dirs:
      to_mkdir.append(parent)
      parent, tail = parent.rsplit('/', 1)
      logging.debug('parent = ' + parent)
    logging.debug(to_mkdir)
    ret += len(to_mkdir)
    dirs |= set(to_mkdir)
  return ret

def main():
  lines = [l.strip() for l in fileinput.input()]
  n_tests = int(lines[0])
  tests = []
  start_of_test = 1
  for i in xrange(0, n_tests):
    (exists, targets) = map(int, lines[start_of_test].split())
    logging.debug((exists, targets))
    exist_dirs  = lines[start_of_test + 1          : start_of_test + 1 + exists]
    target_dirs = lines[start_of_test + 1 + exists : start_of_test + 1 + exists + targets]
    logging.debug('exist_dirs = ' + str(exist_dirs))
    logging.debug('target_dirs = ' + str(target_dirs))
    start_of_test += (exists + targets + 1)
    n = find_mkdir(exist_dirs, target_dirs)
    print 'Case #{}: {}'.format(i+1, n)



if __name__ == '__main__':
  main()
