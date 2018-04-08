import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)

class Shoot(object):
  def __init__(self, pos, damage):
    self.pos = pos
    self.damage = damage

  def swap_to(self, new_pos):
    diff = abs(new_pos - self.pos)
    self.pos = new_pos
    self.damage /= (2 ** diff)

  def move_left_by_1(self):
    self.swap_to(self.pos - 1)

  def __str__(self):
    return '<Shoot pos={} damage={}>'.format(self.pos, self.damage)

  def __repr__(self):
    return self.__str__()


def can_withstand(shield, shots):
  total_damage = sum([s.damage for s in shots])
  return total_damage <= shield


def solve(shield, instructions):
  n_s = len(filter(lambda x: x == 'S', instructions))
  if n_s > shield:
    return 'IMPOSSIBLE'
  shots = []
  power = 1
  for pos, i in enumerate(instructions):
    if i == 'C':
      power *= 2
    elif i == 'S':
      shots.append(Shoot(pos, power))
  logging.debug(shots)

  #total_damage = sum([s.damage for s in shots])
  #if total_damage <= shield:
  #  return 0

  #logging.debug(total_damage)
  moves = 10000
  breaking_point = -1
  accumulator = 0
  for i, s in enumerate(shots):
    remaining_shots = len(shots) - i # include myself.
    if accumulator + s.damage * remaining_shots > shield:
      breaking_point = i
      break
    else:
      accumulator += s.damage
  else:
    return 0
  killing_blow = shots[breaking_point]
  logging.debug('shield = {}'.format(shield))
  logging.debug('killing blow = {}'.format(killing_blow))
  logging.debug('accumulated damage = {}'.format(accumulator))
  remaining_shots = len(shots) - breaking_point
  shots_before_killing = None if breaking_point == 0 else shots[breaking_point - 1]
  moves = 0
  prev_shots = [None] + list(shots[:-1])
  shots_and_prev = zip(shots, prev_shots)
  logging.debug(shots_and_prev)
  while True:
    for s, prev_shot in reversed(shots_and_prev):
      logging.debug('prev_shot = {}'.format(prev_shot))
      can_move_shot = prev_shot is None or (s.pos - prev_shot.pos > 1)
      if can_move_shot:
        s.move_left_by_1()
        moves += 1
        current_state = ['C'] * len(instructions)
        for s in shots:
          current_state[s.pos] = 'S'
        logging.debug(''.join(current_state))
        break
      else:
        logging.debug('cant move')
    if can_withstand(shield, shots):
      break
  return moves

lines = list(fileinput.input())

n_tc = int(lines.pop(0))

for i, l in enumerate(lines):
  if i + 1 > n_tc:
    break
  tmp = l.strip().split()
  shield = int(tmp[0])
  instructions = tmp[1]
  ret = solve(shield, instructions)
  print 'Case #{}: {}'.format(i+1, ret)
