
class Locomotive:
    def __init__(self):
        self.coach_name = ""
        self.conductor_name = ""
        self.fuel = 0
        self.num_linked_coach = 0
        self.total_travel_hours = 0

    def print_info(self):
        print("coach_name:", self.coach_name)
        print("Conductor Name:", self.conductor_name)
        print("Current Fuel:", self.fuel, "uints")
        print("Number of linked coach", self.num_linked_coach)

    def drive_train(self, travel_hours):
        if travel_hours * 10 > self.fuel:
            print("Fuel is not enough for traveling ", travel_hours, "hours")
        else:
            self.total_travel_hours += travel_hours
            self.fuel -= travel_hours*10
            print("Totally traveling hours:", self.total_travel_hours)
            print("Remaining fuel:", self.fuel)

    def fill_fuel(self):
        self.fuel = 100
        print("Current Fuel:", self.fuel, "uints")


class TrainCoach:
    def __init__(self):
        self.coach_name = ""
        # passenger max = 20
        self.num_passenger = 0

    def get_on(self, num_passenger):
        if self.num_passenger + num_passenger > 20:
            print("Too many passenger want to get on coach!!")
            self.num_passenger = 20
        else:
            self.num_passenger += num_passenger
        print("Coach", self.coach_name, "get on ", num_passenger, "passengers")

    def get_off(self, num_passenger):
        if self.num_passenger - num_passenger < 0:
            print("It is not make sense for so many passenger get off the coach")
            self.num_passenger = 20
        else:
            self.num_passenger -= num_passenger
        print("Coach", self.coach_name, "get off ", num_passenger, "passengers")


class Simulator:
    def __init__(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    train_sim = Simulator()
    train_sim.run()


