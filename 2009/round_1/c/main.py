import fileinput

for i, line in enumerate(fileinput.input()):
  if i == 0:
    n = int(line)
  else:
    line = line.strip()
    #print line
    base = len(set(line))
    base = base if base > 1 else 2
    #print 'base = %d' % base
    r = 0
    current_base = 1
    translation = {}
    j = 1
    for a in line:
      if a not in translation:
        translation[a] = j
        if j == 1:
          j = 0
        elif j == 0:
          j = 2
        else:
          j = j + 1
      else:
        continue
    #print str(translation)
    for a in reversed(line):
      a = translation[a]
      #print 'a = %d, x = %d' % (a, current_base)
      r += a * current_base
      current_base *= base
    print 'Case #{i}: {r}'.format(i=i, r=r)
