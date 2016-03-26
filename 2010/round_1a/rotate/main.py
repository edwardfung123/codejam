import fileinput
import logging
#logging.basicConfig(level=logging.DEBUG)

def apply_gravity(col):
  #logging.debug('col = ' + col)
  #last_piece = max(col.rfind('R'), col.rfind('B'))
  #logging.debug('last_piece = ' + str(last_piece))
  #col = col[last_piece+1:] + col[:last_piece + 1]
  length = len(col)
  s = col.replace('.', '')
  col = '.' * (length - len(s)) + s
  return col

def rotate(lines, size, is_apply_gravity=True):
  ''' rotate the board clockwise '''
  logging.debug('lines = ')
  for l in lines:
    logging.debug(l)
  columns = list(reversed(lines))
  # apply gravity
  if is_apply_gravity:
    columns = map(apply_gravity, columns)
  #logging.debug('rotated')
  #for l in columns:
  #  logging.debug(l)
  new_lines = []
  for i in xrange(0, size):
    chars = [col[i] for col in columns]
    l = ''.join(chars)
    logging.debug('{}: l = {}'.format(i, l))
    new_lines.append(l)
  return new_lines

def is_win(lines, char, length):
  def check_horizontal(lines):
    match_str = char * length
    logging.debug('match_str = ' + match_str)
    for l in lines:
      if match_str in l:
        return True
    return False
  # check horizontal
  win = check_horizontal(lines)
  if win:
    return True

  # check vertical
  logging.debug('checking vertical')
  rotated = rotate(lines, len(lines[0]), is_apply_gravity=False)
  #for l in rotated:
  #  logging.debug(l)
  win = check_horizontal(rotated)
  if win:
    return True

  # check \ 
  logging.debug('checking \\')
  size = len(lines[0])
  def check_diagonal(lines):
    for y, l in enumerate(lines[:size-length+1]):
      for x, c in enumerate(l[:size-length+1]):
        if c == char:
          chars = set([lines[y+i][x+i] for i in xrange(0, length)])
          #logging.debug('chars = ' + str(chars) + str(len(chars)))
          if len(chars) == 1 and char in chars:
            return True
    return False
  if check_diagonal(lines):
    return True
  # check /
  flipped = [l[::-1] for l in lines]
  if check_diagonal(flipped):
    return True
  return False

def find_answer(lines, size, length):
  ''' Find the answer for this question '''
  rotated = rotate(lines, size, is_apply_gravity=True)
  logging.debug('rotated = ')
  for l in rotated:
    logging.debug(l)
  (is_r_win, is_b_win) = (is_win(rotated, 'R', length), is_win(rotated, 'B', length))
  if is_r_win and is_b_win:
    return 'Both'
  elif is_r_win:
    return 'Red'
  elif is_b_win:
    return 'Blue'
  else:
    return 'Neither'

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  #logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    (size, length) = map(int, lines[start_test].split())
    tc = lines[start_test+1:start_test+1+size]
    #logging.debug(tc)
    n = find_answer(tc, size, length)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += 1 + size 

if __name__ == '__main__':
  main()
