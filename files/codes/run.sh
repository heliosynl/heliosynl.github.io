#!/bin/bash
# running batch file for HKU hpc2021
#SBATCH --job-name=example                # 1. Job name, only display the first 8 characters
#SBATCH --mail-type=BEGIN,END,FAIL        # 2. Send email upon events (Options: NONE, BEGIN, END, FAIL, ALL)
#SBATCH --partition=amd                   # 3. Request a partition
#SBATCH --mail-user=youremail@connect.hku.hk  #    Email address to receive notification
#SBATCH --qos=normal                      # 4. Request a QoS
#SBATCH --ntasks=64                       # 5. Request total number of tasks (MPI workers)
#SBATCH --nodes=1                         # 6. Request number of node(s), 1 is ok
#SBATCH --mem=200G                        # 7. RAM assignment, more RAM makes longer queuing time, comsol need larger, but 200G is ok
#SBATCH --time=0-12:00:00                 # 8. Job execution duration limit day-hour:min:sec
#SBATCH --output=%x.out                   # 9. Standard output log as $job_name_$job_id.out
#SBATCH --error=%x.err                    #    Standard error log as $job_name_$job_id.err

# print the start time
date
export OMP_NUM_THREADS=1
# module load quantumespresso
# module load impi

# mpirun pw.x < >& 

module load comsol/6.1
export COMSOLTMP=~/group/tmpcomsol

comsol batch -recoverydir $COMSOLTMP -np 64 -inputfile input.mph -outputfile out.mph
# print the end time
date
