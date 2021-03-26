n = int(input())
reservations = set()
guests_arrived = set()

for _ in range(n):
    current_reservation = input()
    reservations.add(current_reservation)

command = input()
while command != "END":
    guests_arrived.add(command)
    command = input()

not_arrived_guest = sorted(reservations - guests_arrived)
print(len(not_arrived_guest))
[print(guest) for guest in not_arrived_guest if guest[0].isdigit()]
[print(guest) for guest in not_arrived_guest if not guest[0].isdigit()]