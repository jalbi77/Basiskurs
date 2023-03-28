# Aufgabe 2 -----------------------------------------------------------------

import math


def bogenmass(winkel_grad):
    return (winkel_grad * math.pi) / 180


winkel_grad = float(input("Geben Sie den Winkel im Gradmass ein: "))
winkel_rad = bogenmass(winkel_grad)
print("Der Winkel in Bogenmass:", winkel_rad)

sinus = math.sin(winkel_rad)
print("Sinus des Winkels:", sinus)


# Or like this:

# # Define radius function
# def bogenmass(a):
#     # Convert angle in degrees to radians
#     winkel_bogenmass = (a * 2 * math.pi) / 360
#
#     # Convert angle in degrees to radians
#     return winkel_bogenmass
#
# # Expect input and assign to a variable
# a = int(input('Input of an angle: '))
#
# # Run function and display result on condition
# if a == 180:
#     print(a, '° is in radians: ', bogenmass(a), 'and therefore = pi')
# else:
#     print(a, '° is in radians: ', bogenmass(a))

