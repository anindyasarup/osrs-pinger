""" 
Module providing function for creating a new process 
and help interact with the input and output streams 
of the process. 
"""
from typing import Union, List
import subprocess


def create_process_object(logger, process_args: Union[str, List[str]]) -> subprocess.Popen[bytes]:
    """
    Create Process Object with the given process arguments using subprocess module

    Args:
        process_args (Union[str, List[str]]): a string command or 
            a string array with command and command line arguments

    Returns:
        subprocess.Popen[bytes]: process object setup with the given process 
            arguments 
    """
    try:
        logger.info("Creating process Object")
        process = subprocess.Popen(process_args,
                                   shell=True,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)
        return process
    except Exception as ex:
        logger.error("An exception occurred: %s", ex)
