# implicit_fisher
A miniapp to explore several parallel implementations of an implicit time integration solver of the 2D [Fisher system](https://en.wikipedia.org/wiki/Fisher%27s_equation) ([reaction-diffusion PDE](https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system)).
The code here is just slightly adapted from https://github.com/eth-cscs/SummerSchool2017; we've just added a cmake-based build system and modify vtk outputs.

## Download

```bash
git clone --recursive git@github.com:pkestene/implicit_fisher.git
```

## Modern CMake and CUDA

See https://github.com/CLIUtils/modern_cmake

## Requirements

- cmake version >= 3.10
- cuda toolkit

## How to build ?

### CUDA version

```bash
# set default CUDA flags passed to nvcc (Nvidia compiler wrapper)
# at least one hardware architecture flags
export CUDAFLAGS="-arch=sm_60 --expt-extended-lambda"
mkdir build
cd build
cmake -DENABLE_CUDA ..
make
# then you can run the application
./src/cuda/fisher_cuda 128 128 10 0.001
```

If you don't specify CUDAFLAGS environment variable, you setup cuda flags later in ccmake interface, search variable CMAKE_CUDA_FLAGS.


### PETSC version

Here the Fisher system of equations is of type <img src="https://render.githubusercontent.com/render/math?math=\frac{\partial U}{\partial t} = f(U,t)">.

Petsc time-stepping module solves the PDE using Newton iterations:

<img src="https://render.githubusercontent.com/render/math?math=x^{k%2B1} = x^k - [ f'(x^k) ]^{-1} * f(x^k)">

where <img src="https://render.githubusercontent.com/render/math?math=f'"> is a short notation for the Jacobian matrix :

<img src="https://render.githubusercontent.com/render/math?math=f'=\frac{\partial f}{\partial U}">

How to build ?

``` bash
    # configure
    export PETSC_DIR=/path/to/your/petsc/install/dir
    cmake -DENABLE_PETSC=ON ..
    make
```

Example run ?

``` bash
    # example run with one output every 10 time steps
    cd build/src/petsc
    mpirun -np 4 ./fisher_petsc -ts_monitor -snes_monitor -ksp_monitor -ts_view -filename fisher -dump_vtk 10
```
