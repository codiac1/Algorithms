from collections import defaultdict, deque
class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:

        # 1. Create adjacency list
        def adjacencyList():

            # Initialize the adjacency list
            adj = defaultdict(list)

            # Iterate through all words
            for word in wordList:

                # Iterate through all characters in a word
                for i, _ in enumerate(word):

                    # Create the pattern
                    pattern = word[:i] + "*" + word[i + 1 :]

                    # Add a word into the adjacency list based on its pattern
                    adj[pattern].append(word)

            return adj

        # 2. Create reversed adjacency list
        def bfs(adj):

            # Initialize the reversed adjacency list
            reversedAdj = defaultdict(list)

            # Initialize the queue
            queue = deque([beginWord])

            # Initialize a set to keep track of used words at previous level
            visited = set([beginWord])

            while queue:

                # Initialize a set to keep track of used words at the current level
                visitedCurrentLevel = set()

                # Get the number of words at this level
                n = len(queue)

                # Iterate through all words
                for _ in range(n):

                    # Pop a word from the front of the queue
                    word = queue.popleft()

                    # Generate pattern based on the current word
                    for i, _ in enumerate(word):

                        pattern = word[:i] + "*" + word[i + 1 :]

                        # Itereate through all next words
                        for nextWord in adj[pattern]:

                            # If the next word hasn't been used in previous levels
                            if nextWord not in visited:

                                # Add such word to the reversed adjacency list
                                reversedAdj[nextWord].append(word)

                                # If the next word hasn't been used in the current level
                                if nextWord not in visitedCurrentLevel:

                                    # Add such word to the queue
                                    queue.append(nextWord)

                                    # Mark such word as visited
                                    visitedCurrentLevel.add(nextWord)

                # Once we done with a level, add all words visited at this level to the visited set
                visited.update(visitedCurrentLevel)

                # If we visited the endWord, end the search
                if endWord in visited:
                    break

            return reversedAdj

        # 3. Construct paths based on the reversed adjacency list using DFS
        def dfs(reversedAdj, res, path):

            # If the first word in a path is beginWord, we have succesfully constructed a path
            if path[0] == beginWord:

                # Add such path to the result
                res.append(list(path))

                return

            # Else, get the first word in a path
            word = path[0]

            # Find next words using the reversed adjacency list
            for nextWord in reversedAdj[word]:

                # Add such next word to the path
                path.appendleft(nextWord)

                # Recursively go to the next word
                dfs(reversedAdj, res, path)

                # Remove such next word from the path
                path.popleft()

            # Return the result
            return res

        # Do all three steps
        adj = adjacencyList()
        reversedAdj = bfs(adj)
        res = dfs(reversedAdj, [], deque([endWord]))

        return res