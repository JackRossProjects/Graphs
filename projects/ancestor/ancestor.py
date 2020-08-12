# Util.py Stack class from earlier
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    # Initialize family tree dict
    tree = {}
    for i in range(len(ancestors)):
        # Check if children nodes are not in family tree
        if ancestors[i][1] not in tree.keys():
            # Create a set
            tree[ancestors[i][1]] = set()
            # Add ancestor node to set
            tree[ancestors[i][1]].add(ancestors[i][0])
        # If children node is in the tree
        else:
            # Add it's ancestor to the parent slot
            tree[ancestors[i][1]].add(ancestors[i][0])

    # key = child, value = parent

    # Initialize Stack and visited set
    s = Stack()
    visited = set()
    # Add the starting node to the top of the stack
    s.push(starting_node)

    # Ancestor stack
    anstack = Stack()
    # While there are still values in the stack
    while s.size() > 0:
        # V becomes the most recent value in the stack
        v = s.pop()
        # If the top value of the stack hasn't been visited
        if v not in visited:
            # Add it to the visited set
            visited.add(v)
            # Add it to the stack of ancestorsy
            anstack.push(v)
            # If that node isn't in the family tree
            if v not in tree.keys():
                pass
            # If that node is in the family tree
            else:
                # Add it to the stack
                for next_vert in tree[v]:
                    s.push(next_vert)
            

    parent = anstack.pop()
    child = anstack.pop()

    #  If individual has no parents, the function should return -1.
    if parent == starting_node:
        return - 1
    # If individual has no children, return the parent 
    elif child is None:
        return parent
    # If the parent and child are not in the family tree
    elif parent not in tree.keys() and child not in tree.keys():
        # Check if tied for earliest and return lowest value
        if parent > child:
            return child
        else:
            return parent
    # If it is in the tree, 
    else:
        # Return earliers ancestor
        return parent
    
