import os

import mpi4py
import mpi4py.futures
import mpi4py.util.dtlib
import mpi4py.util.pkl5
from mpi4py import MPI

# on Windows this checks MSMPI_VER
print(MPI.get_vendor())

print(MPI.Get_library_version())

# TODO: remove for mpi4py 4.0.0
# verify get_config paths exist (not links to build env)
config = mpi4py.get_config()
print(f"config={config}")
for name in ("mpicc", "mpicxx", "mpifort"):
    if name in config:
        path = config[name]
        assert os.path.exists(path), f"{name} missing: {path}"
    else:
        print(f"Missing {name}")
