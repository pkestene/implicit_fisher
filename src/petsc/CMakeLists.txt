add_executable(fisher_petsc "")
target_sources(fisher_petsc PRIVATE
  dump.cpp
  system.cpp
  monitor.cpp
  main.cpp)

target_include_directories(fisher_petsc PUBLIC ${PETSC_INCLUDE_DIRS})
target_link_libraries(fisher_petsc 
  PUBLIC
  MPI::MPI_CXX
  ${PETSC_LIBRARIES})

file(COPY testref DESTINATION .)
