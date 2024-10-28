# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
#  Converts input shape and operation count of fully-connected layer into output.
# Parameters:
#  c_in: input channel count
#  n_wv: number of weight vectors

# Output:
#  Output shape and operation count of a fully-connected layer.
#
# Written by Matthew Moore
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_out = float('nan')
h_out = float('nan')
w_out = float('nan')
adds = 0.0
muls = 0.0
divs = 0.0

# parse script arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])
else:
    print('Usage: python3 full_ops.py c_in n_wv')
    exit()

# write script below this line
c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv * c_in
muls = n_wv * c_in

# script output
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))
