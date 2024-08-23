import csv
import numpy as np

# some parameters
azimuth_start = -180
azimuth_end = 180
azimuth_step = 1
zenith_start = 0
zenith_end = 90
# zenith_step_1 = 1.33
# zenith_step_2 = 2.70
zenith_step_1 = 2.8125
zenith_step_2 = 2.8125
count = 1
total_time = 0.01  # seconds
total_zenith_steps = 32
# total_zenith_steps = (zenith_end - zenith_start) // zenith_step + 1

# timestep
azimuth_positions = (azimuth_end - azimuth_start) // azimuth_step + 1
time_step_per_zenith = total_time / (azimuth_positions * total_zenith_steps)
total_time+=time_step_per_zenith

output_file = './src/livox_laser_simulation/scan_mode/bpearl.csv'
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time/s', 'Azimuth/deg', 'Zenith/deg'])

    time = time_step_per_zenith
    for i in range(20):
        azimuth = azimuth_start
        while azimuth<=azimuth_end:
            zenith = zenith_start
            while zenith<zenith_end:
                writer.writerow([np.double(time), np.double(azimuth), np.double(zenith)])
                time += time_step_per_zenith
                if count<5 or count > 16:
                    zenith+=zenith_step_2
                else:
                    zenith+=zenith_step_1
                count+=1


            azimuth+=azimuth_step
        # zenith = zenith_start
        # azimuth = azimuth_start
        # while zenith<zenith_end:
        #     azimuth = azimuth_start
        #     while azimuth<=azimuth_end:
        #         writer.writerow([np.double(time), np.double(azimuth), np.double(zenith)])
        #         time += time_step_per_zenith
        #         azimuth+=azimuth_step
        #     zenith+=zenith_step


print(f"Scan generation done：{output_file}")
