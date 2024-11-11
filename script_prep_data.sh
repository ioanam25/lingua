#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=a100_short
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00

#SBATCH --job-name=fineweb_edu
#SBATCH --output slurm/fineweb_edu


python setup/download_prepare_hf_data.py fineweb_edu 8 --data_dir ./data --seed 42