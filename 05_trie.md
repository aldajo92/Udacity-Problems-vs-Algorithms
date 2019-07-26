The time complexity of Trie insert function is O(n), which n is the length of the word. The time complexity of Trie find function is O(m), which m is the length of prefix.

The time complexity of TrieNode suffix function is O(n*m), which n is the length of children, m is the recursion depth(the length of complete word).

So the timecomplexity of Trie autocomplete algorithm is O(n*m), and the space complexity is O(n), which n is the number of words have same prefix.