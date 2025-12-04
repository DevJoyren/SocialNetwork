from components.network_reader import NetworkReader
from components.social_graph import SocialGraph
from components.pathfinder import PathFinder
from components.suggestions_engine import SuggestionEngine

DATA = "data/network.txt"

def main():
    # Load the network from the text file.
    # This step transforms the raw file into a usable adjacency list.
    reader = NetworkReader(DATA)
    data = reader.load()

    # Create the main graph object and helper classes.
    # - SocialGraph holds all users and friendships
    # - PathFinder handles shortest-path queries (BFS)
    # - SuggestionEngine generates friend recommendations
    graph = SocialGraph(data)
    pathfinder = PathFinder(graph)
    suggester = SuggestionEngine(graph)

    # Print basic statistics so the user knows the network was read correctly.
    print("Network Statistics:")
    print("Total users:", graph.total_users())
    print("Total friendships:", graph.total_friends())

    # Main program loop. This keeps asking the user for actions until they quit.
    while True:
        print("\nPlease select an action:")
        print("(1) Find shortest connection path")
        print("(2) Friend suggestions")
        print("(3) Quit")

        selection = input("Enter choice (1-3): ").strip()

        # Option 1: Find the shortest path between two users
        if selection == "1":
            start = input("Start user: ").strip()
            end = input("End user: ").strip()

            # Use BFS to compute the shortest path
            path = pathfinder.shortest_path(start, end)

            if path is None:
                # Either the users don't exist or there is no route between them
                print("\nNo connection found.")
            else:
                print("\nShortest path:")
                print(" -> ".join(path))
                print("Path length:", len(path) - 1)

        # Option 2: Show friend suggestions based on mutual friends
        elif selection == "2":
            user = input("Enter username: ").strip()

            try:
                # SuggestionEngine returns a ranked list of new possible connections
                suggestions = suggester.suggest(user)
            except KeyError as e:
                # Happens when the username does not exist
                print(e)
                continue

            # If the user has no suggestions, just let them know
            if not suggestions:
                print(f"\nNo friend suggestions for {user}.")
            else:
                print(f"\nFriend suggestions for {user}:")
                for name, count, mutuals in suggestions:
                    # Convert the set of mutual friends into a comma-separated list
                    mutual_list = ", ".join(sorted(mutuals))
                    print(f"- {name} ({count} mutual friends: {mutual_list})")

        # Option 3: Exit the program
        elif selection == "3":
            print("Goodbye.")
            break

        else:
            # User typed something outside 1–3
            print("Invalid selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    # Run the main function if the script is executed directly.
    main()
