from pprint import pformat as pf

def encode(c1, c2):
  s1 = 0 if c1 is None else ord(c1) - 65
  s2 = 0 if c2 is None else ord(c2) - 65
  #print s1, s2
  return (s1 + s2) % 26


#from itertools import combinations_with_replacement
#from string import ascii_uppercase
#
#mapping = {}
#for t in combinations_with_replacement(ascii_uppercase, 2):
#  k = chr(65 + encode(*t))
#  if k not in mapping:
#    mapping[k] = [t]
#  else:
#    mapping[k].append(t)
#
#logging.debug(pf(mapping))

#s = 'SOUP'
#s = 'EIGHT'
#encrypted = []
#for i, c in enumerate(s):
#  i0, i1 = i - 1, i + 1
#  c1 = s[i0] if i0 > -1 else None
#  c2 = s[i1] if i1 < len(s) else None
#  c = chr(65 + encode(c1, c2))
#  encrypted.append(c)
#
#encrypted = ''.join(encrypted)



def solve(encrypted):
  import logging
  logging.debug(encrypted)
  if len(encrypted) % 2 == 1:
    return 'AMBIGUOUS'

  decrypted = [''] * len(encrypted)
  decrypted[1] = encrypted[0]
  decrypted[-2] = encrypted[-1]
# TODO
  forward = []
  for i in xrange(2, len(encrypted), 2):
    c = encrypted[i]
    x = (26 + (ord(c) - ord(decrypted[i - 1]))) % 26
    decrypted[i + 1] = chr(65 + x) 
    #logging.debug(decrypted[i + 1])

  for i in xrange(-3, -len(encrypted), -1):
    c = encrypted[i]
    x = (26 + (ord(c) - ord(decrypted[i + 1]))) % 26
    decrypted[i - 1] = chr(65 + x)


  decrypted = ''.join(decrypted)
  return decrypted


if __name__ == '__main__':
  import os
  fin = os.getenv('IN')
  if fin:
    with open(fin, 'r') as f:
      n = int(f.readline(), 10)
      for i in xrange(n):
        encrypted = f.readline().strip()
        print 'Case #{}: {}'.format(i+1, solve(encrypted))
  else:
    import logging
    logging.basicConfig(level=logging.DEBUG)
    cases = [
        ('OMDU', 'SOUP'),
        ('BCB', 'AMBIGUOUS'),
        ('AOAAAN', 'BANANA'),
        ]

    for i, tc in enumerate(cases):
      try:
        ret = solve(*tc[:-1])
        assert ret == tc[-1]
        logging.info('case {}: passed!'.format(i))
      except AssertionError:
        logging.error('case {}: failed in as the return = {}'.format(i, ret))
