import numpy as np

studentID=[7.0,9.0,0.0,8.0,2.0,9.0,7.0,8.0,1.0]
A=studentID[7]
B=studentID[8]

deg = np.array([0,30,60,90,120,150,180,210,240,270,300,330])
rad = np.radians(deg)

# Each index corresponds to r(theta)
data = [70.0,52.0,36.0+A,20.0+B,24.0,37.0,49.0,52.0,69.0,75.0,84.0,74.0]

# The function to be "integrated" to determine the area.
def f(r):
    return 0.5*(data[r])**2

def simpsons_approx(f,data,a,b,n):
    dtheta = (b-a)/n
    if n%2 == 0:
        est = f(0)
        for i in range(1,n-1):
            if i%2 == 1:
                est = est + 4*f(i)
            if i%2 == 0:
                est = est + 2*f(i)
        est = est + f(0)
        est = est*(dtheta/3.0)
        return est
    else:
        print("n must be an even value for Simpson's Rule approximations.")

area = simpsons_approx(f,data,0.0,2.0*np.pi,len(data))

print(np.round(area,1)) # Returns 8258.2 square somethings
