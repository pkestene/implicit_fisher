##############################################################
add_library(fisher_utils_cuda "")
target_sources(fisher_utils_cuda PRIVATE
  data.cu
  linalg.cu
  operators.cu
  stats.cu
 )

# the following line shouldn't be necessary as target_link_libraries
# with OpenMP::OpenMP_CXX should pass the correct flags for OpenMP
# but apparently, this is KO when using nvcc :(
# You can remove that if OpenMP is not required
# checked using cmake 3.14.3 (October 2019)
target_compile_options(fisher_utils_cuda PUBLIC
  $<$<COMPILE_LANGUAGE:CXX>:${OpenMP_CXX_FLAGS}>
  $<$<COMPILE_LANGUAGE:CUDA>:-Xcompiler ${OpenMP_CXX_FLAGS}>
  )
target_link_libraries(fisher_utils_cuda PUBLIC CUDA::cublas)
target_link_libraries(fisher_utils_cuda PUBLIC OpenMP::OpenMP_CXX)


##############################################################
# main application
add_executable(fisher_cuda "")
target_sources(fisher_cuda 
  PRIVATE
  main.cu
  )

# target_compile_options(fisher_cuda PUBLIC
#   $<$<COMPILE_LANGUAGE:CXX>:${OpenMP_CXX_FLAGS}>
#   $<$<COMPILE_LANGUAGE:CUDA>:-Xcompiler ${OpenMP_CXX_FLAGS}>
#   )
target_link_libraries(fisher_cuda PUBLIC fisher_utils_cuda)

configure_file(test.sh test.sh COPY_ONLY)
configure_file(plotting.py plotting.py COPY_ONLY)

#############################################################
# unit test
add_executable(unit_tests "")
target_sources(unit_tests
  PRIVATE
  unit_tests.cu)
target_link_libraries(unit_tests PUBLIC fisher_utils_cuda)
