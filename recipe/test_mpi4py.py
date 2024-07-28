from mpi4py import MPI

# on Windows, this checks MSMPI_VER
print(MPI.get_vendor())
