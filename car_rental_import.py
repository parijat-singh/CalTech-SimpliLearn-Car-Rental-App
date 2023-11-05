import datetime as dtm
from datetime import datetime
import math

class Car:
    '''This is class that provides info on the car'''

    #define a constructor
    def __init__(self, id,year, make, model,rental_status):
        self.id = id
        self.year = year
        self.make = make
        self.model = model
        self.rental_status = rental_status

    #define a method for displaying inventory
    def print_inv(self):
        print('Car ID:',self.id,)
        print('Year:',self.year,)
        print('Make:',self.make)
        print('Model:',self.model)
        print('Rental Status:', self.rental_status)
        print('---------------------')
       
    #define a method to rent the car
    def rentcar(self,c,cr_rental_period,transaction_timestamp,cust_name):
        #update car inventory for the car rented
        #print('in method',c,cr_rental_period,transaction_timestamp,cust_name)
        selected_car = [car_inventory[c][0],car_inventory[c][1],car_inventory[c][2],car_inventory[c][3],car_inventory[c][4]]
        car_inventory.pop(c)
        car_inventory[c] = [selected_car[0],selected_car[1],selected_car[2],selected_car[3],'Y',cr_rental_period,transaction_timestamp]
        #provide rental details to the customer
        print('Rented Car Details')
        print('------------------')
        print('Car Year, Make and Model:',selected_car[1],selected_car[2],selected_car[3])
        if cr_rental_period == '1':
            print('Rental Type: Hourly')
            print('Hourly Rate: $5 per hour')
        if cr_rental_period == '2':
            print('Rental Type: Weekly')
            print('Hourly Rate: $600 per Week')
        if cr_rental_period == '3':
            print('Rental Type: Monthly')
            print('Hourly Rate: $2400 per month')
        print('Thank you',cust_name, 'for renting a car with us. Have a safe Drive!')
    
    #method to return the car
    def returncar(self,c):
        #update car_inventory
        selected_car = [car_inventory[c][0],car_inventory[c][1],car_inventory[c][2],car_inventory[c][3],car_inventory[c][4]]
        car_inventory.pop(c)
        car_inventory[c] = [selected_car[0],selected_car[1],selected_car[2],selected_car[3],'N','','']
        
        

class Customer:
    '''This is class that provides info on the customer'''

    #define a constructor
    def __init__(self,cust_name):
        self.cust_name = cust_name
    
    #method to print the bill for the customer
    def printbill(self,c):
        date_format = '%Y-%m-%d %H:%M:%S.%f'
        print('Customer copy of the Car Rental Bill')
        #print(c)
        #print(car_inventory[c][6])
        print('------------------------------------')
        print('Thank you for Renting with us')
        print('Customer Name:', self.cust_name)
        rental_start = datetime.strptime(car_inventory[c][6], date_format)
        print('Rental start Date:',rental_start.strftime("%x"))
        print('Rental start Time:',rental_start.strftime("%X"))
        rental_end = datetime.strptime(str(dtm.datetime.now()),date_format)
        print('Rental end Date:',rental_end.strftime("%x"))
        print('Rental end Time:',rental_end.strftime("%X"))
        time_difference = rental_end - rental_start
        if car_inventory[c][5] == '1':
            num_hrs = math.ceil(time_difference.total_seconds() / 3600)
            print('Rental Type: Hourly')
            print('Number of Hours Rented:',num_hrs)
            print('Hourly Rate: $5 per hour')
            print('Total amount due $',5*num_hrs)
        if car_inventory[c][5] == '2':
            num_weeks = math.ceil(time_difference.total_seconds() / (7*24*3600))
            print('Rental Type: Weekly')
            print('Number of Weeks Rented:',num_weeks)
            print('Hourly Rate: $600 per Week')
            print('Total amount due $',600*num_weeks)
        if car_inventory[c][5] == '3':
            num_mon = math.ceil(time_difference.days / 30.44)
            print('Rental Type: Monthly')
            print('Number of Months Rented:',num_mon)
            print('Hourly Rate: $2400 per month')
            print('Total amount due $',2400*num_mon)
        print('------------------------------------')
        print('')
        print('Please pay the amount Due to complete transaction')

# Car Inventory Data Dictionary
car_inventory = {
            #'car#' : 'year', 'make','model','rental_status','rental Period', 'renting Timestamp'
            "car1" : ['1','2023', 'Ford', 'Mustang', 'N','', ''],
            "car2" : ['2','2022', 'Toyota', 'Camry', 'N','', ''],
            "car3" : ['3','2021', 'Nissan', 'Maxima','Y', '1', '2023-11-02 20:41:58.629443'],
            "car4" : ['4','2022', 'Toyota', 'Camry', 'N','', ''],
            "car5" : ['5','2023', 'Toyota', 'Camry', 'N','', ''],
            "car6" : ['6','2020', 'Toyota', 'Corolla', 'N','', ''],
            "car7" : ['7','2021', 'Ford', 'Fusion', 'N','', ''],
            "car8" : ['8','2022', 'Nissan', 'Altima','Y', '1', '2023-11-03 20:41:58.629443'],
            "car9" : ['9','2023', 'Dodge', 'Charger','Y', '2', '2023-10-26 20:41:58.629443'],
            "car10" : ['10','2020', 'Kia', 'Sorento','Y', '3', '2023-09-02 20:41:58.629443'],

            
}
#print(car_inventory["car1"])

#Function to Display the Main menu. If customer enters invalid choice, it persists with the choices until customer enters a valid input
def mainmenu() :
    choice = True
    while choice:
        user_inp = input('Please pick the number from the menu. 1.Display Inventory,2. Rent a car, 3. Return car, 4. Exit')
        if user_inp in ['1', '2','3','4']:
            choice = False
    return user_inp

#Function to get the ID of the car for Renting. 
def get_car_id_rent() :
    choice = True
    car_id = []
    while choice:
        user_inp = input('Please pick the ID of the car you would like to rent')
        # Get a List of all CAR ID's
        for c in car_inventory:
            car_id.append(car_inventory[c][0])
        if user_inp in car_id:
            choice = False
    return user_inp

#Function to get the ID of the car for returning. 
def get_car_id_return() :
    choice = True
    car_id = []
    while choice:
        user_inp = input('Please pick the ID of the car you would like to return')
        for c in car_inventory:
            car_id.append(car_inventory[c][0])
        if user_inp in car_id:
            choice = False
    return user_inp

#Function to get the user input for Rental type
def get_rental_period() :
    choice = True
    while choice:
        user_inp = input('Enter 1 for Hourly, 2 for Weekly and 3 for Monthly')
        if user_inp in ['1', '2','3']:
            choice = False
    return user_inp
