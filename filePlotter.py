# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

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

def plot_odom_x_y(filename):
    
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
    plt.axis("equal")      # preserve geometry
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
        #plot_errors(filename)
        plot_odom_x_y(filename)
