# MEGBIDS_gui (Brainhack DC 2022 project)
Front end for converting MEG (+MRI T1) to bids.

# Background 
BIDS is becoming more prevalent in neuroimaging and allows for pipelines based on the standardized path structure.  Converting neurophsiological data to bids has become easier, but is still mainly a commandline driven process.  This hackathon project will build some initial GUI development into this process. <br><br>
mne_bids: https://mne.tools/mne-bids/stable/index.html <br>
mne: https://mne.tools/stable/index.html <br>

# PYQT Background
https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/

# Install QT6  
```
conda activate base
conda install conda-forge::mamba -y 

mamba create -n megbids_gui python=3.9 pip  #Currently pyqt6 only available for <=py3.9
conda activate megbids_gui
mamba install --override-channels --channel=conda-forge mne
pip install pyqt6 pyqt6-tools mne_bids pooch

#May be necessary to resolve ssl errors
mamba update libk4crpyto  
```

# Deply Qt Designer for layout
pyqt6-tools designer 

# Test Data
```
conda activate megbids_gui
ipython
```
```
import mne, os
data_path = mne.datasets.sample.data_path()

meg_path = os.path.join(data_path, 'MEG','sample', 'sample_audvis_raw.fif')
mri_path = os.path.join(data_path, 'subjects','sample','mri','T1.mgz')
transform_path = os.path.join(data_path, 'subjects','sample','mri', '
```


