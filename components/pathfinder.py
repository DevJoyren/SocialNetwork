from collections import deque

class PathFinder:
    def __init__(self, graph):
        # Store a reference to the SocialGraph instance.
        # We only need it to access users and their friend lists.
        self.g = graph

    def shortest_path(self, start, end):
        # Basic sanity check: if either user doesn't exist,
        # there's no valid path to calculate.
        if not self.g.has_user(start) or not self.g.has_user(end):
            return None

        # BFS uses a queue. We start by exploring from the start user.
        queue = deque([start])

        # 'visited' keeps track of everyone we've already processed
        # so we don't revisit users or fall into infinite loops.
        visited = {start}

        # 'prev' lets us reconstruct the final path by storing
        # where each node came from during BFS.
        prev = {start: None}

        # This flag becomes True once we've reached the target user.
        found = False

        # Standard BFS loop
        while queue:
            # Take the next user from the queue
            current = queue.popleft()

            # Explore all of their direct friends (neighbors)
            for neighbor in self.g.friend_of(current):

                # Only process users we haven't visited yet
                if neighbor not in visited:
                    visited.add(neighbor)       # mark as visited
                    prev[neighbor] = current    # remember how we reached them
                    queue.append(neighbor)      # add them for further exploration

                    # If we found the target user, we can stop early.
                    # BFS guarantees this is the *shortest* path.
                    if neighbor == end:
                        found = True
                        break

            # Break outer loop as well once the target is found
            if found:
                break

        # If we never reached the target, there's no connection at all.
        if not found:
            return None

        # --- Reconstruct the shortest path using the 'prev' dictionary ---
        path = []
        node = end

        # Walk backwards from the end user to the start user
        while node is not None:
            path.append(node)
            node = prev[node]

        # Reverse it to get the path from start → end
        return list(reversed(path))
