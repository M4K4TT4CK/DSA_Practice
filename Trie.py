from TrieNode import TrieNode

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # O(K) where K is the number of characters in the string
    def search(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        return currentNode

    # O(K) where K is the number of characters in the string
    def insert(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                currentNode = newNode
        currentNode.children['*'] = None

    # Recursive method to collect all words starting from a node
    def collectAllWords(self, words, node=None, word=''):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            if key == '*':
                words.append(word)
            else:
                self.collectAllWords(words, childNode, word + key)
        return words

    
    def autoComplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        else:
            return self.collectAllWords([], currentNode)

if __name__ == "__main__":
    # Create a Trie instance
    trie = Trie()

    # Insert some words into the Trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    trie.insert("bat")
    trie.insert("batman")

    # Test searching for words in the Trie
    word_to_search = "apple"
    search_result = trie.search(word_to_search)
    if search_result:
        print(f"'{word_to_search}' found in Trie")
    else:
        print(f"'{word_to_search}' not found in Trie")

    word_to_search = "apples"
    search_result = trie.search(word_to_search)
    if search_result:
        print(f"'{word_to_search}' found in Trie")
    else:
        print(f"'{word_to_search}' not found in Trie")

    # Test autocomplete feature
    prefix_to_complete = "ba"
    autocomplete_results = trie.autoComplete(prefix_to_complete)
    if autocomplete_results:
        print(f"Autocomplete suggestions for '{prefix_to_complete}':")
        for suggestion in autocomplete_results:
            print(suggestion)
    else:
        print(f"No autocomplete suggestions for '{prefix_to_complete}'")
