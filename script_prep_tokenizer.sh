#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=a100_short
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00

#SBATCH --job-name=tokenizer_llama3
#SBATCH --output slurm/tokenizer_llama3.out


python setup/download_tokenizer.py llama3 "tokenizer" --api_key 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