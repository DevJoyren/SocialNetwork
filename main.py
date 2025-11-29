from components.network_reader import NetworkReader
from components.social_graph import SocialGraph


DATA = "data/network.txt"

def main():
    reader = NetworkReader(DATA)
    data = reader.load()
    graph = SocialGraph(data)

    print("Network Statistics:")
    print("Total users:", graph.total_users())
    print("Total friendships:", graph.total_friends())
    print(data)

if __name__ == "__main__":
    main()
