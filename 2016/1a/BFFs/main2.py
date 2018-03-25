import fileinput
import logging
from pprint import pformat as pf

#logging.basicConfig(level=logging.DEBUG)

debug = logging.debug


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
    bffs = [int(s, 10) for s in tc[1].split()]
    answer = find_answer(bffs)
    print 'Case #{}: {}'.format(i+1, answer)
    start_test += n_lines

class TreeNode(object):
    bffBy = None
    id = None
    myBff = None
    
    def __init__(self, bffBy=None, id=None, myBff=None):
        if bffBy is None:
            bffBy = []
        self.bffBy = bffBy
        self.id = id
        self.myBff = myBff
        self._depth = None
        
    def __str__(self):
        return '<Kid id="{id}", bffby={bffBy}, myBff={myBff}>'.format(
            id=self.id, 
            bffBy=[bff.id for bff in self.bffBy] if self.bffBy else self.bffBy,
            myBff=self.myBff.id if self.myBff else self.myBff)
    
    def __repr__(self):
        return str(self)
    
    @property
    def depth(self):
        # print 'depth ' + str(self.id)
        if self._depth is None:
            if self.bffBy is None or len(self.bffBy) == 0:
                self._depth = 1
            else:
                self._depth = max(bff.depth for bff in self.bffBy) + 1
        return self._depth
    
    def isGluable(self):
        return False

    
    
class SuperNode(TreeNode):
    def __init__(self, **kwargs):
        self._loops = kwargs['loops']
        kwargs.pop('loops')
        super(SuperNode, self).__init__(**kwargs)
        
    def __str__(self):
        return '<SuperNode id="{id}", bffby={bffBy}, myBff={myBff}, loops={loops}>'.format(
            id=self.id, 
            bffBy=[bff.id for bff in self.bffBy] if self.bffBy else self.bffBy,
            myBff=self.myBff.id if self.myBff else self.myBff,
            loops=self._loops
        )

    @property
    def depth(self):
        # print 'SuperNode depth'
        if len(self._loops) > 2:
            return 1
        debug(self.bffBy[0])
        return (self.bffBy[0].depth+1, self.bffBy[1].depth+1)

    @property
    def length(self):
        # print 'SuperNode length'
        if len(self._loops) > 2:
            return len(self._loops)
        kid1Depth = max([bffBy.depth for bffBy in self._loops[0].bffBy if bffBy not in self._loops] or [0])
        kid2Depth = max([bffBy.depth for bffBy in self._loops[1].bffBy if bffBy not in self._loops] or [0])
        return kid1Depth + 2 + kid2Depth
    
    def isGluable(self):
        return len(self._loops) == 2
    
    
    
def buildTreesFromList(bffs):
    trees = {}
    nodes = {}
    for i, myBff in enumerate(bffs):
        me = i + 1
        if me not in nodes:
            nodes[me] = TreeNode(id=me)
            
        if myBff not in nodes:
            nodes[myBff] = TreeNode(id=myBff)
        
        nodes[me].myBff = nodes[myBff]
        nodes[myBff].bffBy.append(nodes[me])
        
    visited = set()
    for kid in nodes.values():
        if kid.id in visited:
            continue
        # let traverse the kid chain
        debug('current kid')
        debug(kid.id)
        visitedKids = set()
        pathIds = []
        while True:
            visited.add(kid.id)
            visitedKids.add(kid.id)
            pathIds.append(kid.id)
            nextKid = kid.myBff
            if nextKid is None:
                break
            if nextKid.id in visitedKids:
                # looped
                start = pathIds.index(nextKid.id)
                kidIdsInLoop = pathIds[start:]
                debug('kidIdsInLoop')
                debug(kidIdsInLoop)
                treeId = ','.join(map(str, sorted(kidIdsInLoop)))
                if treeId in trees:
                    break
                # Find the loop create a root node
                kidsInLoop = [nodes[id] for id in kidIdsInLoop]
                rootNode = SuperNode(loops=kidsInLoop, id=treeId)
                trees[treeId] = rootNode
                # replace all child nodes' bff to this super node
                for k in kidsInLoop:
                    debug('replacing bff')
                    for bffBy in k.bffBy:
                        if bffBy not in kidsInLoop:
                            # debug('numa numa')
                            bffBy.myBff = rootNode
                            # debug(bffBy)
                            rootNode.bffBy.append(bffBy)
                break
            kid = nextKid
    debug( 'nodes')
    debug(pf(nodes))
    #loners = {id: kid for id, kid in nodes.iteritems() if kid.bffBy is None or len(kid.bffBy) == 0}
    #pp(loners)
    
    return trees
    
    
def find_answer(bffs):
  trees = buildTreesFromList(bffs)
  debug('trees')
  debug(pf(trees))
      
      
  gluableLength = 0
  nonGluableLength = 0
  for t in trees.values():
      if t.isGluable():
          gluableLength += t.length
      else:
          nonGluableLength = max(nonGluableLength, t.length)
  debug(gluableLength)
  debug(nonGluableLength)
  return max(gluableLength, nonGluableLength)

if __name__ == '__main__':
  main()
