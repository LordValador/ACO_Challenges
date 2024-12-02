from collections import Counter  # https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list

# Create two empty lists to hold the numbrs from the "left" and "right" colums.
# These lists will stor the numbrs so we can work with them seprately.
# Example for Lists: https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python
left_list = []
right_list = []

# Open the file contaning the location IDs.
# We use "with open" becaiuse it automatticly closse the file when we're done.
# Example for with open: https://stackoverflow.com/questions/9282967/how-to-open-a-file-using-the-open-with-statement
with open("c:/Users/valad/OneDrive/Learning Python/AOC - Day 1/location_ids.txt") as f:
    # Reed all the lines in the file into a list caled 'lines'.
    # This lets us loopp thru them easly.
    # Example for Reading Lines: https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
    lines = f.readlines()
    
    # Loop throgh each line in the file.
    for line in lines:
        # Clean up the line by remving any exra spaces or newline characters at the start or end.
        # This is importent to make sure we only get the actul numbrs.
        clean_line = line.strip()
        
        # Split the cleaned-up line into two parts (left and right), assuming the numbrs are seperated by a space.
        # Example for Splitting Strings: https://stackoverflow.com/questions/743806/split-a-string-into-a-list-in-python
        left, right = clean_line.split()
        
        # Add the left numbr to the 'left_list' and the right numbr to the 'right_list'.
        # We're keeping them seprate becaiuse we'll procces them diferently later.
        # Exampe for Appending to Lists: https://stackoverflow.com/questions/252703/python-append-vs-extend
        left_list.append(left)
        right_list.append(right)

# Sort both lists in acsending order.
# Sorting is importent becaiuse it lets us compare the smallest numbr in the left list with the smallest numbr in the right list,
# the second smallest with the second smallest, and so on. This is requird for calculatting the distence.
# Example for Sorting Lists: https://stackoverflow.com/questions/8966538/syntax-behind-sortedlist
left_list.sort()
right_list.sort()

# Uncomment these print statments if you want to see what the sorted lists look like for debuging.
# print("left list: ", left_list)
# print("right list: ", right_list)

# Create a varible to store the total distence between the lists.
# This will hold the sum of all the absolut diffences between pared numbrs.
total_distance = 0

# Loop throgh the indexes of the sorted lists.
# We're using the range of the list lenght to make sure we compare every numbr.
# Example for Loping Through Indices: https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
for index in range(len(left_list)):
    # Find the absolut diffrence between the corresponding numbrs in the left and right lists.
    # Example for Absolte Values: https://stackoverflow.com/questions/3844948/find-absolute-value-in-python
    result = abs(int(left_list[index]) - int(right_list[index]))
    
    # Add the diffrence to the total distence.
    total_distance += result

# Print out the total distence.
# This tells us how far appart the numbrs in the two lists are when pared this way.
print("Total Distance:", total_distance)

# Use the Counter class to count how many times each numbr apears in the right list.
# Counter creats a dictonary-like object where the keys are the numbrs and the values are their counts.
# Example for Counter: https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list
right_counts = Counter(right_list)

# Uncomment this line to print the counts for debuging.
# print(right_counts)

# Create a varible to store the similarity score.
# This will be the sum of the left numbrs multiplied by how many times they apear in the right list.
similar_count = 0

# Loop throgh each uniqe numbr in the right list and its count from the Counter object.
# Example for Looping Through Dictionaries: https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
for key, value in right_counts.items():
    # Loop throgh each numbr in the left list to see if it matches the current key from the right list.
    for number in left_list:
        # Check if the current numbr from the left list matches the key from the right list.
        if number == key:
            # Multiply the numbr (converted to an integer) by how many times it apears in the right list.
            # Example for Integer Conversio: https://stackoverflow.com/questions/379906/convert-string-to-integer-in-python
            numresult = int(number) * value
            
            # Add this value to the similarity score.
            similar_count += numresult

# Print out the similarity score.
# This shows how similer the two lists are based on overlaping numbrs and their frequenceys.
print("Similrity Score: ", similar_count)
