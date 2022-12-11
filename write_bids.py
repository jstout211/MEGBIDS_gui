#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:00:47 2022

@author: stoutjd
"""
import mne_bids
from mne_bids import BIDSPath, write_anat
import mne
from mne_bids import write_raw_bids
import os
import subprocess

test_dir = "~/src/GUI_testdata/ds000248"
# if not os.path.exists(os.path.expanduser(test_dir)):
#     import openneuro
#     os.mkdir(os.path.dir())
#     openneuro.download(dataset='ds000248')


def write_ctf_bids(
    meg_fname, run=None, session=None, task=None, bids_subject=None, bids_root=None
):
    raw = mne.io.read_raw_ctf(meg_fname, system_clock="ignore")
    raw.info["line_freq"] = 60

    ses = session
    run = str(run)
    if len(run) == 1:
        run = "0" + run
    bids_path = BIDSPath(
        subject=bids_subject,
        session=session,
        task=task,
        run=run,
        root=bids_root,
        suffix="meg",
    )
    write_raw_bids(raw, bids_path, overwrite=True)


def read_meg(meg_fname):
    if meg_fname[-3:] == ".ds":
        return mne.io.read_raw_ctf(meg_fname)
    if meg_fname[-4:] == ".fif":
        return mne.io.read_raw_fif(meg_fname)


def write_mri_bids(
    meg_fname=None,
    mri_deface_fname=None,
    session=None,
    bids_subject=None,
    bids_root=None,
    transform_fname=None,
):
    raw = read_meg(meg_fname)
    trans = mne.read_trans(transform_fname)
    t1_path = mri_deface_fname

    t1w_bids_path = BIDSPath(
        subject=bids_subject, session=session, root=bids_root, suffix="T1w"
    )

    subjects_dir = os.environ["SUBJECTS_DIR"]
    tmp_subjects_dir = "/tmp/defaced_subjs_dir"
    if not os.path.exists(tmp_subjects_dir):
        os.mkdir(tmp_subjects_dir)
    os.environ["SUBJECTS_DIR"] = tmp_subjects_dir
    if not os.path.exists(os.path.join(tmp_subjects_dir, "tmp_defaced")):
        subprocess.run(
            f"recon-all -i {mri_deface_fname} -s tmp_defaced -autorecon1".split(" ")
        )

    landmarks = mne_bids.get_anat_landmarks(
        image=mri_deface_fname,
        info=raw.info,
        trans=trans,
        fs_subject="tmp_defaced",
        fs_subjects_dir=os.environ["SUBJECTS_DIR"],
    )

    # Write regular
    t1w_bids_path = write_anat(
        image=mri_deface_fname,
        bids_path=t1w_bids_path,
        landmarks=landmarks,
        overwrite=True,
    )
    os.environ["SUBJECTS_DIR"] = subjects_dir


def test_write_mri_bids():
    meg_fname = os.path.expanduser("~/src/GUI_testdata/sample_audvis_raw.fif")
    transform_fname = os.path.expanduser(
        "~/src/GUI_testdata/sample_audvis_trunc-trans.fif"
    )
    mri_deface_fname = "/tmp/deface/defaced_sub-01_T1w.nii.gz"
    session = "01"
    run = "01"
    bids_root = "/tmp/bids_root"
    bids_subject = "S01"
    write_mri_bids(
        meg_fname=meg_fname,
        mri_deface_fname="/tmp/deface/defaced_sub-01_T1w.nii.gz",
        session="01",
        bids_subject="S01",
        bids_root="/tmp/bids_root",
        transform_fname=transform_fname,
    )


def test_write_ctf_bids():
    test_ds = (
        "/home/stoutjd/src/GUI_testdata/sub-ON02747_ses-01_task-rest_run-01_meg.ds"
    )
    write_ctf_bids(
        test_ds,
        bids_subject="S01",
        run=1,
        session="01",
        task="rest",
        bids_root="/home/stoutjd/src/GUI_testdata/bids_path",
    )


# def test_write_mri_bids():
#     test_mri='/home/stoutjd/src
