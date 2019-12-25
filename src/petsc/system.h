#ifndef FISHER_SYSTEM_H
#define FISHER_SYSTEM_H

#include <petscvec.h>
#include <petscmat.h>
#include <petscts.h>

#include "AppCtx.h"

PetscErrorCode RHSFunction(TS,PetscReal,Vec,Vec,void*);
PetscErrorCode RHSJacobianAssembled(TS,PetscReal,Vec,Mat,Mat,void*);
PetscErrorCode InitialConditions(Vec,AppCtx*);

#endif // FISHER_SYSTEM_H
