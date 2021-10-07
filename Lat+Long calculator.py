import mpu

print("A program that shows the distance between cities by the crow flies.")
print("by latitude and lingtitude.")
print("All values are given in km!")

print("Enter the Latitude of the first point:")
lat1=float(input())
print("Enter the Longitude of the first point:")
lon1=float(input())
print("Enter the Latitude of the second point:")
lat2=float(input())
print("Enter the Longitude of the second point:")
lon2=float(input())
dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
print(dist)
print("press ENTER to exit the program")
input()
