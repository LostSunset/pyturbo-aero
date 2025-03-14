import numpy as np
from scipy.special import comb

def bernstein_poly(i, n, t):
    """
     The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * ( t**(n-i) ) * (1 - t)**i


def bezier_curve(points, nTimes=1000):
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1], 
                 [2,3], 
                 [4,5], ..[Xn, Yn] ]
        nTimes is the number of time steps, defaults to 1000

        See http://processingjs.nihongoresources.com/bezierinfo/
    """

    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nTimes)

    polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)   ])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals

if __name__=="__main__":
    import matplotlib.pyplot as plt
    from pyturbo.helper import bezier
    control_points = np.array([(0, 0), (1, 2), (3, 1), (4, 0)])
    paht_b = bezier(control_points[:,0],control_points[:,1])
    t = np.linspace(0,1,1000)
    px,py = paht_b.get_point(t)
    
    bx,by = bezier_curve(control_points)

    # Plot the Bezier curve
    plt.plot(bx, by)
    plt.plot(px, py)
    plt.scatter(*zip(*control_points), color='red')  # Plot control points
    plt.show()