class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
g3 = Group("g3")
g4 = Group("g4")
g5 = Group("g5")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_child.add_group(g3)
g3.add_group(g4)

ray = 'ray'
bill = 'bill'
nina = 'nina'
parent.add_user(nina)
g4.add_user(ray)
g5.add_user(bill)
child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    if not isinstance(group, Group):
        return None
    queue = [group]
    idx = 0
    while idx < len(queue):
        cur_group = queue[idx]
        for cur_user in cur_group.get_users():
            if cur_user == user:
                return True
        for group in cur_group.get_groups():
            queue.append(group)
        idx +=1
    return None

print(is_user_in_group('sub_child_user', parent))
print(is_user_in_group('ray', parent))
print(is_user_in_group('bill', parent))
print(is_user_in_group('bill', g5))
print(is_user_in_group('zach', 'Zach')) # returns None if a group passed in isnt a actual Group.
print(is_user_in_group('bill', g5))
print(is_user_in_group('nina', sub_child)) # returns None, because the user lies above the passed ingroup in hierarchy.