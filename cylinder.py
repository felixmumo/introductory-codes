# cylinder volume and surface area  
import math
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = math.pi * radius ** 2 * height
surface_area = 2 * math.pi * radius * (radius + height)
print("The volume of the cylinder is:", volume)
print("The surface area of the cylinder is:", surface_area) 