# 1.You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

fieldLength = 92
fieldWidth = 48.8
area = fieldLength * fieldWidth
print(area)

# 2.You bought 9 packets of potato chips from a store. 
# Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
# Find out using python, how many dollars is the shopkeeper going to give you back?
potato_chips_packets = 9
per_packet_cost = 1.49
given_amount = 20

total_amount_of_packets = potato_chips_packets * per_packet_cost
amount_return_by_shopkeeper = given_amount - total_amount_of_packets
print(amount_return_by_shopkeeper)

# 3.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
area_of_square = 5.5**2
total_cost = area_of_square * 500
print("Total cost ", total_cost)

# 4.Print binary representation of number 17
print(format(17,'b'))