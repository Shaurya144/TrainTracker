# in this code we ask the user whether they want to see ariving or departing trains.
# THen show them the details of 5 trains at a time,
# including the arriving or departing time of each train and the platform they are leaving from/arriving at
# Repaeat until the user says no or there are no more trains to show
# Include sufficient validationa exception handling
# 'Constants' used for the filename provided and the station
FILENAME = "trainTimes.txt"
HOMESTATION = "King's Cross" # this is where they are currently

def parse_file():

    fileContents = []

    try:
        file = open(FILENAME,"r")
    except:
        print("File could not be opened.")
        # End the function early by returning
        return fileContents

    # If no exception was raised, you can parse the file.
    for line in file:

        line = line.strip()
        lineList = line.split(",")

        # Delete the last 'item' of each record, which is empty ("").
        del lineList[-1]
            
        fileContents.append(lineList)

    try:
        file.close()
    except:
        print("File may not have been closed.")
    
    # Remove the header row
    del fileContents[0]
    
    return fileContents

def is_file_valid(allTrains):
    # Perform some checks in case the file was abnormal.
    
    if len(allTrains) == 0:
        return False
    
    # Should have 5 fields
    elif len(allTrains[0]) != 5:
        return False
    
    # The platform number should be a number!
    elif allTrains[0][0].isdigit() == False:
        return False
    
    else:
        # Otherwise, it's probably safe to continue
        return True

# This returns the list of either the departing or arriving trains
def get_trains(allTrains, category):

    filteredTrains = []

    for train in allTrains:

        departureStation = train[1]
        arrivalStation = train[2]

        if category == "d":

            if departureStation == HOMESTATION:
                filteredTrains.append(train)

        elif category == "a":

            if arrivalStation == HOMESTATION:
                filteredTrains.append(train)

    return filteredTrains
                
# This prints the formatted details of a particular train
def print_details(i, j, trains, category):

    trainList = trains[i + j]
    
    platformNum = trainList[0]
    departureStation = trainList[1]
    arrivalStation = trainList[2]
    departureTime = trainList[3]
    arrivalTime = trainList[4]
    
    if category == "d":

        print("The train to "+arrivalStation+" is departing platform "+platformNum+" at "+departureTime+".")

    if category == "a":
        
        print("The train from "+departureStation+" is arriving at platform "+platformNum+" at "+arrivalTime+".")
        
       
# This asks the user whether they want departing or arriving trains and then shows these to them
def user_selection(allTrains):

    category = input("Enter D to view Departures and A to view Arrivals. ").lower()

    while category != "d" and category != "a":
        print("That wasn't valid.")
        category = input("Enter D to view Departures and A to view Arrivals. ").lower()

    trains = get_trains(allTrains, category)

    isDone = False

    # Prepare to loop for as many trains as there are
    for i in range(len(trains)):

        # For every 5 trains...
        if i % 5 == 0:

            print()
            
            for j in range(5):

                # ...try to print out their details using i and j 
                try:
                    print_details(i, j, trains, category)

                # If the list goes out of range, then there are no more trains and the loop can end
                except IndexError:
                    print("There are no more trains to show.")
                    isDone = True
                    break

            print()

            # As long as there are more trains to print, ask the user if they want to see more.
            if not isDone:
                selection = input("Do you want to see more? Y or N? ").lower()

                while selection != "y" and selection != "n":
                    print("That wasn't valid.")
                    selection = input("Do you want to see more? Y or N? ").lower()

                if selection == "n":
                    print()
                    break
            else:
                break
        

# Main program

# Load in file
trainDetails = parse_file()

# Check the file is (roughly) in the format expected
isValid  = is_file_valid(trainDetails)

if isValid:
    # Get the user's choice of mode
    user_selection(trainDetails)
else:
    print("\nThis file doesn't appear to be valid.")
    print("Please double check the",FILENAME,"file is correct.")

print("Thank you for using this program.")
    


