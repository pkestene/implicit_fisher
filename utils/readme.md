Here a few python script examples to help you configure and build PETSc from sources:

- `petsc_config_base.py` : build PETSc using options very similar to Ubuntu package (most of external dependances are provides by Ubuntu instead of being downloaded from PETSc install script)
- `petsc_config_p4est.py` : same as above but slightly modified to enable adaptive mesh refinement library [p4est](http://www.p4est.org/)
- `petsc_config_cuda.py` : minimal configuration to build petsc from sources with [GPU support enabled](https://gitlab.com/petsc/petsc/-/wikis/PETSc-on-GPUs)


Notice before building PETSc with GPU support enabled:

- if you want both MPI+GPU support, make sure to have a CUDA-aware MPI implementation installed on your system; usually OpenMPI or MPICH packages from Linux distribution are not CUDA-aware; so you will need to build e.g. OpenMPI from sources (but this is easy, unless your want to run on a super-computer with high-speed infiniband network, in that can case you'll ask your system admin to do it for you)
- example of configuration to build openmpi-4.0.2 from sources:
```bash
    cd opempi-4.0.2
    mkdir build; cd build
    ../configure --prefix=/home/pkestene/local/openmpi-4.0.2-cuda --with-cuda --enable-mpi-thread-multiple --enable-mpi-cxx --with-hwloc=/usr/ --with-libltdl=/usr/ --with-devel-headers --enable-heterogeneous --disable-vt --without-tm
    make
    make install
```
- you also need to rebuild other packages with your new CUDA-aware MPI implementation (hdf5, ...). The simplest way to go is to let PETSc download and build hdf5 for you.
