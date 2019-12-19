#ifndef FISHER_MONITOR_H
#define FISHER_MONITOR_H

#include <petscts.h>

#include "appctx.h"

PetscErrorCode MonitorVTK(TS ts, 
                          PetscInt stepnum, 
                          PetscReal time,
                          Vec X, 
                          void *ctx);

#endif // FISHER_MONITOR_H
