from ..EngineVehicle import EngineVehicle

class Car(EngineVehicle):
    def start_engine(self):
        print("Car-specific engine starting logic")

    def move(self):
        print("Movement logic")
