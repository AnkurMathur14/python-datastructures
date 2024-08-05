"""
Trie data structure implementation.
Trie is also known as suffix tree or digital tree.
Trie is used to store and search english words very efficiently.
Search complexity: O(l) where l is the length of the word

The complexity of creating a trie is O(n*l), where n is the number of words, and l is an average length of the word:
you need to perform l lookups on the average for each of the n words in the set.

Same goes for looking up words later: you perform l steps for each of the n words.

"""

from node import TrieNode


class Trie:
    def __init__(self, word=None):
        self.root = TrieNode()
        if word:
            self.create_trie(word)

    def __repr__(self):
        return "{}()".format(Trie.__class__.__name__)

    def __str__(self):
        pass

    def __del__(self):
        del self.root

    def create_trie(self, word):
        self.insert(word)

    # T : O(word_length)
    def insert(self, word):
        curr = self.root
        for ch in word:
            if not curr.children[ord(ch) - ord('A')]:
                curr.children[ord(ch) - ord('A')] = TrieNode()
            curr = curr.children[ord(ch) - ord('A')]
        curr.is_terminated = True

    # T : O(word_length)
    def search(self, word):
        curr = self.root
        for ch in word:
            if not curr.children[ord(ch) - ord('A')]:
                return False
            curr = curr.children[ord(ch) - ord('A')]
        return curr.is_terminated

    @staticmethod
    def __search_with_wild_char(node, word, pos):
        if pos >= len(word):
            return node.is_terminated

        if word[pos] != "*":
            node = node.children[ord(word[pos]) - ord('A')]
            if not node:
                return False
            return Trie.__search_with_wild_char(node, word, pos + 1)

        for i in range(26):
            if node.children[i] and Trie.__search_with_wild_char(node.children[i], word, pos + 1):
                return True
        return False

    def search_with_wild_char(self, word):
        return Trie.__search_with_wild_char(self.root, word, 0)

    def starts_with(self, word):
        curr = self.root
        for ch in word:
            if not curr.children[ord(ch) - ord('A')]:
                return False
            curr = curr.children[ord(ch) - ord('A')]
        return True


def main():
    t = Trie("START")

    words = ["ARE", "AS", "DO", "DOT", "NEW", "NEWS", "NO", "NOT", "JUMPER"]
    for word in words:
        t.insert(word)

    print(t.search("START"))  # True
    print(t.search("JUMP"))  # False
    print(t.starts_with("JUMP"))  # True
    print(t.search_with_wild_char("JU*P*R"))  # True
    print(t.search_with_wild_char("DOT*"))  # False


if __name__ == '__main__':
    main()
