from itertools import product
import pprint

k = 5
max_c = 5
original_sequences = map(lambda x: ''.join(x), list(product(['L', 'G'], repeat=k)))
pprint.pprint(original_sequences)

arts = []
arts.append(original_sequences)

for i in xrange(2, max_c):
  last_art = arts[i-1 - 1]
  art = [last_seq.replace('G', original_sequences[-1]).replace('L', original_sequences[i]) for i, last_seq in enumerate(last_art)]
  arts.append(art)

pprint.pprint(arts)
