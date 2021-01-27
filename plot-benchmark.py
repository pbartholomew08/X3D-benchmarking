"""
.. module:: plot-benchmark
    :synopsis:
"""

import csv

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.rc("text", usetex=True)
plt.rc("font", family="serif")
plt.rc("font", size=11)

def get_avg_runtime(row):

    tavg = 0
    for rep in range(3):

        header = "run " + str(rep) + " [s]"
        tavg += float(row[header])
    tavg /= 3.0

    return tavg

def get_data_volume(row):

    datavol = 0

    header_n = "n files [per dt]"
    header_fs = "file size [GB]"
    
    if header_n in row.keys:

        n = int(row[header_n])
        fs = float(row[header_fs])

        datavol = n * fs
        
    return datavol

def get_nranks(row):

    nnodes = int(row[header_nodes])
    ppn = int(row[header_ppn])
    nranks = nnodes * ppn
    
    return nranks

def read_bmk_row(row, bmk_data):

    machine = row["Machine"]

    if not (machine in bmk_data.keys):
        bmk_data[machine] = {}
        bmk_data[machine]["tavg"] = []
        bmk_data[machine]["datavol"] = []
        bmk_data[machine]["nranks"] = []

    bmk_data[machine]["nranks"] = get_nranks(row)
    bmk_data[machine]["tavg"] = get_avg_runtime(row)
    bmk_data[machine]["datavol"] = get_data_volume(row)

def read_benchmark(bmkfile):

    bmk_data = {}
    
    with open(bmkfile, "r") as csvdat:
        reader = csv.DictReader(csvdat)

        for row in reader:

            read_bmk_row(row, bmk_data)

    return bmk_data

def main():
    pass

if __name__ == "__main__":
    main()
