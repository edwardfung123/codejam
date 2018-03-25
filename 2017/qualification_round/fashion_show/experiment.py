from itertools import product
from pprint import pprint

'''
rows = list(product('+x.o', repeat=3))

from main import check_row

for row in rows:
  ret = check_row(row, 3)
  pprint(row)
  pprint(ret)

zz
'''

n = 3
prod = product('+x.o', repeat=n*n)

products = list(prod)

#print('{} products'.format(len(all_products)))

#pprint(all_products)



pprint(products)

grids = []
for l in products:
  grid = [l[i:i+n] for i in xrange(0, n*n, n)]
  grids.append(grid)
pprint(grids[0])

from main import check_grid, rotate_grid, get_diagonal, check_diagonal, eval_grid

valid_grids = [(grid, eval_grid(grid)) for grid in grids if check_grid(grid, n)]
valid_grids.sort(key=lambda t: t[1], reverse=True)
pprint(valid_grids)

# check_grid(grids[0], n)
#grid = [
#    '...',
#    'x+o',
#    '.+.',
#    ]
#pprint(check_grid(grid, 3))
#for d in get_diagonal(grid, 3):
#  pprint(d)
#  pprint(check_diagonal(d))
