add_executable(fisher_petsc "")
target_sources(fisher_petsc PRIVATE
  dump.c
  system.c
  monitor.c
  main.c)

target_include_directories(fisher_petsc PUBLIC ${PETSC_INCLUDE_DIRS})
target_link_libraries(fisher_petsc 
  PUBLIC
  MPI::MPI_CXX
  ${PETSC_LIBRARIES})

file(COPY testref DESTINATION .)
