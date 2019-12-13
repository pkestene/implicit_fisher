cmake_minimum_required(VERSION 3.10)
project(implicit_fisher LANGUAGES CXX C)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS OFF)

# custom cmake macros location
list(INSERT CMAKE_MODULE_PATH 0 "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
list(INSERT CMAKE_MODULE_PATH 0 "${CMAKE_CURRENT_SOURCE_DIR}/cmake/cuda")
list(INSERT CMAKE_MODULE_PATH 0 "${CMAKE_CURRENT_SOURCE_DIR}/cmake/petsc")

# Prevent from build in source tree
include(preventBuildInSource)

# Init build type: Release, Debug, ...
include(initBuildType)

# useful for debugging cmake
include(print_target_properties)

# To transform relative path from pkg-config into absolute
include(FindPkgconfigLibrariesAbsolutePath)
include(LibrariesAbsolutePath)

# a simple macro to build executable avoiding copy paste
#include(build_macro)

# always export compile commands database
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  

option(ENABLE_CUDA "build cuda version" OFF)
option(ENABLE_PETSC "build petsc version" OFF)

#####################################################################
if (ENABLE_CUDA)

  enable_language(CUDA)

  #find_package(CUDA REQUIRED)
  find_package(CUDALibs REQUIRED COMPONENTS CUBLAS )

  if(NOT DEFINED CMAKE_CUDA_STANDARD)
    set(CMAKE_CUDA_STANDARD 11)
    set(CMAKE_CUDA_STANDARD_REQUIRED ON)
  endif()

endif(ENABLE_CUDA)

#if (ENABLE_PETSC)
  find_package(PETSC)
#endif(ENABLE_PETSC)

# other third party libraries
find_package(OpenMP)
#find_package(OpenGL)
#find_package(GLUT)

# we also need extra stuff to make sure compile flags are correctly
# passed to nvcc / host compiler
include(protect_nvcc_flags)
include(protect_pthread_flag)

##########################################################
##########################################################
##########################################################
##########################################################

# build some executable
add_subdirectory(src)

# Testing
#enable_testing()

#-------------------------------------------------------------------#
# Configuration summary
#-------------------------------------------------------------------#
message("//===================================================")
message("  ${PROJECT_NAME} build configuration:")
message("//===================================================")
message("ENABLE_CUDA : ${ENABLE_CUDA}")
if(ENABLE_CUDA)
  message("  CUDA compiler ID      : ${CMAKE_CUDA_COMPILER_ID}")
  message("  CUDA compiler Version : ${CMAKE_CUDA_COMPILER_VERSION}")
  message("  C++ Compiler : ${CMAKE_CXX_COMPILER_ID} "
    "${CMAKE_CXX_COMPILER_VERSION} " 
    "${CMAKE_CXX_COMPILER_WRAPPER}")
  message("    ${CMAKE_CXX_COMPILER}")
  message("  CUDA Compiler      : ${CMAKE_CUDA_COMPILER}")
  message("  CUDA Compiler exec : ${CUDA_NVCC_EXECUTABLE}")
  message("  CUDA Compile flags : ${CMAKE_CUDA_FLAGS}")
endif(ENABLE_CUDA)
message("")
message("  OpenMP compile flags : ${OpenMP_CXX_FLAGS}")
message("")
message("  PETSc enabled : ${ENABLE_PETSC}")
if (ENABLE_PETSC)
  message("PETSC_DIR       : ${PETSC_DIR}")
  message("PETSC_ARCH      : ${PETSC_ARCH}")
  message("PETSC_VERSION   : ${PETSC_VERSION}")
  message("PETSC_INCLUDES  : ${PETSC_INCLUDE_DIR}")
  message("PETSC_LIBRARIES : ${PETSC_LIBRARIES}")
endif(ENABLE_PETSC)
#message(" Other third party libraries")


