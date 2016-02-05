#give 3 ways to add 2 items to the list called class_room
	#eg. class_room = ['chair', 'projector']
	#new list: class_room = ['chair', 'projector', 'PCs', 'snacks']
#remove the item located at index 1 (can you find 3 different ways?)
#remove the item snacks

class_room = ['chair', 'projector']
class_room.append("PCs")
class_room = class_room + ["snacks", "dogs"]
class_room.extend(["computers", "water"])

print class_room