class SuggestionEngine:
    def __init__(self, graph):
        # Store the graph instance so we can access all users + friendships
        # This keeps the suggestion logic separated from the graph structure itself.
        self.g = graph

    def suggest(self, user: str) -> list[tuple[str, int, set[str]]]:
        """
        Returns a list of tuples (suggested_user, mutual_count, mutual_friends)
        sorted by mutual_count desc.
        :return suggestions
        """

        # Check if the user actually exists in the network.
        # If not, there's no point calculating anything.
        if not self.g.has_user(user):
            raise KeyError(f"User '{user}' not found in network.")

        # Direct friends of the target user.
        # Using a set for fast lookups
        direct = self.g.friend_of(user)

        # Dictionary to store potential suggestions:
        # key = friend-of-friend (candidate)
        # value = set of mutual friends
        mutual_counts = {}

        # Loop through each *direct* friend
        for friend in direct:

            # For each friend, check all their friends (friends-of-friends)
            for fof in self.g.friend_of(friend):

                # Skip if the friend-of-friend is the user themself
                # This prevents things like suggesting the user to themselves.
                if fof == user:
                    continue

                # Skip if the friend-of-friend is already a direct friend.
                # We want *new* connections, not people the user already knows.
                if fof in direct:
                    continue

                # At this point, `fof` is a valid candidate for suggestion.
                # Add the mutual friend to the set of mutual friends.
                if fof not in mutual_counts:
                    mutual_counts[fof] = set()

                # Add the current friend as a mutual friend between user and fof.
                mutual_counts[fof].add(friend)

        # Convert the dictionary into a list of tuples:
        # (person, number_of_mutual_friends, set_of_mutual_friends)
        suggestions = [
            (person, len(mutuals), mutuals)
            for person, mutuals in mutual_counts.items()
        ]

        # Sort the suggestions:
        # 1. Highest mutual-friend count first
        # 2. Alphabetical order to keep results stable and readable
        suggestions.sort(key=lambda x: (-x[1], x[0]))

        # Return the final ranked list of suggestions.
        return suggestions
