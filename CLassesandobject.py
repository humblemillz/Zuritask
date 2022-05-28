class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, change_name, change_age, add_track, get_score):
        self.change_name = change_name
        self.change_age = change_age
        self.add_track = add_track
        self.get_score = get_score
        pass


Bob = Student(change_name="Bob", change_age=26, add_track=["FE", "BE"], get_score=20.90)
""" i used this print out the bob and inspect its content
print(Bob.change_name)
print(Bob.change_age)
print(Bob.add_track)
print(Bob.get_score)"""
# Expected methods


Bob.change_name = "Peter"
Bob.change_age = 34
Bob.add_track = "UI/UX"
Bob.get_score = 0


print(Bob.change_name)
print(Bob.change_age)
print(Bob.add_track)
print(Bob.get_score)
