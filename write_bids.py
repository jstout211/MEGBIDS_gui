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