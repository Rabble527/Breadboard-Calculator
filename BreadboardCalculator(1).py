
# Online Python - IDE, Editor, Compiler, Interpreter
wire_length = float(0)

rails_crossed = 0
print("Welcome to the Breadboard Wire Measurement Tool\n")
cross_gap = input("Will you cross the centre gap: \"y\" or \"n\"?")
connect_rail = input("Will you connect to a power rail: \"y\" or \"n\"?")

cross_rail = input("Will you cross over the power rail: \"y\" or \"n\"?")
if cross_rail == "y":
   wire_length += 8.92
    
    
level_height = int(input("What height level? Note base = 0\n"))
    
number_of_bends = int(input("How many bends will there be?")) #subtract 0.05 inch per bend
number_of_spaces = int(input("How many squares, including start and finish, will it cover?"))

length_of_tail = float(input("How long will each tail be in mm?"))


total_length = float(0)

wire_length += (number_of_spaces - 1) * 2.54 # Number of Spaces
print(f"A: {wire_length}")

wire_length -= (number_of_bends * 1.27) # Number of Bends
print(f"B: {wire_length}")

if level_height >= 1: # Tier Level
    wire_length += ((level_height  * 2.54) + 2.54)
else:
    wire_length += 0
print(f"C: {wire_length}")

if cross_gap == "y": # Does it cross the gap?
    wire_length += 5.08
else:
    wire_length += 0
print(f"D: {wire_length}")

if connect_rail == "y": # Does it connect to the power rail?
    wire_length += 4.46
else:
    wire_length += 0
print(f"E: {wire_length}")

total_length = round(wire_length + (length_of_tail * 2), 2) # Calculate total length

print("\n")
print(f"You need to cut {total_length}mm")
