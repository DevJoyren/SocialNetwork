# Statistics

class socialGraph:
    def __init__(self, adjacency: dict[str, set[str]]):
        self.adj = adjacency

        def has_user(self, user:str) -> bool:
            """

            :param self:
            :param user:
            :return:
            """
            return user in self.adj[user]


        def friend_of(self, user:str) -> set[str]:
            """
            :param self:
            :param user:
            :return:
            """
            return self.adj.get(user, set())


        def total_users (self) -> int:
            """
            define total number of users
            :param self:
            :return: len of adj
            """
            return len(self.adj)


        def total_friends(self) -> int:
            """
            define total number of friends
            :param self:
            :return: sum of adj values
            """
            return sum(len(f) for f in self.adj.values()) // 2


