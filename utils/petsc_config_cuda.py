#!/usr/bin/env python

"""
 This is a petsc configuration script for building latest PETSc
 version on Ubuntu 18.04 with GPU support enabled.

 # on a super-computer, you may need to load some modules, e.g.
 module load cuda/10.2
 module load openmpi/4.0.2-cuda
"""

import os
petsc_hash_pkgs=os.path.join(os.getenv('HOME'),'petsc-hash-pkgs')
if not os.path.isdir(petsc_hash_pkgs): os.mkdir(petsc_hash_pkgs)

if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure

  PETSC_ARCH="x86_64-linux-gnu-cuda"
  PETSC_VERSION="3.12.2-cuda"
  PETSC_MPI="openmpi"
  #PETSC_MPI_DIR="/usr/lib/x86_64-linux-gnu/openmpi"
  PETSC_MPI_DIR="/home/pkestene/local/openmpi-4.0.2-cuda"
  #export OMPI_MCA_plm_rsh_agent=/bin/false
  PETSC_BUILD_DIR=PETSC_ARCH+"-real"

  configure_options = [
    'COPTFLAGS=-O3',
    'CXXOPTFLAGS=-O3',
    'FOPTFLAGS=-O3',
    '--with-precision=double',
    '--with-debugging=0',
    '--shared-library-extension=_real',
    '--with-clanguage=c++',
    '--with-shared-libraries',
    '--with-pic=1',
    '--useThreads=0',
    '--with-fortran-interfaces=1',
    '--with-mpi-dir='+PETSC_MPI_DIR,
    '--with-cuda=1',
    '--with-cudac=nvcc',
    '--CUDAFLAGS=-arch=sm_75',
    '--CUDAOPTFLAGS=-O3',
    '--download-viennacl=1',
    '--with-blas-lib=-lblas',
    '--with-lapack-lib=-llapack',
    '--download-scalapack=1',
    #'--with-scalapack=1',
    #'--with-scalapack-lib=-lscalapack-'+PETSC_MPI,
    # '--with-mumps=1',
    # '--with-mumps-include=[]',
    # '--with-mumps-lib=-ldmumps -lzmumps -lsmumps -lcmumps -lmumps_common -lpord',
    '--download-mumps=1',
    '--download-suitesparse=1',
    #'--with-suitesparse=1',
    #'--with-suitesparse-include=/usr/include/suitesparse',
    #'--with-suitesparse-lib=-lumfpack -lamd -lcholmod -lklu',
    '--download-spooles=1',
    #'--with-spooles=1',
    #'--with-spooles-include=/usr/include/spooles',
    #'--with-spooles-lib=-lspooles',
    '--download-ptscotch',
    #'--with-ptscotch=1',
    #'--with-ptscotch-include=/usr/include/scotch',
    #'--with-ptscotch-lib=-lptesmumps -lptscotch -lptscotcherr',
    #'--with-fftw=1',
    #'--with-fftw-include=[]',
    #'--with-fftw-lib=-lfftw3 -lfftw3_mpi',
    '--with-superlu=1',
    '--with-superlu-include=/usr/include/superlu',
    '--with-superlu-lib=-lsuperlu',
    '--download-hdf5=1',
    '--CXX_LINKER_FLAGS=-Wl,--no-as-needed',
    '--download-metis=1',
    '--download-parmetis=1',
    '--download-triangle=1',
    '--download-ctetgen=1',
    '--download-ml=1',
    '--download-hypre=1',
    # '--with-hypre=1',
    # '--with-hypre-include=/usr/include/hypre',
    # '--with-hypre-lib=-lHYPRE_IJ_mv -lHYPRE_parcsr_ls -lHYPRE_sstruct_ls -lHYPRE_sstruct_mv -lHYPRE_struct_ls -lHYPRE_struct_mv -lHYPRE_utilities',
    '--prefix=/home/pkestene/local/petsc-'+PETSC_VERSION
  ]

  print("Configuring petsc with the following options:")
  print("\n")
  print(configure_options)
  print("\n")

  configure.petsc_configure(configure_options)
