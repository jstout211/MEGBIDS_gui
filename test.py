#!/usr/bin/env python
import PySimpleGUI as sg
import write_bids as wb

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Select the path to MEG .ds folder'), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Select the path to BIDS output directory'), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Type run number'), sg.InputText()],
    [sg.Text('Type session number'), sg.InputText()],
    [sg.Text('Type task name'), sg.InputText()],
    [sg.Text('Type bids subject'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    meg_ds_path = values[0]
    bids_root_path = values[1]
    run_num = values[2]
    session_num = values[3]
    task_name = values[4]
    bids_subj = values[5]

    if event == "Ok":
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
