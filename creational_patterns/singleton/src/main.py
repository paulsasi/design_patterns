
import database

if __name__ == '__main__':
    
    db1 = database.Database(name="database1")
    print(db1)
    print(db1.get_name())

    db2 = database.Database(name="database2")
    print(db2)
    print(db2.get_name())

    db2.change_name("database3")
    print(db2)
    print(db2.get_name())
