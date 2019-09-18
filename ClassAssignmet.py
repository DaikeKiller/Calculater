# x1 = input("First point in x coordinate:")
# y1 = input("First point in y coordinate:")
# x2 = input("Second point in x coordinate:")
# y2 = input("Second point in y coordinate:")
# x = input("enter the third point in x:")

def gradient(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

def line(x,x1,x2,y1,y2):
    line = gradient(x1,x2,y1,y2)*(x-x1) + y1
    return line

# print(line)


