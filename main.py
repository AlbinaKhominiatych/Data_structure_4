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

    def display_top_popular(self):
        self.popular = []
        self._get_popular_words(self.root)
        if self.popular:
            print("Топ 10")
            for word in self.popular[:10]:
                print(f'{word.key}: {word.counter} було додано разів')
            else:
                print("Слова відсутні")


    def _get_popular_words(self, node):
        if node is not None:
            self._get_popular_words(node.left)
            self.popular.append(node)
            self.popular.sort(key=lambda x: x.counter, reverse=True)
            if len(self.popular)>10:
                self.popular.pop()
            self._get_popular_words(node.right)

dictionary = DictionaryTree()
dictionary.add_word("apple", "яблуко")
dictionary.add_word("apple", "яблучко")
dictionary.add_word("banana", "банан")
dictionary.display_top_popular()