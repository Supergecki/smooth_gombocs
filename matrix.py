# Creates a Matrix class inheriting from the list class.
# Matrices are initiated with m columns and n rows and all cells set to 0.

class Matrix(list):
    def __init__(self, m, n):
        list.__init__([])
        self.m = m
        self.n = n
        self.columns = self.m
        self.rows = self.n
        for i in range(m):
            self.append([0] * n)
            
    def formatted_print(self, rjust=6):
        for m in self:
            string_row = ""
            for i in m:
                string_row += str(i).rjust(rjust) + " "
            print(string_row)
            
    def fprint(self, rjust=6):
        self.formatted_print(rjust)
        
    def __str__(self, rjust=6):
        full_string = ""
        for m in self:
            string_row = ""
            for i in m:
                string_row += str(i).rjust(rjust) + " "
            full_string += string_row + "\n"
        return full_string

if __name__ == "__main__":    # Small testing Matrix.
    m1 = Matrix(3,4)
    m1[0][0] = 12
    m1[2][2] = 72
    print(str(m1))
    print(m1.m, m1.n, m1.columns, m1.rows)
