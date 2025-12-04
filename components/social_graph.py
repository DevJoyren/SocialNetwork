# Statistics

class SocialGraph:
    def __init__(self, adjacency: dict[str, set[str]]):
        # Store the full adjacency list that was created by NetworkReader.
        # This represents the entire social network.
        self.adj = adjacency

    def has_user(self, user: str) -> bool:
        """
        Checks whether the given user exists in the network.
        Returns True if the username is in the adjacency list.
        """
        return user in self.adj

    def friend_of(self, user: str) -> set[str]:
        """
        Returns the set of direct friends for the given user.
        If the user does not exist, return an empty set instead of crashing.
        """
        return self.adj.get(user, set())

    def total_users(self) -> int:
        """
        Counts the total number of unique users in the network.
        Simply the number of keys in the adjacency dictionary.
        """
        return len(self.adj)

    def total_friends(self) -> int:
        """
        Counts all friendships in the network.

        Every friendship appears twice in the adjacency list
        (A is in B's list AND B is in A's list),
        so we divide the total sum by 2 to avoid double-counting.
        """
        return sum(len(f) for f in self.adj.values()) // 2
