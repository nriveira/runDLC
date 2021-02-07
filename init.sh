module load tacc-singularity cuda/9.0
module load cudnn nccl
module save

singularity pull docker://nriveira/colginlab:latest
pip install deeplabcut==2.2b7