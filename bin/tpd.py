#!/usr/bin/python3

import base
from utils import *

# setup logging
logfile = get_logfile(sys.argv[0])

logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

#
def main():

    logging.info("Starting")

#
if __name__ == "__main__":
    main()
