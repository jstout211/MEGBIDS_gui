#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:00:47 2022

@author: stoutjd
"""
import mne_bids
from mne_bids import BIDSPath
import mne
from mne_bids import write_raw_bids
import os


test_dir = '~/src/GUI_testdata/ds000248'
if not os.path.exists(os.path.expanduser(test_dir)):
    import openneuro
    os.mkdir(os.path.dir())
    openneuro.download(dataset='ds000248')
    

def write_ctf_bids(meg_fname, run=None, session=None, task=None,
                   bids_subject=None, bids_root=None):
    raw = mne.io.read_raw_ctf(meg_fname, system_clock='ignore')  
    raw.info['line_freq'] = 60 
    
    ses = session
    run = str(run) 
    if len(run)==1: run='0'+run
    bids_path = BIDSPath(subject=bids_subject, session=session, task=task,
                          run=run, root=bids_root, suffix='meg')
    write_raw_bids(raw, bids_path, overwrite=True)
    
# def write_mri_bids():
    
    
    
def test_write_ctf_bids():
    test_ds='/home/stoutjd/src/GUI_testdata/sub-ON02747_ses-01_task-rest_run-01_meg.ds'
    write_ctf_bids(test_ds, 
                   bids_subject='S01',
                   run=1,
                   session='01',
                   task='rest',
                   bids_root='/home/stoutjd/src/GUI_testdata/bids_path')
    
# def test_write_mri_bids():
#     test_mri='/home/stoutjd/src
                   