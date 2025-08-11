
class Node:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next = None

class CarQueue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, car_number):
        new_node = Node(car_number)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Car {car_number} has entered the parking.")
            return
        self.rear.next=new_node
        self.rear=new_node
        print(f"Car {car_number} has entered the parking.")

   
    def dequeue(self):
        if self.front is None:
            print("No cars in the parking to remove.")
            return None
        removed_car =self.front.car_number
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Car {removed_car} has exited the parking.")
        return removed_car

    def display(self):
        if self.front is None:
            print("Parking is empty.")
            return
        current = self.front
        print("Cars currently in parking (front to rear):")
        while current:
            print(f"Car {current.car_number}", end=" -> ")
            current = current.next
        print("None")

def main():
    parking = CarQueue()
    while True:
        print("\n=== Car Parking System ===")
        print("1. Car Enter")
        print("2. Car Exit")
        print("3. Display Cars in Parking")
        print("4. Exit Program")
        choice = input("Enter your choice: ")

        if choice == '1':
            car_number = input("Enter car number: ")
            parking.enqueue(car_number)
        elif choice == '2':
            parking.dequeue()
        elif choice == '3':
            parking.display()
        elif choice == '4':
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
