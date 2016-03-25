import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)
import pprint
import re

def find_words(word_dict, line):
  if '(' in line:
    # just use regex... why not..
    line = line.replace('(', '[').replace(')', ']')
    logging.debug(line)
    regex = re.compile(line)
    ret = reduce(lambda x, y: x + 1 if regex.match(y) else x, word_dict, 0)
    return ret
  else:
    return 1 if line in word_dict else 0


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
