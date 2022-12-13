# Creates a heightfield and fills it with values. Uses the Matrix class.

from matrix import Matrix
from math import pi, sin, cos, tan, exp

RAD = 180           # Represents a half angle, corresponding to pi in radiant.
PARAM_C = 1/2       # smaller values create bigger deviation of base_f from the identity function
PARAM_D = 1/2       # deviation from the sphere
ANGLE_ACCURACY = 72 # The higher the angle accuracy, the more values are calculated. It is the number of phi respectively theta values.
VALUE_ACCURACY = 3  # Accuracy of the values in number of decimals after the decimal point.

PRINT_HEIGHTFIELD = False # If set to True, prints the heightfield matrix into the console.
SAVE_HEIGHTFIELD  = True  # If set to True, saves a copy of the heightfield in a text file.
FILENAME_HF       = "heightfield1.txt" # Filename for saving.
CREATE_XYZ_FILE   = True  # If set to True, creates a xyz-file to plot the point cloud.
FILENAME_XYZ      = "test.xyz" # Filename for saving.

def get_phi(m):
    return -RAD/2 + m * (RAD / ANGLE_ACCURACY)
    
def get_theta(n):
    return n * (2*RAD / ANGLE_ACCURACY)
    
def convert_to_rad(angle):
    return angle * pi / 180
 
def base_f(phi, c):
    return pi * ((exp(phi / (RAD * c) + 1 / (2 * c)) - 1) / (exp(1/c) - 1) - 1/2) 
    
def f1(phi, c):
    return sin(base_f(phi, c))
    
def f2(phi, c):
    return -f1(-phi, c)
    
def calculate_R(phi, theta, c, d):
    return 1 + d * calculate_Rdelta(phi, theta, c)
    
def calculate_Rdelta(phi, theta, c):
    if phi == RAD/2:
        return 1
    elif phi == -RAD/2:
        return -1
    else:
        a = get_weighting(phi, theta, c)
        return a * f1(phi, c) + (1 - a) * f2(phi, c)
        
def get_weighting(phi, theta, c):
    rad_phi = convert_to_rad(phi)
    rad_theta = convert_to_rad(theta)
    return 1 / (1 + tan(rad_theta)**2 * cos(base_f(phi, c))**2 / cos(base_f(-phi, c))**2)
    #return (cos(rad_theta)**2 * (1 - f1(phi, c)**2))   /   (cos(rad_theta)**2 * (1 - f1(phi, c)**2) + sin(rad_theta)**2 * (1 - f2(phi, c)**2))

heightfield1 = Matrix(ANGLE_ACCURACY, ANGLE_ACCURACY)
if CREATE_XYZ_FILE: point_cloud1 = Matrix(ANGLE_ACCURACY**2, 3)
for m in range(len(heightfield1)):
    for n in range(len(heightfield1[m])):
        radius = calculate_R(get_phi(m), get_theta(n), PARAM_C, PARAM_D)
        heightfield1[m][n] = round(radius, VALUE_ACCURACY)
        if CREATE_XYZ_FILE:
            phi = convert_to_rad(get_phi(m))
            theta = convert_to_rad(get_theta(n))
            #radius = 1
            point_cloud1[m * len(heightfield1) + n][0] = round(radius * cos(theta) * cos(phi), VALUE_ACCURACY) # x coordinate for point
            point_cloud1[m * len(heightfield1) + n][1] = round(radius * sin(theta) * cos(phi), VALUE_ACCURACY) # y coordinate for point
            point_cloud1[m * len(heightfield1) + n][2] = round(radius * sin(phi) , VALUE_ACCURACY)           # z coordinate for point

if PRINT_HEIGHTFIELD:
    print("Values for theta, ranging from 0 to 2*pi:".center(ANGLE_ACCURACY * (VALUE_ACCURACY + 3) + (ANGLE_ACCURACY - 1)))
    print("\n")
    heightfield1.fprint()
    print("\n")
    print("Side values are for phi, ranging from -pi/2 to pi/2.".center(ANGLE_ACCURACY * (VALUE_ACCURACY + 3) + (ANGLE_ACCURACY - 1)))
    
if SAVE_HEIGHTFIELD:
    f = open(FILENAME_HF, 'w')
    f.write(str(heightfield1))
    f.close()
    
if CREATE_XYZ_FILE:
    f = open(FILENAME_XYZ, 'w')
    f.write(str(point_cloud1))
    f.close()
