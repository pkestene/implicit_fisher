# run examples

```bash
mpirun -n 4 ./fisher_petsc -nx 99 -ny 88 -ts_monitor -snes_monitor -ksp_monitor
mpirun -n 1 ./fisher_petsc -nx 16 -ny 16 -ts_monitor -snes_monitor -ksp_monitor -assemble 1 -pc_type gamg -dump 1
```

Please note that currently data dump is only available when using one MPI task, but you can use petsc viewer capability, by adding option '-ts_monitor_solution_vtk fisher-%03D.vts'


# run tests

```bash
export TEST_OPTIONS="-ts_monitor -snes_monitor -ksp_monitor -ts_view"
mpirun -n 1 ./fisher_petsc ${TEST_OPTIONS}  2>&1 > test1.tmp
diff test1.tmp testref/test1.ref
```

```bash
mpirun -n 2 ./fisher_petsc ${TEST_OPTIONS}  2>&1 > test2.tmp
diff test2.tmp testref/test2.ref
```
