#! /usr/bin/env python3
# coding: utf-8 

# First line: the script must be executed using python 3
# Second line : utf-8 encoding used in the script source code in order to have accented characters

"""
=========================================================
Entrypoint for granite
=========================================================
"""

#    _____   __  __   _____     ____    _____    _______ 
#   |_   _| |  \/  | |  __ \   / __ \  |  __ \  |__   __|
#     | |   | \  / | | |__) | | |  | | | |__) |    | |   
#     | |   | |\/| | |  ___/  | |  | | |  _  /     | |   
#    _| |_  | |  | | | |      | |__| | | | \ \     | |   
#   |_____| |_|  |_| |_|       \____/  |_|  \_\    |_|   
#                                                        
#
# Standard includes
import argparse
import logging
import yaml
# Import the tqdm library for a smart progress meter  for loops
from tqdm import tqdm
# Project includes
from granite.deliverable import DeliverableGenerator

def run() -> None:

    #  Configure the logging system
    logging.basicConfig(format = "[%(process)s:%(threadName)s](%(asctime)s) %(levelname)s - %(name)s - [%(filename)s:%(lineno)d] - %(message)s", level=logging.INFO)

    # Configure the command line analysis module
    # parser = argparse.ArgumentParser(description="Template")
    parser = argparse.ArgumentParser()

    # Add command line argument to retrieve the operator configuration file
    parser.add_argument('-c', '--config-file', help = "Configuration file in yaml, default to 'config.yaml'")

    # Parse command line arguments
    args = parser.parse_args()

    # Retrieve the configuration file. If no configuration file is specified, use the default one.
    config_file = args.config_file or "config.yaml"

    # Open the configuration file
    with open(config_file) as config:

        # Load the information of the projects defined in the configuration file
        config_info = yaml.safe_load(config)

    # If no configuration file is put in the stream (not even the default one is present)
    if not config_info:
        # Raise an exception
        raise Exception('Invalid configuration file')
        
    # For each project in the configuration file:
    # Note: a tqdm progress bar is added to allow the operator to be informed of 
    # the progress of the project processing
    for project in tqdm(config_info.values()):
        # Generate the package delivery
        DeliverableGenerator(project)

# Encapsulate the main function in a conditional structure
# This makes it possible to import the file as a module and not to run the main() command.
if __name__ == "__main__":

    # Run granite application !
    run()


