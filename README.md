# Count samples for Genotyping

A simple script to number samples on gel after running PCR. 
It uses OpenCV's template matching to detect DNA ladders; if a ladder is detected, it numbers samples accordingly.

As our lab adds controls at the end of samples, these are also added by default (i.e., Wild-Type, Cre positive, Tris)

**This is still very much a work in progress!!**
