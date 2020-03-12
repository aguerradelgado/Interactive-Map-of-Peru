# Alessandra Guerra Delgado
# Integration Project
# Interactive Map of Peru! Learn more than just the Geography! Culture, History, Cuisine, and Customs

#Side-Note: might make this about the most popular regions of Peru rather than all regions

print("Welcome to the VERY BEST, there is no better, AMAZING")
print("WONDERFUL, EXTRODINARY, AWARD-WINNING Interactive Map!")
print("We will be visiting the mystic country of Peru")
print("Before we Travel to Peru, let's calculate the price of your ticket.")
print("Bellow are the airport locations with flights our to Peru.")
print("1. Fort Myer's")
print("2. Tampa")
print("3. Miami")
print("4. Orlando")
start_location = int(input("Enter in the number of the airport you are flying from:"))

if start_location == 1:
    economy_ticket_price = 400
    print("You are flying out of Fort Myer's.")
elif start_location == 2:
    economy_ticket_price = 500
    print("You are flying out of Tampa")
elif start_location == 3:
    economy_ticket_price = 350
    print("You are flying out of Miami.")
else:
    economy_ticket_price = 600
    print("You are flying out of Orlando.")

print("The cost of your ticket is $" , format((economy_ticket_price), '0.2f'), sep='')

upgrade = input("Would you like to upgrade your ticket to first class for an additional charge of $200.00?")
if upgrade == 'yes':
    economy_ticket_price += 200
    print("AYE! Flying in STYLE! Your total ticket cost is now $" , format((economy_ticket_price), '0.2f'), sep='')
elif upgrade == 'no':
    print("Way to save! First class is overrated. Your total ticket cost is $" , format((economy_ticket_price), '0.2f'), sep='')
    
print("Lets fly over!Buckle up!")
print("Welcome to Peru!")
print("We are extremely excited to have you here")
print("Please select where you would like to begin your journey.")
print("Peru is separated into 24 different regions.Similar to Provinces and States.")
print("Please enter the number of the region you would like to travel to first:")
print("1. Amazonas")
print("2. Ancash")
print("3. Apurimac")
print("4. Arequipa")
print("5. Ayacucho")
print("6. Cajamarca")
print("7. Callao")
print("8. Cusco")
print("9. Huancavelica")
print("10. Huanuco")
print("11. Ica")
print("12. Janin")
print("13. La Libertad")
print("14. Cambayeque")
print("15. Lima")
print("16. Coneto")
print("17. Madre de Dios")
print("18. Pasco")
print("19. Piura")
print("20. Puno")
print("21. San Martin")
print("22. Tacna")
print("23. Tumbles")
print("24. Ucayali")

user_choice = int(input())
if user_choice == 1:
    print("Great Selection! Las Amazonas, or the Amazon, is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, known for
    #Prompt to chose from more options, Amazon tabe might be a bit different because there are not really any in-habitants. Think more wild life and envrioment
    #Fun fact about Native people that are protected from modern technology
elif user_choice == 2:
    print("Great Selection! Ancash is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 3:
    print("Great Selection! Apurimac is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 4:
    print("Great Selection! Arequipa is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 5:
    print("Great Selection! Ayacucho is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 6:
    print("Great Selection! Cajamarca is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 7:
    print("Great Selection! Callao is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 8:
    print("Great Selection! Cusco is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 9:
    print("Great Selection! Huancavelica is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 10:
    print("Great Selection! Huanuco is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 11:
    print("Great Selection! Ica is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 12:
    print("Great Selection! Junin is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 13:
    print("Great Selection! La Libertad is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 14:
    print("Great Selection! Lambayeque is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 15:
    print("Great Selection! Lima is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 16:
    print("Great Selection! Loneto is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 17:
    print("Great Selection! Madre de Dios is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 18:
    print("Great Selection! Pasco is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 19:
    print("Great Selection! Piura is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 20:
    print("Great Selection! Puno is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 21:
    print("Great Selection! San Martin is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 22:
    print("Great Selection! Tacna is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 23:
    print("Great Selection! Tumbles is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
elif user_choice == 24:
    print("Great Selection! Ucayali is one of the best places to start our Journey through Peru")
    #Give a breif history about this region, average size and population, what it is known for best
    #Prompt another menu of choices: History, People, Food, Attractions, Geography, What It's Like Today, and Fun-Facts
else:
    print("Invalid input. Please chose from options 1-24:")
    int(input("Enter region number:"))
