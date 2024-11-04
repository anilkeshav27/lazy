import time
from os import environ
from task import runTask

def preChecks():
    if environ.get("TASK_HOME") is None:
        print("unable to retrieve the environment variable TASK_HOME needed for task")
    else:
        runTask()
        


if __name__ == "__main__":
     preChecks()




