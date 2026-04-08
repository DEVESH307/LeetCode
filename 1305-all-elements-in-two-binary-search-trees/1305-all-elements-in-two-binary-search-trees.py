# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def merge(self, arr1, arr2):
#         i = j = 0
#         merged = []

#         while i < len(arr1) and j < len(arr2):
#             if arr1[i] <= arr2[j]:
#                 merged.append(arr1[i])
#                 i += 1
#             else:
#                 merged.append(arr2[j])
#                 j += 1

#         # remaining
#         merged.extend(arr1[i:])
#         merged.extend(arr2[j:])

#         return merged

        
#     def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
#         def inorder(node, sorted_arr):
#             if not node:
#                 return

#             inorder(node.left, sorted_arr)
#             sorted_arr.append(node.val)
#             inorder(node.right, sorted_arr)

#         arr1 = []
#         arr2 = []

#         inorder(root1, arr1)
#         inorder(root2, arr2)

#         return self.merge(arr1, arr2)


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def merge(arr1, arr2):
            i = j = 0
            merged = []

            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1

            # remaining
            merged.extend(arr1[i:])
            merged.extend(arr2[j:])

            return merged

        return merge(inorder(root1), inorder(root2))