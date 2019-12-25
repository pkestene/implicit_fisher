#ifndef FISHER_APPCTX_H
#define FISHER_APPCTX_H

#include <petscts.h>

/* A user-defined context to store problem data */
struct AppCtx {

  DM          da;             /* distributed array data structure */
  Vec         u_local;        /* local ghosted approximate solution vector */
  PetscInt    nx,ny;          /* Grid sizes */
  PetscScalar dxinv2;         /* holds 1/dx^2, which is (nx-1)^2 */
  PetscInt    dump_vtk_interval; /* time steps between two VTK dumps */
  char        baseFilename[PETSC_MAX_PATH_LEN];

};

#endif // FISHER_APPCTX_H
