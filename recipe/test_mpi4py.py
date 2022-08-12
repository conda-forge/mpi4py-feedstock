import os

import mpi4py
from mpi4py import MPI
import mpi4py.futures

# on Windows this checks MSMPI_VER
print(MPI.get_vendor())

print(MPI.Get_library_version())

# verify get_config paths exist (not links to build env)
config = mpi4py.get_config()
print(f"config={config}")
for name in ("mpicc", "mpicxx", "mpifort"):
    if name in config:
        path = config[name]
        assert os.path.exists(path), f"{name} missing: {path}"
    else:
        print(f"Missing {name}")
