# logc:
# reading from a file which has multiple names in it
# we woudl print the content of the file
# the program woudl tell us how many names there are in the list
# the program would also tell us the number of times that a name has been repeated
counter_dict = {}
with open("/Users/xoempire/Desktop/names.txt") as filey:
	line = filey.readline()
	while line:
		line = line.strip('\n')
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = filey.readline()
print(counter_dict)

