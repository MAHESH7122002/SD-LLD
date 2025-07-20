from .Vehicle import Vehicle

class NonEngineVehicle(Vehicle):
    def move(self):
        print("Non-Engine Vehicles do not have start engine method")
