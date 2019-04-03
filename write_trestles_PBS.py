#!/usr/bin/env python3

import argparse

#create an argument  parser object ('parser') that will hold all the information necessary to parse the command line
parser=argparse.ArgumentParser(description='generates a PBS job script for the AHPCC Trestles cluster')


#add positional arguments (absolutely required for the job to run) ie. the required input aka job name
parser.add_argument('job_name', help='the name of the job')
#we specifed the variable name here to job_name, so we deleted this from the code job_name='raquel'


#add optional arguments
parser.add_argument('-q', '--queue', help='name of the Trestles queue(default=q06h32c)', default='q06h32c')
parser.add_argument('-p', '--ppn', help='number of processors (default=32)', type=int, default='32')
parser.add_argument('-w', '--walltime', help='amount of time needed for job (default=6)', type=int, default='6')
#blast required commands:job name,  - N and two required arguments data base and queue 

#parse the command line arguments
args=parser.parse_args()


print ('#PBS -N',args.job_name)
print ('#PBS -q', args.queue)
print ('#PBS -j oe')
print ('#PBS -m abe')
print ('#PBS -M rgpalmer@uark.edu')
print ('#PBS -o', args.job_name + '.$PBS_JOBID')
print ('#PBS -l',"nodes=1:ppn=" +str(args.ppn))
print ('PBS -l args.walltime'+str(args. walltime)+ ":00:00")

print('cd $PBS_O_WORKDIR')
print ()

print('module purge')
print ('module load python/3.6.0-anaconda') 
