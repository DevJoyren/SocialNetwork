# Script to read the text file and create a network dictionary

class NetworkReader:
    def __init__(self, filename: str):
        # Store the filename so the loader knows where to read the data from.
        self.filename = filename

    def load(self) -> dict[str, set[str]]:
        """
        Loads the social network from the text file and converts it
        into an adjacency dictionary where each user maps to a set
        of all their direct friends.
        :return: network (dict)
        """

        # The main structure that will hold all users and connections.
        network = {}

        # Try opening the file. If the file doesn't exist, we catch the error below.
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    # Remove extra whitespace and line breaks.
                    line = line.strip()

                    # Skip empty lines just in case the file contains them.
                    if not line:
                        continue

                    # Each line has the format: "User: friend1 friend2 friend3 ..."
                    user_part, friends_part = line.split(":")
                    user = user_part.strip()

                    # Split the friends into a list. If someone has no friends, handle it gracefully.
                    friends = friends_part.strip().split() if friends_part.strip() else []

                    # Make sure the user exists in the network dictionary.
                    # If they appear for the first time, initialize their set.
                    if user not in network:
                        network[user] = set()

                    # Loop through each listed friend
                    for friend in friends:
                        # Add the friend to the current user's set
                        network[user].add(friend)

                        # Ensure the friend is also present in the dictionary.
                        # This makes the graph symmetrical (mutual friendships).
                        if friend not in network:
                            network[friend] = set()

                        # Add the user to the friend's set as well.
                        # This keeps the graph undirected.
                        network[friend].add(user)

        except FileNotFoundError:
            # If the file cannot be found, show a clear error instead of crashing silently.
            raise FileNotFoundError(f"File {self.filename} not found.")

        # Return the adjacency dictionary representing the social network.
        return network
