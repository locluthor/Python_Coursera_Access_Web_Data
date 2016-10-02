import re

def computeSum( filename ) :
	sum = 0;
	fileContent = open(filename, "r");
	
	digits = re.findall("[0-9]+", fileContent.read());
	
	for number in digits :
		sum += int(number);
	
	return sum;
	
	
# print computeSum("regex_sum_42.txt");
print computeSum("regex_sum_323661.txt");