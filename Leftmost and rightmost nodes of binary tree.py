'''
Leftmost and rightmost nodes of binary tree
Given a Binary Tree of size N, Print the corner nodes ie- the node at the leftmost and rightmost of each level.
Input :
         1
       /  \
     2      3
    / \    / \
   4   5  6   7    
Output: 1 2 3 4 7
Explanation:
Corners at level 0: 1
Corners at level 1: 2 3
Corners at level 2: 4 7

Input:

        10
      /    \
     20     30
    / \  
   40  60
Output: 10 20 30 40 60
'''

def printCorner(root):
    if not root:
        return
    
    q = []
    q.append(root)
    
    while q:
        n = len(q)
        
        # Traverse the current level
        for i in range(n):
            node = q.pop(0)
            
            # Print the first node of the current level
            if i == 0:
                print(node.data, end=" ")

            # Enqueue the children of the current node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # Print the last node of the current level
        if n > 1:
            print(node.data, end=" ")
