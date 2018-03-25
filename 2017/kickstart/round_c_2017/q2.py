from x_squared.answer import answer
import fileinput
lines = list(fileinput.input())

n = int(lines.pop(0), 10)

i = 1
while len(lines):
  n_lines = int(lines.pop(0), 10)
  grid, lines = lines[:n_lines], lines[n_lines:]
  print 'Case #{}: {}'.format(i, answer(grid))
  i += 1

