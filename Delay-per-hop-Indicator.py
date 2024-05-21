import random
import time

class Vehicle:
    def __init__(self, id):
        self.id = id
        self.position = 0
        self.speed = random.uniform(10, 25)  # Randomly generate speed

    def move(self):
        self.position += self.speed

    def get_position(self):
        return self.position

class VANET:
    def __init__(self, num_vehicles):
        self.vehicles = [Vehicle(i) for i in range(num_vehicles)]
        self.hop_delay_threshold = 2  # Set a lower delay threshold

    def simulate_communication_with_DPHI(self):
        sender = random.choice(self.vehicles)
        receiver = random.choice(self.vehicles)

        while sender == receiver:
            receiver = random.choice(self.vehicles)

        sender.move()
        receiver.move()

        hop_delay = abs(receiver.get_position() - sender.get_position()) / sender.speed

        if hop_delay > self.hop_delay_threshold:
            print(f"Using DPHI: Possible wormhole attack! Delay too large: {hop_delay}")
        else:
            print(f"Using DPHI: Communication normal. Delay: {hop_delay}")

    def simulate_communication_without_DPHI(self):
        sender = random.choice(self.vehicles)
        receiver = random.choice(self.vehicles)

        while sender == receiver:
            receiver = random.choice(self.vehicles)

        sender.move()
        receiver.move()

        hop_delay = abs(receiver.get_position() - sender.get_position()) / sender.speed

        print(f"Without DPHI: Communication normal. Delay: {hop_delay}")

def main():
    num_vehicles = 50  # Increase the number of vehicles
    simulation_time = 10  # Increase the number of communications

    vanet = VANET(num_vehicles)

    print("Using DPHI for communication:")
    for _ in range(simulation_time):
        vanet.simulate_communication_with_DPHI()
        time.sleep(1)

    print("\nWithout DPHI for communication:")
    for _ in range(simulation_time):
        vanet.simulate_communication_without_DPHI()
        time.sleep(1)

if __name__ == "__main__":
    main()
