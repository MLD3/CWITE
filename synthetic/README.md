# Synthetic experiments

This folder contains the synthetic data-generation notebooks and model-training scripts used for the one-dimensional labor simulation experiments.

## Generate synthetic data

Set a data root and output root:

```bash
export CWITE_DATA_ROOT=/path/to/cwite-data
export CWITE_OUTPUT_ROOT=/path/to/cwite-outputs
```

Generate the main synthetic datasets by running `data_generation.ipynb`. The notebook writes joblib files under:

```text
$CWITE_DATA_ROOT/onevar_data/
```

Generate the assumption-violation datasets by running `data_generation_violations_assumption_4.ipynb`. That notebook writes joblib files under:

```text
$CWITE_DATA_ROOT/viol4_onevar_data/
```

The model scripts expect files named like:

```text
X_train_COUNT0.joblib
orig_y_train_COUNT0.joblib
y_train_COUNT0.joblib
binary_y_train_COUNT0.joblib
X_val_COUNT0.joblib
y_val_COUNT0.joblib
binary_y_val_COUNT0.joblib
X_test_COUNT0.joblib
y_test_COUNT0.joblib
actual_binary_y_testCOUNT0.joblib
```

## Run models

The main scripts write models and predictions to `CWITE_OUTPUT_ROOT`:

```bash
python3 IPCW.py 0 125
python3 deephit.py 0 125
python3 powells.py 0 125
python3 proposed.py 0 125
python3 oracle.py 0 125
```

The two numeric arguments are the first and last synthetic replicate indices. The original experiments used ranges such as `0 125`, `125 250`, ..., `875 1000`.

## Included legacy outputs

For transparency, legacy text outputs and figures from the original runs are kept under:

```text
results/legacy_text_outputs/
results/figures/
d_calibration/results/legacy_text_outputs/
```

These files document previous selected hyperparameters, DGP parameters, and plotting outputs. New model-script runs write fresh text summaries to `results/legacy_text_outputs/`.
