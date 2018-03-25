import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)


def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    n_lines = 2
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = int(tc[0], 10)
    adj = [int(s, 10) - 1 for s in tc[1].split()]
    answer = find_answer(F=adj)
    print 'Case #{}: {}'.format(i+1, answer)
    start_test += n_lines

import itertools
# The F parameter is the list of BFF identifiers, but 0-based (subtracting 1 from the input).
def find_answer(F):
  n = len(F)
  r = 0
  # Iterate over all possible orderings of the n kids.
  for O in itertools.permutations(xrange(n)):
    first = O[0]
    second = O[1]
    for i in xrange(1, n):  # Iterate over the permutation, skipping the first.
      # Check if i can be the last one by checking it and the first.
      prev = O[i - 1]
      cur = O[i]
      if ((F[cur] == first or F[cur] == prev) and
          (F[first] == cur or F[first] == second)):
        r = max(r, i + 1)
      # Check if i can be in the middle, and stop if it can't.
      if F[cur] != prev and (i == n - 1 or F[cur] != O[i + 1]):
        break
  return r

if __name__ == '__main__':
  main()
