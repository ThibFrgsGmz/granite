#! /usr/bin/env python3
# coding: utf-8 

# First line: the script must be executed using python 3
# Second line : utf-8 encoding used in the script source code in order to have accented characters

"""
=========================================================
Entrypoint for  granite
To run service, set CONFIG_LOCATION environmental variable and run
python -m granite+.__main__
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
# Import the time library to add delays
import time
import os
import argparse
import logging
import yaml
# Import the tqdm library for a smart progress meter  for loops
from tqdm import tqdm
# Project includes
# Import all function from the functions module
try:
    # import analysis.functions as func
    from granite.deliverable import DeliverableGenerator
except ImportError as err:
    print('ImportError :', err)

def run():
    # Retrieve the absolute path of the file
    BASE = os.path.abspath(os.path.dirname(__file__))

    #  Configure the logging system
    logging.basicConfig(format = "[%(process)s:%(threadName)s](%(asctime)s) %(levelname)s - %(name)s - [%(filename)s:%(lineno)d] - %(message)s", level=logging.INFO)

    parser = argparse.ArgumentParser(description="Template")

    help_msg = "Configuration file in yaml, default to 'config.yaml'"

    parser.add_argument('-c', '--config-file', help=help_msg)
    help_msg = "output directory, default to '.'"
    parser.add_argument('-o', '--output-dir', help=help_msg)

    args = parser.parse_args()

    # Define the configuration file
    config_file = args.config_file or "config.yaml"

    with open(config_file) as config:
        config_info = yaml.safe_load(config)
    if not config_info:
        raise Exception('Invalid configuration file')
    else:
        # for item in config_info.values():
        for item in tqdm(config_info.values()):
            # Generate the package delivery
            generator = DeliverableGenerator(item)

# Encapsulate the main function in a conditional structure
# This makes it possible to import the file as a module and not to run the main() command.
if __name__ == "__main__":

    run()


