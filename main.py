# Jeff Koss
# Date: 07/27/2023
# Class: MS548 Advanced Programming Concepts
# Professor: Jill Coddington
# Assignment: Final Project - Cellphone Tracker
# ETA: 6 hours or more

# Actual Time: 

# Notes: 
# You must install the following libraries: 
# pip install phonenumbers

# Import the packages we installed
import phonenumbers 
# Import the variable for the phone number in the other file
from myphone import number
# Import geocoder to get the location of the phone number
from phonenumbers import geocoder
# Import timezone to get timezone of number
from phonenumbers import timezone

# a variable that stores the phonumber in phonenumbers and parses it
pepnumber = phonenumbers.parse(number)

# a variable that stores the location of the phonenumber in geocoder
location = geocoder.description_for_number(pepnumber, "en")

# Prints out the location of the phonenumber
print(location)

# A variable at will parse the phone number for provider info
service_pro = phonenumbers.parse(number)

# Prints the carrier name of the phone number 
print(timezone.time_zones_for_number(service_pro))

