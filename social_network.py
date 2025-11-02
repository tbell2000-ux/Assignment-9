class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Test adding duplicate
    network.add_person("Alex")

    # Create friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # Error test
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    print("\n--- Social Network ---")
    network.print_network()


# A graph is the best structure to represent a social network because it works the same way people connect in real life.
# Each person is a node, and every friendship is a line that connects two people together. This makes it easy to see who is friends with who, and it lets people connect in many directions instead of following a single pattern.
# You can add new friends or remove them without messing up the whole structure. It also makes sense because in real life, friendships go both ways. If I am friends with you, you are friends with me too.
# Using a list or a tree would not work as well. A list is too simple because it only holds names in one order and does not show who is connected to who. A tree would not work either because it follows a parent and child structure, which would make it impossible to show that two people are connected both ways.
# Real social connections are more mixed, and people can be part of many friend groups that overlap.
# When I tested my network, I noticed that adding friends or printing out all the connections takes a little longer as the number of people grows. But this is worth it because the graph makes everything more realistic. It captures how people really interact and keeps the relationships easy to manage and understand.