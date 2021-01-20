# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:17:35 2021

@author: Alfredo
"""


# Daily Coding Problem #445

# Problem:
# Given a binary tree where all nodes are either 0 or 1, prune the tree
# so that subtrees containing all 0s are removed.



class Node:
    def __init__(self, v, l = None, r = None):
        self.val = v
        self.left = l
        self.right = r
        
    def __str__(self):
        '''
        This function is taken from BinaryTree Python Library's Node class
        https://github.com/joowani/binarytree
        '''
    
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))
    

# recursive function that sums up the total of 1s in a node's children
# if a child has a zum of 0, the child is pruned
def pruneZeros(nd):
    if nd.left == None and nd.right == None:
        return nd.val
    
    l = 0
    r = 0
    
    if nd.left:
        l = pruneZeros(nd.left)
        
        if l == 0:
            nd.left = None
        
    if nd.right:
        r = pruneZeros(nd.right)
        
        if r == 0:
            nd.right = None
    
    return nd.val + l + r


# --------------------------------------------------------------------------
# Testing

def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    '''
    This function is taken from BinaryTree Python Library's Node class
    https://github.com/joowani/binarytree
    '''
    
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, root.val)
    else:
        node_repr = str(root.val)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        _build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


tree = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))
print(tree)
# 
#   0______
#  /       \
# 1       __0
#        /   \
#       1     0
#      / \
#     0   0
# 
pruneZeros(tree)
print(tree)
#
#   0__
#  /   \
# 1     0
#      /
#     1
# 
