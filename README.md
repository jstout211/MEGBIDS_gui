# MEGBIDS_gui (Brainhack DC 2022 project)
Front end for converting MEG (+MRI T1) to bids.

# Background
BIDS is becoming more prevalent in neuroimaging and allows for pipelines based on the standardized path structure.  Converting neurophsiological data to bids has become easier, but is still mainly a commandline driven process.  This hackathon project will build some initial GUI development into this process. <br><br>
mne_bids: https://mne.tools/mne-bids/stable/index.html <br>
mne: https://mne.tools/stable/index.html <br>

# Install Packages
```
conda activate base
conda install conda-forge::mamba -y

mamba create -n megbids_gui python=3.9 pip
conda activate megbids_gui
mamba install --override-channels --channel=conda-forge mne
pip install PySimpleGUI mne_bids nibabel

```

# Test Data
```
mamba create -n datalad conda-forge::datalad
conda activate datalad
datalad install https://github.com/OpenNeuroDatasets/ds000248.git
datalad get ds000248.git
```

```
import mne, os
data_path = mne.datasets.sample.data_path()

meg_path = os.path.join(data_path, 'MEG','sample', 'sample_audvis_raw.fif')
mri_path = os.path.join(data_path, 'subjects','sample','mri','T1.mgz')
transform_path = os.path.join(data_path, 'subjects','sample','mri',        )
```