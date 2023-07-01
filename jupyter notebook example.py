class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current <= self.top:
            self.current += 1
        else:
            pass
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current >= self.bottom:
            self.current -= 1
        else:
            pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
    def __str__(self):
        return "Current floor: {}".format(self.current)
elevator = Elevator(-1, 10, 0)
elevator.up()
print(elevator.current)
elevator.down()
print(elevator.current)
elevator.go_to(10)
print(elevator.current)
elevator.up()
print(elevator.current)
elevator.down()
print(elevator.current)
elevator.go_to(-1)
print(elevator.current)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current)
elevator.go_to(5)
print(elevator)

