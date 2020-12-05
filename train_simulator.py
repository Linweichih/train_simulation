class Locomotive:
    def __init__(self):
        self.locomotive_name = ""
        self.conductor_name = ""
        self.fuel = 100
        self.num_linked_coach = 0
        self.total_travel_hours = 0
        # self.next_coach = None
        self._init_loco_name()

    def _init_loco_name(self):
        print("Input locomotive name:")
        self.locomotive_name = input()
        print("Input conductor's name:")
        self.conductor_name = input()

    def print_info(self):
        print("Locomotive Name:", self.locomotive_name)
        print("Conductor Name:", self.conductor_name)
        print("Remaining Fuel:", self.fuel, "uints")
        print("Number of linked coach", self.num_linked_coach)

    def drive_train(self, travel_hours):
        if travel_hours * 10 > self.fuel:
            print("Fuel is not enough for traveling ", travel_hours, "hours")
        else:
            self.total_travel_hours += travel_hours
            self.fuel -= travel_hours * 10
            print("Totall traveling hours:", self.total_travel_hours)
            print("Remaining fuel:", self.fuel)

    def fill_fuel(self):
        self.fuel = 100
        print("Remaining Fuel:", self.fuel, "uints")


class TrainCoach:
    def __init__(self, name="", num_pass=0, next_coach=None):
        self.coach_name = name
        # passenger max = 20
        self.num_passenger = num_pass
        self.next_coach = next_coach
        self._init_name()

    def _init_name(self):
        print("Input train coach's name:")
        self.coach_name = input()

    def print_info(self):
        print("coach_name:", self.coach_name)
        print("Number of passenger:", self.num_passenger)

    def get_on(self):
        print("How many passenger want to get on coach", self.coach_name)
        num_passenger = int(input())
        if self.num_passenger + num_passenger > 20:
            print("Too many passenger want to get on coach!!")
            self.num_passenger = 20
        else:
            self.num_passenger += num_passenger
            print("Coach", self.coach_name, "get on ", num_passenger, "passengers")

    def get_off(self):
        print("How many passenger want to get off coach", self.coach_name)
        num_passenger = int(input())
        if self.num_passenger - num_passenger < 0:
            print("It is not make sense for so many passenger get off the coach")
        else:
            self.num_passenger -= num_passenger
            print("Coach", self.coach_name, "get off ", num_passenger, "passengers")


class TrainLink:
    def __init__(self):
        self.head = Locomotive()
        self.tail = None

    def print_node(self):
        self.head.print_info()
        print("=============================")
        node = self.tail
        while node:
            node.print_info()
            print("=============================")
            node = node.next_coach

    def add_node_at_end(self):
        if not self.tail:
            self.tail = TrainCoach()
            self.head.num_linked_coach += 1
            return
        node = self.tail
        while node.next_coach:
            node = node.next_coach
        # find the last node
        node.next_coach = TrainCoach()
        self.head.num_linked_coach += 1

    def get_on_train(self):
        node = self.tail
        while node:
            node.get_on()
            node = node.next_coach

    def get_off_train(self):
        node = self.tail
        while node:
            node.get_off()
            node = node.next_coach

    def remove_node(self, order_remove_coach):
        count = 1
        node = self.tail
        previous = None
        if order_remove_coach == 2:
            self.tail = self.tail.next_coach
            self.head.num_linked_coach -= 1
            return
        elif order_remove_coach > 2:
            while node:
                count += 1
                if count == order_remove_coach:
                    if node.num_passenger > 0:
                        print("You can not remove the coach ,because there are passenger on the train!!")
                        return
                    previous.next_coach = node.next_coach
                    self.head.num_linked_coach -= 1
                    return
                else:
                    previous = node
                    node = node.next_coach
            print("Could not find order", order_remove_coach, "'s train coach!!")

        else:
            print("You can not remove the invalid coach!!")


class Simulator:
    def __init__(self):
        self.train = TrainLink()
        self.command_table = ["加乘客車廂 到列車尾端。",
                              "刪除第k節車廂",
                              "顯示列車狀態 #(traversal)",
                              "行駛列車 (請輸入要開幾小時)",
                              "乘客上車 (依序輸入每個乘客車廂要上車的人數，注意容量上限)",
                              "乘客下車 (依序輸入每個乘客車廂要下車的人數，注意容量下限)",
                              "火車頭燃料補充 #(直接呼叫火車頭內的方法)"]

    def print_command_table(self):
        print("Command Table")
        for i in range(len(self.command_table)):
            print(i+1, self.command_table[i])

    def run(self):
        """
        self.train.add_node_at_end()
        self.train.print_node()
        self.train.remove_node(2)
        self.train.get_on_train()
        self.train.get_off_train()
        self.train.head.drive_train(5)
        self.train.print_node()
        self.train.head.fill_fuel()
        self.train.head.drive_train(11)
        self.train.print_node()

        """
        while True:
            self.print_command_table()
            print("Input command :")
            command = int(input())
            if command == 1:
                self.train.add_node_at_end()
            elif command == 2:
                print("which train coach you want to remove?")
                k = int(input())
                self.train.remove_node(k)
            elif command == 3:
                self.train.print_node()
            elif command == 4:
                print("How many hours you want to drive?")
                hours = int(input())
                self.train.head.drive_train(hours)
            elif command == 5:
                self.train.get_on_train()
            elif command == 6:
                self.train.get_off_train()
            elif command == 7:
                self.train.head.fill_fuel()
            else:
                break


if __name__ == '__main__':
    train_sim = Simulator()
    train_sim.run()
