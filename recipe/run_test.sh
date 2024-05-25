set -ex

export OMPI_MCA_plm_ssh_agent=false
export OMPI_MCA_pml=ob1
export OMPI_MCA_mpi_yield_when_idle=true
export OMPI_MCA_btl_base_warn_component_unused=false
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
export OMPI_ALLOW_RUN_AS_ROOT=1
export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

mpiexec -n 2 python -m mpi4py.bench helloworld
mpiexec -n 2 python -m mpi4py.bench ringtest

# most tests are in Python
python ${RECIPE_DIR}/test_mpi4py.py
