#!/usr/bin/env python
import os
import PySimpleGUI as sg
import write_bids as wb
import subprocess

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Select the path to MEG .ds folder'), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Select the path to BIDS output directory'), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Select the path to mri file'), sg.InputText(), sg.FileBrowse()],
    [sg.Text('Type run number'), sg.InputText()],
    [sg.Text('Type session number'), sg.InputText()],
    [sg.Text('Type task name'), sg.InputText()],
    [sg.Text('Type bids subject'), sg.InputText()],
    [sg.Button('Deface')],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    sg.Popup("Welcome! In the next window, you will select the path to\
        your MEG .ds folder. You will also be prompted to specify naming convention.", keep_on_top=True)
        
    event, values = window.read()
    meg_ds_path = values[0]
    bids_root_path = values[1]
    button_mri = values[2]
    run_num = values[3]
    session_num = values[4]
    task_name = values[5]
    bids_subj = values[6]
    # button_val = values[7]

    if event == "Deface":
        # deface the mri files
        fs_home = os.environ["FREESURFER_HOME"]
        face = os.path.join(fs_home, "average/face.gca")
        talairach = os.path.join(fs_home, "average/talairach_mixed_with_skull.gca")
        temp = "/tmp/deface"
        if not os.path.exists(temp): os.mkdir(temp)
        cmd = f"mri_deface {button_mri} {talairach} {face} {temp}/defaced_{button_mri}"
        subprocess.run(cmd.split(" "))
        subprocess.run(f"freeview {temp}/defaced_*.nii.gz")

    if event == "Ok":
        # MEG Component
        wb.write_ctf_bids(
            meg_ds_path,
            run=run_num,
            session=session_num,
            task=task_name,
            bids_subject=bids_subj,
            bids_root=bids_root_path
        )
        break
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

def test_deface():
    button_mri = os.path.expanduser('~/src/GUI_testdata/sub-ON02747_ses-01_anat.nii.gz')
    fs_home = os.environ["FREESURFER_HOME"]
    face = os.path.join(fs_home, "average/face.gca")
    talairach = os.path.join(fs_home, "average/talairach_mixed_with_skull.gca")
    temp = "/tmp/deface"   
    if not os.path.exists(temp): os.mkdir(temp)
    cmd = f"mri_deface {button_mri} {talairach} {face} {temp}/defaced_{button_mri}"
    subprocess.run(cmd.split(" "))