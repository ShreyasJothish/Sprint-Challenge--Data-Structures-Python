class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = Node(value)
        current = self

        while current:
            # Traverse right
            if current.value < node.value:
                if current.right:
                    current = current.right
                else:
                    break
            # Traverse left
            else:
                if current.left:
                    current = current.left
                else:
                    break

        if current.value < node.value:
            current.right = node
        else:
            current.left = node

    def contains(self, target):
        current = self

        while current:
            if current.value == target:
                return True

            if current.value < target:
                current = current.right
            else:
                current = current.left

        return False

    def get_max(self):
        current = self

        while current:
            if current.right:
                current = current.right
            else:
                break

        return current.value

    def for_each(self, cb):

        def traverse(self, cb):
            if not self:
                return

            left = self.left
            right = self.right

            traverse(left, cb)
            cb(self.value)
            traverse(right, cb)

        return traverse(self, cb)
