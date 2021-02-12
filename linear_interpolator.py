# linear_interpolator.py

def return_y_value(coords1, coords2, x3):
    y3 = (((x3 - coords1[0])*(coords2[1] - coords1[1]))/(coords2[0]-coords1[0])) + coords1[1]
    return y3

if __name__ == "__main__":
    y = return_y_value((1,2), (3,4), 5)
    print(y)