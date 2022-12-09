# MEGBIDS_gui (Brainhack DC 2022 project)
Front end for converting MEG (+MRI T1) to bids.

# Install QT6  
```
conda activate base
conda install conda-forge::mamba -y 

mamba create -n megbids_gui python=3.9 pip  #Currently pyqt6 only available for <=py3.9
conda activate megbids_gui
mamba install --override-channels --channel=conda-forge mne
pip install pyqt6 pyqt6-tools mne_bids

#May be necessary to resolve ssl errors
mamba update libk4crpyto  
```

# Deply 
pyqt6-tools designer 
