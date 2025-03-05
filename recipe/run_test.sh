#/bin/sh
set -ex

# UCX memory events can cause crashes,
# at least on linux-aarch64 + CPython 3.12
# also seen in Julia: https://github.com/openucx/ucx/issues/5061
export UCX_MEM_MMAP_HOOK_MODE=reloc

# Basic tests
mpiexec -n 1 python -m mpi4py --version
mpiexec -n 1 python -m mpi4py --mpi-std-version
mpiexec -n 1 python -m mpi4py --mpi-lib-version
mpiexec -n 2 python -m mpi4py.bench helloworld
mpiexec -n 2 python -m mpi4py.bench ringtest

# Additional tests are in Python
python ${RECIPE_DIR}/test_mpi4py.py
