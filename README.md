# CWITE MLHC 2026 Code Release (Paper will be uploaded when it is published online)

This repository contains code accompanying the MLHC 2026 paper on CWITE for time-to-event prediction under limited uncensored training support and censoring distribution shift.

## Directory Structure

- `synthetic/`: synthetic labor experiments, baselines, CWITE variants, calibration analyses, and plotting/result notebooks.
- `semi_synthetic/`: semi-synthetic SUPPORT-based experiments, baselines, CWITE variants, clustering analyses, and result-generation notebooks.
- `real_data/`: real labor analysis code, feature-selection sweeps, clustering sensitivity analyses, propensity-stratified evaluation, calibration checks, and clinical overprediction metrics.
- `hyperparameter_recovery/`: helper scripts and recovered tables used to summarize selected hyperparameters from experiment outputs.

## Data Availability

The synthetic experiments can be regenerated from the included code. The semi-synthetic experiments use SUPPORT-derived data preparation artifacts included with the experiment code where available. The real-data experiments use protected clinical data that cannot be redistributed; those scripts are included to document the analysis pipeline and should be run in an approved environment with the required derived input files.

The semi-synthetic experiments are based on the SUPPORT study: Knaus et al., "The SUPPORT prognostic model. Objective estimates of survival for seriously ill hospitalized adults," Annals of Internal Medicine, 1995. PubMed: https://pubmed.ncbi.nlm.nih.gov/7810938/; DOI: https://doi.org/10.7326/0003-4819-122-3-199502010-00007.

## Data Generation

Detailed regeneration instructions are provided in the experiment folders:

- `synthetic/README.md`: synthetic data generation notebooks, expected generated files, and example commands for running the synthetic methods.
- `semi_synthetic/README.md`: SUPPORT-derived semi-synthetic data preparation, expected generated files, hyperparameter scripts, and final method runs.

The generated data files are intentionally kept outside the repository and are read through `CWITE_DATA_ROOT`. Model outputs and predictions are written outside the repository through `CWITE_OUTPUT_ROOT`.

## Included Results

Legacy text logs, selected configurations, paper tables, and figures used during manuscript preparation are retained for transparency, but they are separated from the runnable source code:

- `synthetic/results/legacy_text_outputs/`
- `synthetic/results/figures/`
- `synthetic/d_calibration/results/legacy_text_outputs/`
- `semi_synthetic/results/legacy_text_outputs/`
- `semi_synthetic/results/paper_outputs/`

New synthetic and semi-synthetic runs write their text summaries into the corresponding `results/legacy_text_outputs/` directories rather than the source-code directories.

## Running The Code

Install the Python dependencies listed in `requirements.txt`, then point the scripts at local data and output directories:

```bash
export CWITE_DATA_ROOT=/path/to/cwite-data
export CWITE_OUTPUT_ROOT=/path/to/cwite-outputs
```

The synthetic and semi-synthetic scripts read from `CWITE_DATA_ROOT` and write models/predictions under `CWITE_OUTPUT_ROOT`. The expected subdirectories are:

```text
$CWITE_DATA_ROOT/onevar_data
$CWITE_DATA_ROOT/viol4_onevar_data
$CWITE_DATA_ROOT/support50_propbin_data
$CWITE_OUTPUT_ROOT/onevar_models
$CWITE_OUTPUT_ROOT/onevar_test_preds
$CWITE_OUTPUT_ROOT/support50_propbin_models
$CWITE_OUTPUT_ROOT/support50_propbin_test_preds
```

For real-data analyses, use the real-data-specific variables:

```bash
export CWITE_REAL_DATA_DIR=/path/to/approved/real_labor_joblibs
export CWITE_REAL_RUN_ROOT=/path/to/real_data_outputs
cd real_data
bash run_all_realdata_series.sh
```

The protected clinical data used in the real-data experiments cannot be redistributed, so the real-data scripts require approved local derived joblib files. All formerly local machine paths have been replaced by these environment variables or command-line arguments.

## Hyperparameters

Selected hyperparameters and helper scripts for recovering them from output archives are in `hyperparameter_recovery/`. For synthetic experiments, final selected configurations may vary by independently generated replicate; those replicate-level configurations are documented in the released code and associated output files rather than repeated in full in the manuscript.
