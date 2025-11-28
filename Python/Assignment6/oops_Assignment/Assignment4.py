# Create a class that captures airline tickets. 
# 	Each ticket lists the departure and arrival 
# cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter 
# for the seat within the row (such as 12F). 
# Make two examples of tickets.

class Airline_Ticket:
    
    def __init__(self,departure,arrival,flight_num,seatRow, seatletter):
        self.departure=departure
        self.arrival=arrival
        # self.cities=cities
        self.flight_num=flight_num
        self.SeatRow=seatRow
        self.SeatLetter=seatletter
        # self.seat_assig=seat_assig
    
    
    def seatArrangement(self):
        return self.SeatRow, self.SeatLetter
    
    
    def displayTicket (self):
        return f"Departure: {self.departure}  Arrival: {self.arrival}  Flight_Num: {self.flight_num}  Seat_Arrangement: {self.seatArrangement()}"
        
        
    
# class Seat_Arrangement:
    
#     def __init__ (self,row,letter):        
#         self.row=row
#         self.letter= letter
    
    
    
    
def main():
    ticket1 =Airline_Ticket("Pune","Nagpur",55555,14,"H")
    print(ticket1.displayTicket())
  
if __name__ == '__main__':
    main()