
class Locomotive:
    def __init__(self):
        self.locomotive_name = ""
        self.conductor_name = ""
        self.fuel = 100
        self.num_linked_coach = 0
        self.total_travel_hours = 0
        self.next_coach = None
        self._init_loco_name()

    def _init_loco_name(self):
        print("Input locomotive name:")
        self.locomotive_name = input()
        print("Input conductor's name:")
        self.conductor_name = input()

    def print_info(self):
        print("coach_name:", self.locomotive_name)
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
    def __init__(self, name="", num_pass=0, next_coach=None):
        self.coach_name = name
        # passenger max = 20
        self.num_passenger = num_pass
        self.next_coach = next_coach

    def _init_name(self):
        print("Input train coach's name:")
        self.coach_name = input()

    def print_info(self):
        print("coach_name:", self.coach_name)
        print("Number of passenger:", self.num_passenger)

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


class TrainLink:
    def __init__(self):
        self.head = Locomotive()
        self.tail = None
        self.num_train_coach = 1

    def print_node(self):
        node = self.head
        while node:
            pass

    def add_node_at_end(self):
        node = self.head
        while node.next_coach:
            node = node.next_coach
        # find the last node
        node.next_coach = TrainCoach()
        self.num_train_coach += 1

    def remove_node(self, order_remove_coach):
        count = 0
        node = self.head
        previous = None
        if order_remove_coach >= 2:
            while node:
                count += 1
                if count == order_remove_coach:
                    if node.num_passenger > 0:
                        print("You can not remove the coach ,because there are passenger on the train!!")
                        break
                    previous.next_coach = node.next_coach
                    break
                else:
                    previous = node
                    node = node.next_coach

        else:
            print("Tou can not remove the invalid coach!!")


class Simulator:
    def __init__(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    train_sim = Simulator()
    train_sim.run()


