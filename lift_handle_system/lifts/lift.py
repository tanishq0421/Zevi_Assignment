class Lift:
    def __init__(self, num_floors):
        self.curr_floor = 0
        self.state = "CLOSE"
        self.num_floors = num_floors
        
    def move_to_floor(self, dest_floor, start_floor):
        self.curr_floor = dest_floor    
        if self.curr_floor != start_floor:
            self.state = "OPEN"
        else:
            if self.state == "OPEN":
                self.state = "CLOSE"
            else:
                self.state = "OPEN"
        
        if self.state != "OPEN":
            self.state = "CLOSE"
            
    def operate(self, start_floor):
        time_taken = abs(start_floor - self.curr_floor)
        if self.state == "CLOSE":
            time_taken += 2 #time taken to opening and closing the door
        elif self.state == "OPEN":
            time_taken += 1 # time taken to closing the door    