#!/bin/bash
#SBATCH --account=pcon0003
#SBATCH --job-name=persistent_arxov
#SBATCH --dependency=singleton
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --signal=B:SIGUSR1@90
# catch the SIGUSR1 signal
_resubmit() {
        ## Resubmit the job for the next execution
            echo "$(date): job $SLURM_JOBID received SIGUSR1 at $(date), re-submitting"
                sbatch $0
}
trap _resubmit SIGUSR1

## Insert the command to run below. Here, we're just outputing the date every
## 10 seconds, forever

echo "$(date): job $SLURM_JOBID starting on $SLURM_NODELIST"
python neverend.py 
