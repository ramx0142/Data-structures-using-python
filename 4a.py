class CarParkingQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity  

    def is_full(self):
        return len(self.queue) >= self.capacity

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, car_number):
        if self.is_full():
            print(f"Parking Full! Car {car_number} cannot enter.")
        else:
            self.queue.append(car_number)
            print(f"Car {car_number} has entered the parking.")

    def dequeue(self):
        if self.is_empty():
            print("Parking Empty! No cars to exit.")
        else:
            car_number = self.queue.pop(0)
            print(f"Car {car_number} has exited the parking.")

    def display(self):
        if self.is_empty():
            print("No cars in parking.")
        else:
            print("Cars currently in parking:")
            for car in self.queue:
                print(f" - Car {car}")



def main():
    parking_capacity = 5
    parking_lot = CarParkingQueue(parking_capacity)

    while True:
        print("\n--- Car Parking System ---")
        print("1. Car Entry (Enqueue)")
        print("2. Car Exit (Dequeue)")
        print("3. Show Cars in Parking")
        print("4. Exit Program")

        choice = input("Enter your choice (1-4): ")


        if choice == '1':
            car_number = input("Enter Car Number to park: ")
            parking_lot.enqueue(car_number)
        elif choice == '2':
            parking_lot.dequeue()
        elif choice == '3':
            parking_lot.display()
        elif choice == '4':
            print("Exiting Program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
