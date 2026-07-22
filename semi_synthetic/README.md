# Semi-synthetic SUPPORT experiments

This folder contains the SUPPORT-based semi-synthetic data-preparation notebooks and model-training scripts.

## Source data

The semi-synthetic experiments are based on the SUPPORT study:

Knaus et al., "The SUPPORT prognostic model. Objective estimates of survival for seriously ill hospitalized adults," Annals of Internal Medicine, 1995. PubMed: https://pubmed.ncbi.nlm.nih.gov/7810938/; DOI: https://doi.org/10.7326/0003-4819-122-3-199502010-00007.

The included `support2csv.zip` contains the SUPPORT-derived CSV used by the preparation notebooks.

## Generate semi-synthetic data

Set a data root and output root:

```bash
export CWITE_DATA_ROOT=/path/to/cwite-data
export CWITE_OUTPUT_ROOT=/path/to/cwite-outputs
```

Run `Support_data_50_oracle_update.ipynb` to generate the semi-synthetic splits used by the experiments. The notebook writes joblib files under:

```text
$CWITE_DATA_ROOT/support50_propbin_data/
```

The model scripts expect files named like:

```text
X_train_covariate_low_resource.joblib
y_train_covariate_low_resource.joblib
orig_y_train_covariate_low_resource.joblib
binary_y_train_covariate_low_resource.joblib
X_val_covariate_low_resource.joblib
y_val_covariate_low_resource.joblib
orig_y_val_covariate_low_resource.joblib
binary_y_val_covariate_low_resource.joblib
X_test_covariate_low_resource.joblib
orig_y_test_covariate_low_resource.joblib
binary_y_test_covariate_low_resource.joblib
```

## Run models

First run the hyperparameter-selection scripts:

```bash
python3 IPCW_hyp.py
python3 deephit_hyp.py
python3 powells_hyp.py
python3 oracle_hyp.py
```

These write selected-configuration text files. The release keeps the original selected-configuration files in:

```text
results/legacy_text_outputs/
```

Then run the final model scripts, which read those selected configurations and write models/predictions under `CWITE_OUTPUT_ROOT`:

```bash
python3 IPCW.py
python3 deephit.py
python3 powells.py
python3 oracle.py
python3 proposed_smallweight_linear.py
python3 proposed_largeweight_linear.py
python3 proposed_smallweight_exp.py
python3 proposed_largeweight_exp.py
```

## Included legacy outputs

For transparency, generated result tables, plots, and legacy text outputs from the original runs are kept under:

```text
results/paper_outputs/
results/legacy_text_outputs/
```
