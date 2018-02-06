# Automated Gating of Live, Dead, and Debris Cell Populations

This directory contains data for a machine learning based
approach to flow cytometry cell population classification.

## Objective

Given an fcs file representing a cell sample from a cancer patient
we want to cluster the data points (also known as events) into three
distinct clusters: live cells, dead cells, and debris.  The machine
generated clusters should mimic the clusters a scientist would manually
create. Ultimately, we want to output an fcs file that contains only
the live subset so a scientist can perform further analysis with this
file.

This problem is one piece of a larger objective to classify all populations
of live cells as a certain cell type (granulocytes, T-cells, B-cells,
etc) from an fcs file. This initial live vs dead vs debris is a
critical first step to purify the data for downstream classification of
the live cells.

### Output

Please create a notebook of your work exploring that data and building the
classifier, we'll discuss the details of your analysis during the interview.
Also, please package up the classifier into a script that takes a single fcs
file as input and returns a new fcs file that only contains the live cells
population.

## Files within this folder

Each fcs well file contains flow data from a few thousand patient cells
within a well exposed to a specific drug.

- `Well_x.fcs`: flow cytometry data files with additional experimental
  metadata added, such as which antibodies were used to stain.

- `live_dead_debris__labels.csv`: the `live`, `dead`, or `debris` label for
  each event recorded in the fcs files. The labels were generating from the
  manual gates determined by a scientist.

This data has been extracted from a single screen for a single patient. Note that
there is high variablity in the data from patient to patient due to the fact that
patients respond differently to the same drugs. However, many of the wells
within a screen are replicates for the same drug, so there should be some
correllation in these pairs.

Any machine based approaches will ultimately be judged against human attempts
at gating, even if the human attempts are somewhat flawed.

## Initial approach

Manual gating of live vs dead vs debris is traditionally done using FSC
vs SSC.  Clustering using these dimensions are a good starting point,
though feel free to incorporate additional dimensions.

We recommend using Notable Labs version of the `fcsparser` python library:

https://github.com/NotableLabs/fcsparser

This will allow you access the events data in a dataframe:
```
path = 'path/to/dropbox_folder/Well_C3.fcs'
meta, df = fcsparser.parse(path, reformat_meta=True)
print df[['FSC-H', 'SSC-H']]
```
