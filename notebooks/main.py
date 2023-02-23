import math
import random
from typing import TextIO
import sys

Q_LIMIT = 100
BUSY = 1
IDLE = 0
# Global variables
next_event_type = 0
num_custs_delayed = 0
num_delays_required = 0
num_events = 0
num_in_q = 0
server_status = 0
area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [0.0] * 3
total_of_delays = 0.0
infile = None
outfile = None



def main():
    # open the input and output files
    infile = open("mm1.in", "r")
    outfile  = open("mm1.out", "w")
    # specify number of events for timing function
    num_events = 2

    # read input parameters
    # read first line and split in 3 parts
    line = infile.readline().strip()
    parts = line.split()
    # convert each to appropriate data type
    mean_interarrival: float = float(parts[0])
    mean_service: float = float(parts[1])
    num_delays_required: int = int(parts[2])
    # write report heading and input parameters
    outfile.write("Single-server queueing system\n\n")
    outfile.write("Mean interarrival time{:11.3f} minutes\n\n".format(mean_interarrival))
    outfile.write("Mean service time{:16.3f} minutes\n\n".format(mean_service))
    outfile.write("Number of customers{:14d}\n\n".format(num_delays_required))

    # initialize the simulation
    initialize()
    # run the simulation while more delays are still needed
    while num_custs_delayed < num_delays_required:
        # determine next event
        timing()
        # update time average statistical accumulators
        update_time_avg_stats()
        # invoke the appropriate event function
        if next_event_type == 1:
            arrive()
        else:
            depart()
    # invoke report generator and end simulation
    report()
    infile.close()
    outfile.close()


# Function prototypes
def initialize():
    # initialize simulation clock
    sim_time: float = 0.0
    # initialize the state variables
    server_status: int = IDLE
    num_in_q: int = 0
    time_last_event: float = 0.0
    # initialize statistical counters
    num_custs_delayed: int = 0
    total_of_delays: float = 0.0
    area_num_in_q: float = 0.0
    area_server_status: float = 0.0
    # Initialize event list. Since no customers are present, the departure (service completion) event is eliminated
    # from consideration.

    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30


def timing():
    infile: TextIO = open("mm1.out", "r")
    outfile: TextIO = open("mm1.out", "w")
    sim_time: float = 0.0
    i: int = 0
    min_time_next_event: float = 1.0e+29
    next_event_type: int = 0
    # determine the event type of the next event to occur
    for i in range(1, num_events):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    # check to see whether event list is empty
    if next_event_type == 0:
        # the event list is empty so stop the simulation
        outfile.write("\nEvent list empty at time {}\n".format(sim_time))
        sys.exit(1)
    sim_time = min_time_next_event


def arrive(num_in_q=None, total_of_delays=None, num_custs_delayed=None, server_status=None):
    outfile = open("mm1","r")
    delay: float = 0.0
    # schedule next arrival
    time_next_event[1] = sim_time + expon(mean_interarrival)
    #check to see whether server is busy
    if server_status==BUSY:
        #server is busy so increment number of customers in queue
        num_in_q+=1
        #check whether overflow condition exists
        if num_in_q>Q_LIMIT:
            #queue overflowed stop simulation
            with open(outfile) as outfile:
                outfile.write(f"\nOverflow of the array time_arrival at time {sim_time}")
                outfile.write(f" time {sim_time}")
                sys.exit(2)
        # There is still room in the queue, so store the time of arrival of the arriving customer at the (new) end of time_arrival.
        time_arrival[num_in_q] = sim_time
    else:
        delay: float = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY

        #scheduke a departure i.e service completion
        time_next_event[2] = sim_time + expon(mean_service)



def depart(num_in_q=None, total_of_delays=None, num_custs_delayed=None):
    i: int = 0
    delay: float = 0.0
    if num_in_q==0:
        #queue is empty so make server idle
        #and eliminate the departure (service completion) event from consideration
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        #queue is not empty so decrement customers
        #in queue
        num_in_q -= 1

        delay = sim_time -time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time +expon(mean_service)
        for i in range(1,num_in_q):
            time_arrival[i] = time_arrival[i+1]





def report():
    outfile.write(f"\n\nAverage delay in queue{total_of_delays / num_custs_delayed:11.3f} minutes\n\n")
    outfile.write(f"Average number in queue{area_num_in_q / sim_time:10.3f}\n\n")
    outfile.write(f"Server utilization{area_server_status / sim_time:15.3f}\n\n")
    outfile.write(f"Time simulation ended{sim_time:12.3f} minutes")


def update_time_avg_stats(time_last_event=None, area_num_in_q=None, area_server_status=None):
    time_since_last_event=sim_time-time_last_event
    time_last_event = sim_time
    area_num_in_q += num_in_q
    area_server_status += server_status * time_since_last_event


def expon(mean):
    """"
    Generate a random number from an exponential distribution with a given mean

    Args:
        mean(float): The mean of exponential distribution.

    Returns:
        float: A random number from exponential distribution
    """

    return random.expovariate(1.0 / mean)


# the main function


if __name__ == "__main__":
    main()
