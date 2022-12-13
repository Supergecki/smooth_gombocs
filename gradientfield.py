# Reads a heightfield and analyzes it, creating a gradientfield.

from matrix import Matrix

VALUE_ACCURACY = 3 # Accuracy of the values in number of decimals after the decimal point.
FILENAME = "heightfield1.txt" # Filename for the file which contains the heightfield.

def load_heightfield(filename): # loads the heightfield from the given filename  
    f = open(filename, "r")
    raw_data = f.read()
    line_data = raw_data.split("\n")
    MATRIX_N = len(line_data) - 1 # fetches the n which is necessary for matrix initialisation.
    line1 = line_data[0]
    line_numbers = []
    for number in line1.split(" "):
        if number != '':
            line_numbers.append(float(number))
    MATRIX_M = len(line_numbers) # fetches the m which is necessary for matrix initialisation.
    
    heightfield = Matrix(MATRIX_M, MATRIX_N)
    for i in range(len(line_numbers)):          # initialises matrix for the first row of numbers.
        heightfield[0][i] = line_numbers[i]
        
    for j in range(len(line_data[1:])): # loads the rest of the heightfield into matrix.
        line = line_data[j]
        line_numbers = []
        for number in line.split(" "):
            if number != '':
                line_numbers.append(float(number))
        for i in range(len(line_numbers)):
            heightfield[j][i] = line_numbers[i]
    return heightfield
    
def create_gradientfield(heightfield): # creates a gradientfield from the given heightfield
    gradientfield = Matrix(heightfield.m, heightfield.n)
    hidden_southpole_value = 1 + (1 - heightfield[0][0]) # Because the R value at the southpole isn't saved for the heightfield, it is explicitly calculated here.
                                                         # (this value and the northpole value are symmetrical around 1, i.e. the sphere)
    for m in range(len(heightfield)):
        for n in range(len(heightfield[m])):
            center_value = heightfield[m][n]
            if m == 0:                    # Case at the northpole. Uses four different "south" directions to stand for north, east, south and west.
                deg90 = round(gradientfield.n / 4) # Calculates the distance between two south directions to create 90 degrees between them.
                north_value = heightfield[1][0]
                west_value = heightfield[1][deg90]
                south_value = heightfield[1][2 * deg90]
                east_value = heightfield[1][3 * deg90]
            elif m == len(heightfield)-1: # North, east and west steps are normal. Because there is no saved southern value, the hidden southpole value is used.
                north_value = heightfield[m-1][n]
                west_value = heightfield[m][n-1]
                south_value = hidden_southpole_value
                if n == len(heightfield[m])-1: east_value = heightfield[m][0]
                else:                          east_value = heightfield[m][n+1]
            else:                         # Normal case. Goes a step into north, east, south and west direction.
                north_value = heightfield[m-1][n]
                west_value = heightfield[m][n-1]
                south_value = heightfield[m+1][n]
                if n == len(heightfield[m])-1: east_value = heightfield[m][0]
                else:                          east_value = heightfield[m][n+1]
            north_to_center = round(north_value - center_value, VALUE_ACCURACY)
            west_to_center = round(west_value - center_value, VALUE_ACCURACY)
            center_to_south = round(center_value - south_value, VALUE_ACCURACY)
            center_to_east = round(center_value - east_value, VALUE_ACCURACY)
            gradientfield[m][n] = (north_to_center, west_to_center, center_to_south, center_to_east)
    return gradientfield
    
def analyze_gradientfield(gradientfield): # Analyzes a given gradientfield, finding local maxima and minima and filling in arrows to show the gradient directions.
    analyzed_gradientfield = Matrix(gradientfield.m, gradientfield.n) # Tries to find local maxima, i.e. where: north_to_center and west_to_center are positive; center_to_south and center_to_east negative OR
    for m in range(gradientfield.m):                                  # Tries to find local minima, i.e. where: north_to_center and west_to_center are negative; center_to_south and center_to_east positive
        for n in range(gradientfield.n):
            if gradientfield[m][n][0] > 0 and gradientfield[m][n][1] > 0 and gradientfield[m][n][2] < 0 and gradientfield[m][n][3] < 0: # Found a local maximum.
                analyzed_gradientfield[m][n] = "O" # O will be the sign for local maxima because all "sides" of it go outwards.
            elif gradientfield[m][n][0] < 0 and gradientfield[m][n][1] < 0 and gradientfield[m][n][2] > 0 and gradientfield[m][n][3] > 0: # Found a local minimum.
                analyzed_gradientfield[m][n] = "X" # X will be the sign for local minima because all "sides" of it go inwards.
            else: # No local extremum found at this point. Looking for the biggest gradient in a direction to draw an arrow towards.
                biggest_gradient = max(-gradientfield[m][n][0], -gradientfield[m][n][1], gradientfield[m][n][2], gradientfield[m][n][3])
                direction_number = (-gradientfield[m][n][0], -gradientfield[m][n][1], gradientfield[m][n][2], gradientfield[m][n][3]).index(biggest_gradient)
                if direction_number == 0: analyzed_gradientfield[m][n] = "^"
                elif direction_number == 1: analyzed_gradientfield[m][n] = "<"
                elif direction_number == 2: analyzed_gradientfield[m][n] = "v"
                elif direction_number == 3: analyzed_gradientfield[m][n] = ">"                
    return analyzed_gradientfield

heightfield1 = load_heightfield(FILENAME)   
#heightfield1.fprint() # Test
gradientfield1 = create_gradientfield(heightfield1)
#gradientfield1.fprint() # Test
analyzed_gradientfield1 = analyze_gradientfield(gradientfield1)
analyzed_gradientfield1.fprint(rjust=1)
