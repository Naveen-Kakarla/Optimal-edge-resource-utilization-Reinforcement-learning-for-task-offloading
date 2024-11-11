import os

# Example file path construction
data_name = str("%03d" % (1))  # Assuming data_num is defined
file_name = "KAIST" + "_30sec_" + data_name + ".txt"  # Assuming LOCATION is defined
file_path = "C:/Users/harih/Downloads/Resources-Allocation-in-The-Edge-Computing-Environment-Using-Reinforcement-Learning-master/Resources-Allocation-in-The-Edge-Computing-Environment-Using-Reinforcement-Learning-master/data/" + "KAIST" + "/" + file_name

print(os.path.exists(file_path))
# Print the path to see if it’s correct
print("Constructed file path:", file_path)


try:
    with open(file_path, "r", encoding="utf-8") as f:
        print(f.read())  # or perform other operations on the file
except Exception as e:
    print(f"Error opening the file: {e}")