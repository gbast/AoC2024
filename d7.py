import networkx as nx
import matplotlib.pyplot as plt
import time
import sys

class TreeNode:
    def __init__(self, value, operation=None, left=None, right=None):
        self.value = value  # The result of the operation
        self.operation = operation  # The operation used to calculate the value
        self.left = left  # Left child (using +)
        self.right = right  # Right child (using *)

    def __repr__(self):
        return f"TreeNode(value={self.value}, operation={self.operation})"

class TreeNode2(TreeNode):
     def __init__(self, value, operation=None, left=None, right=None, mid=None):
        self.value = value  # The result of the operation
        self.operation = operation  # The operation used to calculate the value
        self.left = left  # Left child (using +)
        self.mid = mid # Mid child (using ||)
        self.right = right  # Right child (using *)
        
def build_tree(numbers, index=0, current_value=None):
    if index >= len(numbers):
        return None

    # Set the initial value
    if current_value is None:
        current_value = numbers[index]
        index += 1

    if index == len(numbers):
        # If no more numbers left, return the current node
        return TreeNode(value=current_value)

    # Create nodes for + and *
    left_child = build_tree(numbers, index + 1, current_value + numbers[index])
    right_child = build_tree(numbers, index + 1, current_value * numbers[index])

    # Return current node with children
    return TreeNode(
        value=current_value,
        operation=None,
        left=TreeNode(value=current_value + numbers[index], operation="+", left=left_child),
        right=TreeNode(value=current_value * numbers[index], operation="*", right=right_child),
    )

def print_tree(node, depth=0):
    if node is not None:
        print("  " * depth + f"{node.value} ({node.operation})")
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)

def get_leaf_values(node, leaf_values):
    if node is None:
        return
    if node.left is None and node.right is None:
        # If it's a leaf node, add the value
        leaf_values.append(node.value)
        return
    # Traverse left and right subtrees
    get_leaf_values(node.left, leaf_values)
    get_leaf_values(node.right, leaf_values)

     
        
def check_val(ref_value, lista):
    for l in lista:
        if(l==ref_value):
            return True
    return False

def process_tree():
    total_sum = 0  # To store the sum of reference values where match is true
    results = {}
    i = 0
    with open('d7.txt', 'r') as f:
            for line in f.readlines():
                temp = line.split(': ')
                ref_value = int(temp[0])
                numbers = [int(x) for x in temp[1].split(' ')]

           
                # Build the tree for the current list
                i+=1
                tree = build_tree(numbers)
                leaf_values = []
                get_leaf_values(tree, leaf_values)
                if check_val(ref_value, leaf_values):
                    total_sum += ref_value 
                #    print("FOUND",ref_value)
               
        #        print("Leaf values:", leaf_values)
                
                sys.stdout.write("\r%d" % (i) )
                sys.stdout.flush()
            
                del tree
    return total_sum









total_sum = process_tree()
print()
print(f"cnt=",total_sum)

##part2
def build_tree2(numbers, index=0, current_value=None):
    if index >= len(numbers):
        return None

    # Set the initial value
    if current_value is None:
        current_value = numbers[index]
        index += 1

    if index == len(numbers):
        # If no more numbers left, return the current node
        return TreeNode2(value=current_value)

    # Create nodes for + and *
    left_child = build_tree2(numbers, index + 1, current_value + numbers[index])
    mid_child = build_tree2(numbers, index + 1, int(str(current_value) + str(numbers[index]))  )
    right_child = build_tree2(numbers, index + 1, current_value * numbers[index])

    # Return current node with children
    return TreeNode2(
        value=current_value,
        operation=None,
        left=TreeNode2(value=current_value + numbers[index], operation="+", left=left_child),
        mid=TreeNode2(value=int(str(current_value) + str(numbers[index])), operation="||", left=mid_child),
        right=TreeNode2(value=current_value * numbers[index], operation="*", right=right_child),
    )

def get_leaf_values2(node, leaf_values):
    if node is None:
        return
    if node.left is None and node.right is None and node.mid is None:
        # If it's a leaf node, add the value
        leaf_values.append(node.value)
        return
    # Traverse left and right subtrees
    get_leaf_values2(node.left, leaf_values)
    get_leaf_values2(node.mid, leaf_values)
    get_leaf_values2(node.right, leaf_values)
    
def process_tree2():
    total_sum = 0  # To store the sum of reference values where match is true
    results = {}
    i = 0
    with open('d7.txt', 'r') as f:
            for line in f.readlines():
                temp = line.split(': ')
                ref_value = int(temp[0])
                numbers = [int(x) for x in temp[1].split(' ')]

           
                # Build the tree for the current list
                i+=1
                tree = build_tree2(numbers)
                leaf_values = []
                get_leaf_values2(tree, leaf_values)
                if check_val(ref_value, leaf_values):
                    total_sum += ref_value 
                sys.stdout.write("\r%d" % (i) )
                sys.stdout.flush()
            
                del tree
    return total_sum


total_sum2 = process_tree2()
print()
print(f"cnt2=",total_sum2)