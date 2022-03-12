
import numpy as np



# Regular or irregular spacing



# 2 pt backward looking first derivative
def b2p1d(x, y):
    out = x * 0.0
    for k in range(1, len(x)):
        out[k] = ((y[k] - y[k-1])/(x[k] - x[k-1]))
        out[0] = out[1]
    return out


# 3 point centered first derivative
def c3p1d(x, y):
    out = x * 0.0
    dx = x[1] - x[0]
    n = len(x)
    for k in range(0, n-1):
        
        out[0] = (-1*(y[2]) + 4*(y[1]) -3*(y[0])) / (2 * (dx))

        out[k] = (y[k+1] - y[k-1]) / (2*(dx))
        
        out[-1] = ((3*(y[n-1])) - (4*y[n-2]) + (y[n-3])) / (2 * (dx))
            
        
    return out

# 3 point centered second derivative
def c3p2d(x, y):
    y = y*1.0
    x = x*1.0
    out = x * 0.0
    dx = x[1] - x[0]
    for k in range(1, len(x)-1):
        out[k] = (y[k+1] + (-2*(y[k])) + y[k-1]) / ((dx)**2)
        out[-1] = out[-2]
        out[0] = out[1]  
    
    return out




# 2 point forward looking first derivative
def f2p1d(x, y):
    out = x * 0.0
    for k in range(0, len(x)-1):
        out[k] = ((y[k+1] - y[k])/(x[k+1] - x[k]))
        out[-1] = out[-2]
    return out


# Regular spacing only
# Accumulated trapezoidal rule
def trap_int(x, y):
    out = x * 0.0
    for k in range(1, len(x)):
        out[k] = out[k-1] + 1/2 * (y[k-1] + y[k]) * (x[k] - x[k-1])
    return out

# Accumulated hybrid rule
def hybrid_int(x, y):
    out = x * 0.0
    dx = x[1] - x[0]
    for N in range(1, len(x) + 1):
        if N == 1:
            out[N - 1] = 0
        elif N == 2:
            out[N - 1] = 1/2 * (y[N-2] + y[N-1]) * (dx)
        elif N == 3:
            out[N - 1] = (1/3 * (y[N-3] + 4*y[N-2] + y[N-1]) * dx)
        elif N == 4:
            out[N - 1] = (3/8*dx*(y[N-4] + 3*y[N-3] + 3*y[N-2] + y[N-1]))
        elif N%2 == 1:
            out[N - 1] = (1/3 * (y[0] + (4*y[1:N-1:2].sum()) + (2*y[2:N-2:2].sum()) + y[N-1]) * dx)
        else:
            out[N - 1] = (1/3 * (y[0] + (4*y[1:N-4:2].sum()) + (2*y[2:N-5:2].sum()) + y[N-4]) * dx) + (3/8*dx*(y[N-4] + 3*y[N-3] + 3*y[N-2] + y[N-1]))

    return out



if __name__ == "__main__":

    x = np.linspace(0, 7, 3)
    y = 4 * x ** 1 + 3 * x ** 0
    int1t = trap_int(x, y)
    int1h = hybrid_int(x, y)
    out_b2p1d1 = b2p1d(x, y)
    out_f2p1d1 = f2p1d(x, y)
    out_c3p1d1 = c3p1d(x, y)
    out_c3p2d1 = c3p2d(x, y)
    print("Trapezoidal:\n", int1t)
    print("Hybrid:\n", int1h)
    print("Actual Integral:\n", 4 * x ** 2 / 2 + 3 * x ** 1 / 1)
    print("Backward 2:\n", out_b2p1d1)
    print("Forwrard 2:\n", out_f2p1d1)
    print("Center 3:\n", out_c3p1d1)
    print("Actual Derivative:\n", 4 * x ** 0)
    print("Center 3 2nd:\n", out_c3p2d1)
    print("Actual 2nd Derivative:\n", 0 * x ** 0)

    y = 9 * x ** 2 + 6 * x ** 1 + 4 * x ** 0
    int1t = trap_int(x, y)
    int1h = hybrid_int(x, y)
    out_b2p1d1 = b2p1d(x, y)
    out_f2p1d1 = f2p1d(x, y)
    out_c3p1d1 = c3p1d(x, y)
    out_c3p2d1 = c3p2d(x, y)
    print("Trapezoidal:\n", int1t)
    print("Hybrid:\n", int1h)
    print("Actual Integral:\n", 9 * x ** 3 / 3 + 6 * x ** 2 / 2 + 4 * x / 1)
    print("Backward 2:\n", out_b2p1d1)
    print("Forwrard 2:\n", out_f2p1d1)
    print("Center 3:\n", out_c3p1d1)
    print("Actual Derivative:\n", 18 * x ** 1 + 6 * x ** 0)
    print("Center 3 2nd:\n", out_c3p2d1)
    print("Actual 2nd Derivative:\n", 18 * x ** 0)
