# -----------------------------------------------------------------------------#
# Title: Assignment 07
# Description: Working with Error Handling and Pickling
# ChangeLog (Who,When,What):
# JNussb,5.30.2022,Created started script
# ------------------------------------------x-----------------------------------#

# ---------------Import Pickle ---------------#
import pickle  # Imports pickle module to retrieve binary data

# --------------- Data ---------------#snip
# Pickled Objects cannot be stored as text, they must be saved as a binary file, note the .dat
strPickleFile = 'Range.dat'
firPickle = ''

# --------------- Processing ---------------#
def save_data_to_file(pickle_file, list_of_data): #saving data to binary data file
    file = open(pickle_file, "wb")  # Note the b at the end of wb, it must be added when working w/ a binary file
    pickle.dump(list_of_data, file)
    # This references the pickle module and the .dumb function stores the data into our binary pickle file
    file.close()

def read_data_from_file(pickle_file): # reading data from binary data file.
    file = open(pickle_file, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

# --------------- Presentation ---------------#

# Using raised an exception for structured error handling.
# Try block raises a ValueError exception if outside the allowed range.
try:
    x = int(input('Enter a number up to 100: '))
    if x > 100:
        raise ValueError(x)

    save_data_to_file(strPickleFile, firPickle)
    print(read_data_from_file(strPickleFile))

except ValueError:
    print(x, "is out of allowed range")
    print("Please choose an acceptable number within range next time\n")

else:
    print(x, "is within the allowed range")