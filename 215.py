# Problem: The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.
#
# More rigorously, we can define it as follows:
#    The horizontal distance of the root is 0.
#    The horizontal distance of a left child is hd(parent) - 1.
#    The horizontal distance of a right child is hd(parent) + 1.
# The bottom view of a tree, then, consists of the lowest node at each horizontal distance.
# If there are two nodes at the same depth and horizontal distance, either is acceptable.

# node class
class Node:
    def __init__(self, val):
        self.value= val
        self.left = None
        self.right = None
    

#helper function
def dfs(nd, hd, mp):
    
    mp[hd] = nd.value
        
    if nd.left!=None:
        dfs(nd.left, hd-1, mp)
    if nd.right!=None:
        dfs(nd.right, hd+1, mp)
        
    return

#main function
def bottom(root):
    mp = {}
    res = []
    
    dfs(root, 0, mp)
    
    for i in sorted(mp):
        res.append(mp[i])

    return res


#create tree from list to test our algorithm
def bfs_create(lst, i):
    if i >= len(lst) or lst[i] == None:
        return None
    
    nd = Node(lst[i])
    nd.left = bfs_create(lst, 2 * i + 1)
    nd.right = bfs_create(lst, 2 * i + 2)

    return nd

tree = [5,3,7,1,4,6,9,0,None, None,None, None, None, 8]
a = bfs_create(tree, 0)

print(bottom(a))
