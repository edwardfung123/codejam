import fileinput

def sorter(name_t):
  return name_t[1]


def grouper(name_t):
  return name_t[1]

def solve(names):
  names = [(n, len(set(n.replace(' ', '', 20)))) for n in names]
  names.sort(key=sorter)
  from itertools import groupby
  grouped = {k: list(v) for k, v in groupby(names, key=grouper)}
  import pprint
  #pprint.pprint(grouped)
  names = grouped[max(grouped.keys())]
  names.sort(key=lambda t: t[0])
  if len(names) > 1:
    # pprint.pprint(names)
    pass
  return names[0][0]


lines = list(fileinput.input())
lines.pop(0)
i = 0
while len(lines) > 0:
  n = int(lines.pop(0), 10)
  names, lines = lines[:n], lines[n:]
  names = [n.strip() for n in names]
  s1 = solve(names)
  print "Case #{}: {}".format(i+1, s1)
  i += 1
