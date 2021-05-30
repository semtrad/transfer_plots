#!/usr/bin/python3

import base
import glob, socket

from utils import *
from os import listdir
from os.path import isfile, join

from plot_file import PlotFile

# setup logging
logfile = get_logfile(sys.argv[0])

logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

#
def scan_plots_dir():

    plot_names = sorted(glob.glob(f"{from_path}/*.plot"))

    for plot_name in plot_names:
        transfer_plot, created = get_or_create(session, PlotFile, plot_name=plot_name)

        from_hostname = socket.gethostname()
        plot_size     = os.path.getsize(plot_name)

        transfer_plot.from_hostname = from_hostname
        transfer_plot.plot_size     = plot_size
        transfer_plot.to_path       = to_path

        if created:
            logging.info(f"Creating entry for plot_name:{plot_name}")

            transfer_plot.status        = 'new'

        session.commit()

#
def main():

    logging.info("Starting")

    scan_plots_dir()

#
if __name__ == "__main__":
    main()
