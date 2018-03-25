import fileinput
import logging
logging.basicConfig(level=logging.DEBUG)


def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    n_lines = 2
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = int(tc[0], 10)
    adj = [int(s, 10) - 1 for s in tc[1].split()]
    answer = find_answer(adj=adj, n=n)
    print 'Case #{}: {}'.format(i+1, answer)
    start_test += n_lines

class SimplePath(object):
    def __init__(self, i, adj):
        self.nodes = [i]
        self.is_cyclic = False
        self.is_cyclic_tail = False
        self.cycle_start_node_index = None
        
        n = len(adj)
        cur = i
        # print '----'
        for i in xrange(0, n):
            next = adj[cur]
            # print 'next = %d' % next
            self.is_cyclic = next in self.nodes
            if self.is_cyclic:
                # print 'loop'
                # loop
                self.cycle_start_node_index = self.nodes.index(next)
                if next == self.nodes[-2]:
                    self.is_cyclic_tail = True
                break
            self.nodes.append(next)
            cur = next
            
    def __repr__(self):
        return '<SimplePath nodes={nodes}, is_cyclic={is_cyclic}, cycle_start_node_index={cycle_start_node_index}, is_cyclic_tail={is_cyclic_tail}>'.format(
            nodes=self.nodes, is_cyclic=self.is_cyclic, is_cyclic_tail=self.is_cyclic_tail,
            cycle_start_node_index=self.cycle_start_node_index)
    
    def __len__(self):
        return len(self.nodes)
    
    @property
    def cyclic_tail(self):
        return self.nodes[-2:] if self.is_cyclic_tail else None
    
    @property
    def head(self):
        return self.nodes[:-2]
    
    @property
    def is_circle(self):
        if self.is_cyclic == False:
            return False
        else:
            if self.cycle_start_node_index == 0:
                return True
            elif self.is_cyclic_tail == True:
                return True
        return False
    
    @property
    def is_complete_circle(self):
        return self.is_cyclic and self.cycle_start_node_index == 0

    def can_join_path(self, other):
        both_has_cyclic_tail = self.is_cyclic_tail == True and other.is_cyclic_tail == True
        same_tail = self.cyclic_tail[0] == other.cyclic_tail[1] and self.cyclic_tail[1] == other.cyclic_tail[0]
        different_head = set(self.head).isdisjoint(set(other.head))
        return (both_has_cyclic_tail and same_tail and different_head) 
    
    
    
class JoinedPath(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __len__(self):
        return len(self.p1) + len(self.p2) - 2
    
    def __repr__(self):
        return '<JoinedPath path1={p1}, path2={p2}, len={len}'.format(p1=self.p1, p2=self.p2, len=len(self))
    
    
def find_answer(n, adj):
    paths = [SimplePath(i, adj) for i in xrange(0, n)]
    valid_paths = [p for p in paths if p.is_circle]
    from pprint import pformat as pf
    #pp(paths)
    complete_circles = []
    lines = []
    for p in valid_paths:
        #pp((p, p.is_circle, len(p)))
        complete_circles.append(p) if p.is_complete_circle else lines.append(p)

    # TODO: optimize?    
    complete_circles.sort(key=len, reverse=True)    
    logging.debug(pf(complete_circles))
    # TODO: 
    lines.sort(key=len, reverse=True)
    logging.debug(pf(lines))
    from itertools import combinations
    comb = combinations(lines, 2)

    joinable_line_pairs = [p for p in comb if p[0].can_join_path(p[1])]
    #print 'joinable_line_pairs'
    #pp(joinable_line_pairs)
    joined_paths = [JoinedPath(*pair) for pair in joinable_line_pairs]
    joined_paths.sort(key=len, reverse=True)
    logging.debug('joined_paths')
    logging.debug(pf(joined_paths))

    longest_circle_path_len = len(complete_circles[0]) if complete_circles else -1
    longest_joined_path_len = len(joined_paths[0]) if joined_paths else -1
    longest_lines_len = len(lines[0]) if lines else -1

    return max(longest_circle_path_len, longest_joined_path_len, longest_lines_len)

if __name__ == '__main__':
  main()
