#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --time=8:58:00
#SBATCH --job-name su2_job
#SBATCH --output=mpi_output_%j.txt
#SBATCH --mail-type=FAIL
 
cd $SLURM_SUBMIT_DIR

 
 
module load CCEnv
module load  StdEnv/2023  intel/2023.2.1
module load intelmpi/2021.9.0


mpirun -np 40 ~/bin-6/SU2_CFD NATO_Run4.cfg 


