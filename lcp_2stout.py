import numpy as np
from scipy.interpolate import interp1d
import sys

def beta_a_interp(type):
    a, beta = np.loadtxt("lcp_sort.dat",usecols=(0,1),unpack=True)

    if (type == "latspacing"): f_beta_a = interp1d(beta,a,kind="cubic")
    elif (type == "beta"): f_beta_a = interp1d(a,beta,kind="cubic")

    return lambda x: f_beta_a(x)

option = sys.argv[1]

if option == "-a":
    beta = float(sys.argv[2])
    a_func = beta_a_interp("latspacing")
    print("a[fm]: %.12f"%a_func(beta))
elif option == "-b":
    a = float(sys.argv[2])
    beta_func = beta_a_interp("beta")
    print("beta: %.12f"%beta_func(a))
else:
    print("Unknown option %s"%option)
