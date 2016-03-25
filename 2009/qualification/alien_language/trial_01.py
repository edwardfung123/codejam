import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)
import pprint
import itertools

def find_words(word_dict, line):
  # split the line into tokens
  tmp = line.split(')')
  if len(tmp) == 1:
    return 1 if line in word_dict else 0
  tokens = [[s[1:]] if s.startswith('(') else list(s)  for s in tmp]
  tokens = [item for sublist in tokens for item in sublist]
  logging.debug(tokens)
  ret = reduce(lambda x,y: x + 1 if y in word_dict else x, map(''.join, itertools.product(*tokens)), 0)
  return ret

def main():
  i = 1
  lines = [line.strip() for line in fileinput.input()]
  (word_length, dict_size, test_size) = map(int, lines[0].split())
  #logging.debug((word_length, dict_size, test_size))
  word_dict = set(lines[1:dict_size+1])
  #logging.debug(word_dict)
  for i, line in enumerate(lines[dict_size+1:]):
    logging.debug(line)
    n = find_words(word_dict, line)
    print 'Case #{i}: {val}'.format(i=i+1, val=n)




if __name__ == '__main__':
  main()
