import matplotlib.pyplot as plt
from utilities import FileReader




def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file()
    
    time_list=[]
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append((val[-1] - first_stamp) / 1e9) # convert to seconds
    
    
    fig, axes = plt.subplots(1,2, figsize=(14,6))

    # ---- Left subplot: state-space (e vs e-dot) ----
    axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    axes[0].set_title("State-Space Plot (Error vs Derivative of Error)")
    axes[0].grid(True)

    # ---- Right subplot: each individual state vs time ----
    axes[1].set_title("Each Individual State vs Time")
    axes[1].set_xlabel("Time [s]")
    axes[1].set_ylabel("State Value")


    axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    axes[0].grid()

    if "angular" in filename:
        axes[0].set_xlabel("Error (rad)")
        axes[0].set_ylabel("Error Derivative (rad/s)")
        for i in range(0, len(headers) - 1):
            axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i]+ " angular")
    else:
        axes[0].set_xlabel("Error (m)")
        axes[0].set_ylabel("Error Derivative (m/s)")
        for i in range(0, len(headers) - 1):
            axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")

    axes[1].legend()
    axes[1].grid()

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



