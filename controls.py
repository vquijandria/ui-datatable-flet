#In this file we create a few lines of code to map and keep
#note of the class instances. This will allow us to easily
#access each instance when we need to change something

global control_reference
control_reference = {}


#This function will add the key and value to the dict
def add_to_control_reference(key, value):
    global control_reference
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

#we can create another function that returns the dict

def return_control_reference():
    global control_reference
    return control_reference