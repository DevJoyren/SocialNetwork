from collections import deque

class PathFinder:
    def __init__(self, graph):
        self.g = graph

    def shortest_path(self, start: str, end: str) -> list[str] | None:
        """
        "Searches for shortest path between start and end
         Using BFS to find the shortest path"
        :param start:
        :param end:
        :return:
        """

        if not self.g.has_user(start) or not self.g.has_user(end):
            return None

        if start == end:
            return [start]

        q = deque([start])
        visited = {start}
        prev = {start: None}

        while q:
            current = q.popleft()

            for neighbor in self.g.friends_of(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    prev[neighbor] = current
                    q.append(neighbor)

                    if neighbor == end:
                        q.clear()
                        break

        if end not in prev:
            return None

        path = []
        node = end
        while node is not None:
            path.append(node)
            node = prev[node]

        return list(reversed(path))