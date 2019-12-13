# implicit_fisher
A miniapp to explore several parallel implementations of a time-implicit discretization of the Fisher (advection-diffusion) equation

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

