The solution found was to split a path based on "/" as a list. Similar to autocomplete Trie, the list of the elements represent the char of the word, and RouteTrie implement Router.

The time complexity of RouteTrie fo finding and inserting function is O(n), which n is the length of path_list. The space complexity of Router is O(n), which n is the length of path list.