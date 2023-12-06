class TreeNode:
    def __init__(self, key, translation):
        self.key = key
        self.translation = translation
        self.left = None
        self.right = None
        self.counter = 1

class DictionaryTree:
    def __init__(self):
        self.root = None
        self.popular = []

    def add_word(self, key, translation):
        if not self.root:
            self.root = TreeNode(key, translation)
        else:
            self._add_word(self.root, key, translation)

    def _add_word(self, node, key, translation):
        if key == node.key:
            node.translation = translation
            node.counter += 1 #звернути увагу на підрахунок
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, translation)
            else:
                self._add_word(node.left, key, translation)
        else:
            if node.right is None:
                node.right = TreeNode(key, translation)
            else:
                self._add_word(node.right, key, translation)
