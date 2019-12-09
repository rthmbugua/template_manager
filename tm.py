import json
import sys

if len(sys.argv) < 2:
	exit("Usage: $ python tm.py <subject>")

subject = sys.argv[1]


def convert(infile = "subgroups", outfile = "kiswahili.json"):
	jsonstring = ''

	with open(infile, "r") as file:
		for line in file:
			jsonstring += line

	jsonstring = jsonstring.replace("\'", "\"")

	data = json.loads(jsonstring)
	new_data = {}

	for key in data:
		new_data[key] = {}
		new_data[key]['status'] = False
		new_data[key]['activities'] = data[key]

	with open(outfile, "w") as file:
		json.dump(new_data, file)


def loadData(subject):
	with open(subject + ".json") as file:
		dt = json.load(file)
		file.close()
	return dt

data = loadData(subject)
# list all activities
def listActivities():
	for key in data:
		status = 'done' if data[key]['status'] else 'xxxx'
		print("{}      {}             :  {}".format(len(data[key]['activities']), status, key))

# while True:
# 	# print available choices
# 	print "1. List of Activities"
# 	print "2. Update activity status"

# 	choice = int(input("Enter command: "))

# 	if choice == 1:
# 		listActivities()
# 	elif choice == 2:
# 		updateBehaviour = input("Enter behaviour to update: ")
# 		updateStatus = input("Enter status: ")
# 	else:
# 		print"You must enter a command"
	    

		
