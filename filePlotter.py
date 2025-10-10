# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import math
import numpy as np
import matplotlib.pyplot as plt
from utilities import FileReader

def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file() 
    time_list=[]
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append((val[-1] - first_stamp) / 1e9) # convert to seconds

    for i in range(0, len(headers) - 1):
        plt.plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")

    plt.title(f"Sensor Data Plot: {filename}")

    plt.xlabel("Time [s]")
    plt.ylabel("Sensor Values")
    
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    plt.legend()
    plt.grid()
    plt.show()

def plot_odom_x_y(filename): # plot x vs y from odom data
    
    headers, values=FileReader(filename).read_file() 

    xs = [row[0] for row in values] # array of x values
    ys = [row[1] for row in values] # array of y values

    # Plot the path
    plt.plot(xs, ys, label=filename, linewidth=1.6)
    # Mark start/end
    plt.scatter(xs[0], xs[0], s=0)  # harmless; prevents legend warning on empty scatter
    plt.scatter(xs[0], ys[0], s=30, marker="o", label=f"{filename} start")
    plt.scatter(xs[-1], ys[-1], s=30, marker="x", label=f"{filename} end")

    plt.title(f"Robot Trajectory (x vs y): {filename}")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_laser(filename, row_index=0): # plot laser scan for one angle
    
    headers, values = FileReader(filename).read_file()

    row = values[row_index] # select one row to plot

    ranges = np.array(row[:-2], dtype=float) # slice off the last two values to get all laser ranges
    angle_offset = float(row[-2]) # robot/sensor heading at this scan 
    _timestamp_ns = row[-1] # timestamp in nanoseconds

    n = len(ranges) # should be 360
    theta_local_deg = np.arange(n, dtype=float)  # array w values 0, 1, 2, ..., 359
    theta_local = np.deg2rad(theta_local_deg)  # convert to radians     

    theta = theta_local + angle_offset # add offset to every angle

    mask = np.isfinite(ranges) & (ranges > 0.0) # filter out invalid measurements

    r  = ranges[mask]
    th = theta[mask] 

    x = r * np.cos(th)
    y = r * np.sin(th)

    plt.figure()
    plt.scatter(x, y, s=6)
    plt.scatter([0], [0], s=40, marker='x', label='Sensor')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Laser scan (row {row_index}) — {filename}")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


    
import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    for filename in filenames:
        plot_errors(filename)
        #plot_odom_x_y(filename)
        #plot_laser(filename, row_index=0)
