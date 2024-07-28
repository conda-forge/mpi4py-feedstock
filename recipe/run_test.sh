#/bin/sh
set -ex

# Basic tests
mpiexec -n 1 python -m mpi4py --version
mpiexec -n 1 python -m mpi4py --mpi-std-version
mpiexec -n 1 python -m mpi4py --mpi-lib-version
mpiexec -n 2 python -m mpi4py.bench helloworld
mpiexec -n 2 python -m mpi4py.bench ringtest

# Additional tests are in Python
python ${RECIPE_DIR}/test_mpi4py.py
