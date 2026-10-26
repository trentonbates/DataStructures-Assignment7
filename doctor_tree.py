class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Tree is empty. Cannot insert without root.")
            return False

        manager_name = str(manager_name).strip()
        employee_name = str(employee_name).strip()

        if manager_name == employee_name:
            print("Doctor cannot be a subordinate of themselves.")
            return False

        if manager_name == "" or employee_name == "":
            print("Names cannot be empty.")
            return False

        side = str(side).strip().lower()
        if side not in ("left", "right"):
            print(f"Invalid side '{side.upper()}'. Use 'LEFT' or 'RIGHT'.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(employee_name)
                print(f"✅ {employee_name} added to the LEFT of {manager_name}.")
            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(employee_name)
                print(f"✅ {employee_name} added to the RIGHT of {manager_name}.")
            else:
                print(f"{manager_name} already has a {side.upper()} subordinate.")
            return True

        found = False

        if current_node.left:
            found = self.insert(manager_name, employee_name, side, current_node.left)

        if not found and current_node.right:
            found = self.insert(manager_name, employee_name, side, current_node.right)

        if not found and current_node == self.root:
            print(f"{manager_name} not found in the tree.")

        return found

    def preorder(self, root):
        if root is None:
            return []
        return [root.name] + self.preorder(root.left) + self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.name] + self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.name]

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Bates", "Dr. Phan", "left")
tree.insert("Dr. Croft", "Dr. Bates", "left")
tree.insert("Dr. Croft", "", "left")
tree.insert("", "Dr. Phan", "left")

print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))