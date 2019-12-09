import json
with open("template_update.json", "r") as config_file:
  config = json.load(config_file)

def menu():
    print "Press 1: To view list of activities. "
    print "Press 2: To Update templates. "
    print "Press 3: To quit the program. "
    return int(input("What would you like to do? "))

choice = menu()

while True:
    if choice == 1:
        print config
        
        choice = menu()

    elif choice == 2:
        changestring= input('Template to be changed? ')
        # changestring = 'click-words-to-popout,status:true'
        keyval = changestring.split(':')
        print keyval
        keys = keyval[0].split(',')
        vals = keyval[1]
        
        # Move our "pointer"
        obj = config
        for key in keys[:-1]:
            try: obj = obj[key]
            except TypeError:
                 # Probably want a more general solution
                obj = obj[int(key)]
                
         # Update value       
        obj[keys[-1]] = vals

        with open("template_update.json", "w") as config_file:
            json.dump(config, config_file, indent=4)
        

        
        choice = menu()

       
   
    elif choice == 3:
        break


with open("template_update.json", "w") as config_file:
     json.dump(config, config_file, indent=4)
#   config_file.write(json.dumps(config))
