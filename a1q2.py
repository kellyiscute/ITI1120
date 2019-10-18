def in_out(xs,ys,side):
    qx = float(input('Enter a number for the x coordinate of a query point: '))
    qy = float(input('Enter a number for the y coordinate of a query point: '))

    print(qx <= xs+side and qx >= xs and qy <= ys+side and qy >= ys)

