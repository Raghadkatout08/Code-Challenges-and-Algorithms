class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def sortedArrayToBST(self, nums):
        def helper(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            
            return root
        
        return helper(0, len(nums) - 1)

def print_tree(root):
    if not root:
        return "[]"
    
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values from the end
    while result and result[-1] is None:
        result.pop()
    
    return str(result).replace("None", "null")

# Example usage:
if __name__ == "__main__":
    tree = Tree()
    
    nums1 = [-10, -3, 0, 5, 9]
    root1 = tree.sortedArrayToBST(nums1)
    
    if root1:
        print("Input: nums =", nums1)
        print("Output:", print_tree(root1))
    
    nums2 = [1, 3]
    root2 = tree.sortedArrayToBST(nums2)

    print("***************************")

    if root2:
        print("Input: nums =", nums2)
        print("Output:", print_tree(root2))
    
    print("***************************")

    nums3 = [1, 2, 3, 4, 5, 6, 7]
    root3 = tree.sortedArrayToBST(nums3)
    
    if root3:
        print("Input: nums =", nums3)
        print("Output:", print_tree(root3))
    print("***************************")

    nums4 = [-5, -3, -1, 0, 2, 4, 6]
    root4 = tree.sortedArrayToBST(nums4)
    
    if root4:
        print("Input: nums =", nums4)
        print("Output:", print_tree(root4))
