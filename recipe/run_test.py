import os
from subprocess import check_call
import sys

# openmpi env, before imoprting mpi4py
os.environ["OMPI_MCA_plm"] = "isolated"
os.environ["OMPI_MCA_btl_vader_single_copy_mechanism"] = "none"
os.environ["OMPI_MCA_rmaps_base_oversubscribe"] = "yes"
os.environ["OMPI_ALLOW_RUN_AS_ROOT"] = "1"
os.environ["OMPI_ALLOW_RUN_AS_ROOT_CONFIRM"] = "1"

import mpi4py
from mpi4py import MPI
import mpi4py.futures

# on Windows this checks MSMPI_VER
print(MPI.get_vendor())

print(MPI.Get_library_version())

for bench in ("helloworld", "ringtest"):
    print(f"Checking {bench}")
    check_call(
        [
            "mpiexec",
            "-n",
            "2",
            sys.executable,
            "-m",
            "mpi4py.bench",
            bench,
        ],
        env=os.environ,
    )
# verify get_config paths exist (not links to build env)
config = mpi4py.get_config()
print(f"config={config}")
for name in ("mpicc", "mpicxx", "mpifort"):
    if name in config:
        path = config[name]
        assert os.path.exists(path), f"{name} missing: {path}"
    else:
        print(f"Missing {name}")
