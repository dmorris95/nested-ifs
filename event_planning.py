#Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room" 
print(venue)


#Task 2

additional_facilities = "audio system" if attendees > 150 else "shout louder"
additional_facilities += " and projector" if attendees > 200 else " and powerpoint"
print(additional_facilities)


#Task 3

food = input("Would you like vegetarian food? yes or no:")
caterer = "Veggie Delight Caterers" if food == "yes" else "Gourmet Meals Caterers"
print(caterer)