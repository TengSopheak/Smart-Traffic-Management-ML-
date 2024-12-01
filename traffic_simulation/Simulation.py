import multiprocessing
from TrafficLightSimulation1 import traffic_light_simulation_1
from TrafficLightSimulation2 import traffic_light_simulation_2
from TrafficLightSimulation3 import traffic_light_simulation_3
from TrafficLightSimulation4 import traffic_light_simulation_4

if __name__ == "__main__":
    # List of simulation modules to run
    simulations = [
        traffic_light_simulation_1,
        traffic_light_simulation_2,
        traffic_light_simulation_3,
        traffic_light_simulation_4
    ]

    # Create and start a separate process for each simulation
    processes = []
    for simulation in simulations:
        p = multiprocessing.Process(target=simulation)
        p.start()
        processes.append(p)

    # Optionally wait for all processes to complete
    for p in processes:
        p.join()
