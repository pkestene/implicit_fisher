#include "monitor.h"

// =====================================================
// =====================================================
PetscErrorCode MonitorVTK(TS ts,
                          PetscInt stepnum, 
                          PetscReal time, 
                          Vec X, 
                          void *ctx)
{

  PetscErrorCode ierr;
  AppCtx *appctx = (AppCtx*) ctx;   /* user-defined application context */

  char filename[PETSC_MAX_PATH_LEN];

  if (appctx->dump_vtk_interval < 0)
    PetscFunctionReturn(0);

  if (stepnum % appctx->dump_vtk_interval == 0) {

    PetscPrintf(PETSC_COMM_WORLD, "Saving data at time step: %d\n", stepnum);
    
    // prepare complete output filename
    int fileId = stepnum / appctx->dump_vtk_interval;

    ierr = PetscSNPrintf(filename,sizeof(filename),"%s-%03D.vts",appctx->baseFilename,fileId);CHKERRQ(ierr);

    // then write file
    {
      PetscViewer viewer;
      PetscViewerVTKOpen(PetscObjectComm((PetscObject)ts), filename,
                         FILE_MODE_WRITE, &viewer);
      VecView(X, viewer);
      PetscViewerDestroy(&viewer);
    }

  }

  PetscFunctionReturn(0);

} // MonitorVTK
