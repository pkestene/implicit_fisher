if (ENABLE_CUDA)
  add_subdirectory(cuda)
endif(ENABLE_CUDA)

if (ENABLE_PETSC)
  add_subdirectory(petsc)
endif(ENABLE_PETSC)
