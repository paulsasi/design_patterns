class Database:

    class __Database:

        def __init__(self, name):
            self.name: str = name

        def get_name(self):
            return self.name

        def change_name(self, new_name: str):
            self.name = new_name

    instance : __Database =  None

    def __new__(cls, name: str):
        if not Database.instance:
            Database.instance = Database.__Database(name)
        else:
            Database.instance.change_name(name)
        return Database.instance


