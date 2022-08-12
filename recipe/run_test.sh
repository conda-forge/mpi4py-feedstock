set -ex

export OMPI_MCA_plm=isolated
export OMPI_MCA_btl_vader_single_copy_mechanism=none
export OMPI_MCA_rmaps_base_oversubscribe=yes
export OMPI_ALLOW_RUN_AS_ROOT=1
export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

mpiexec -n 2 python -m mpi4py.bench helloworld
mpiexec -n 2 python -m mpi4py.bench ringtest

# most tests are in Python
python ${RECIPE_DIR}/test_mpi4py.py
