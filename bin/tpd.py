#!/usr/bin/python3

import base
import glob, socket, datetime

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

        if created:
            logging.info(f"Creating entry for plot_name:{plot_name}")

            from_hostname = socket.gethostname()
            plot_size     = os.path.getsize(plot_name)

            transfer_plot.from_hostname = from_hostname
            transfer_plot.plot_size     = plot_size
            transfer_plot.to_path       = to_path
            transfer_plot.status        = 'new'

        session.commit()

#
def transfer_plots():

    next_transfer = session.query(PlotFile).filter(PlotFile.status != 'transferred').order_by(PlotFile.id).first()

    if next_transfer != None: 
        from_hostname = socket.gethostname()

        if next_transfer.from_hostname == from_hostname:
            if next_transfer.status == 'new':
                logging.info(f"Transferring {next_transfer.plot_name} to {next_transfer.to_path}")

                transfer_start_time = datetime.datetime.now()

                next_transfer.status              = 'transferring'
                next_transfer.transfer_start_time = transfer_start_time
                session.commit()

                # rsync_cmd = f'rsync --progress --remove-source-files --bwlimit=80m {next_transfer.plot_name} {next_transfer.to_path}'
                rsync_cmd = f'RSYNC_PASSWORD=rsync; export RSYNC_PASSWORD; rsync --remove-source-files --bwlimit=80m {next_transfer.plot_name} {next_transfer.to_path}'

                os.system(rsync_cmd)

                transfer_end_time = datetime.datetime.now()

                transfer_total_time = int((transfer_end_time - transfer_start_time).total_seconds())

                next_transfer.status              = 'transferred'
                next_transfer.transfer_end_time   = transfer_end_time
                next_transfer.transfer_total_time = transfer_total_time
                session.commit()

                logging.info(f"Transfer complete in {transfer_total_time} seconds")

            else:
                logging.info(f"Current plot status is {next_transfer.status}")

        else:
            logging.info(f"Next plot to transfer is on host:{next_transfer.from_host}")

    else:
        logging.info("No plot_file to transfer")

#
def main():

    while True:
        scan_plots_dir()

        transfer_plots()

        time.sleep(60)

#
if __name__ == "__main__":
    main()
