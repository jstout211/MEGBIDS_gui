#!/usr/bin/env python
import os
import PySimpleGUI as sg
import write_bids as wb
import subprocess

sg.theme('LightGrey3')   # Add a touch of color
# All the stuff inside your window.

def open_window(defaced_mri_path = None):
    layout = [[sg.Text("New Window", key="new")]]
    layout = [
                [sg.Text(f"Path to defaced MRI:"), sg.InputText(defaced_mri_path), sg.FileBrowse()],
                [sg.Text('Select the path to MEG .ds folder'), sg.InputText(), sg.FolderBrowse()],
                [sg.Text('Select the path to Transform Matrix'), sg.InputText(), sg.FileBrowse()],
                [sg.Text('Select the path to BIDS output directory'), sg.InputText(), sg.FolderBrowse()],
                # [sg.Text('Select the path to mri file'), sg.InputText(), sg.FileBrowse()],
                [sg.Text('Type run number'), sg.InputText()],
                [sg.Text('Type session number'), sg.InputText()],
                [sg.Text('Type task name'), sg.InputText()],
                [sg.Text('Type bids subject'), sg.InputText()],
                # [sg.Button('Deface')],
                [sg.Button('Ok'), sg.Button('Cancel')]
            ]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        defaced_mri_path = values[0]
        meg_ds_path = values[1]
        transform_matrix = values[2]
        bids_root_path = values[3]
        run_num = values[4]
        session_num = values[5]
        task_name = values[6]
        bids_subj = values[7]

        # fs_home = os.environ["FREESURFER_HOME"]
        # face = os.path.join(fs_home, "average/face.gca")
        # talairach = os.path.join(fs_home, "average/talairach_mixed_with_skull.gca")
        # temp = "/tmp/deface"
        # if not os.path.exists(temp): os.mkdir(temp)
        # fname_local=os.path.basename(button_mri)
        # cmd = f"mri_deface {button_mri} {talairach} {face} {temp}/defaced_{fname_local}"
        # subprocess.run(cmd.split(" "))
        # # subprocess.run(f"freeview {temp}/defaced_{fname_local}".split(' '))
        # button_mri = f"{temp}/defaced_{fname_local}"

        wb.write_ctf_bids(
            meg_ds_path,
            run=run_num,
            session=session_num,
            task=task_name,
            bids_subject=bids_subj,
            bids_root=bids_root_path
        )

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break

    window.close()


def main(): # Main Window
    layout = [[sg.Text('Select the path to mri file'), sg.InputText(), sg.FileBrowse()],
            [sg.Button('Skip'), sg.Button("Deface + Continue", key="open"), sg.Button('Cancel')]
            ]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()

        button_mri = values[0]
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "Skip": 
            mri_path = '' 
            open_window(mri_path)
        if event == "open":
            # deface the mri files
            fs_home = os.environ["FREESURFER_HOME"]
            face = os.path.join(fs_home, "average/face.gca")
            talairach = os.path.join(fs_home, "average/talairach_mixed_with_skull.gca")
            temp = "/tmp/deface"
            if not os.path.exists(temp): os.mkdir(temp)
            fname_local=os.path.basename(button_mri)
            cmd = f"mri_deface {button_mri} {talairach} {face} {temp}/defaced_{fname_local}"
            subprocess.run(cmd.split(" "))
            subprocess.run(f"freeview {temp}/defaced_{fname_local}".split(' '))
            mri_path = f"{temp}/defaced_{fname_local}"
            open_window(mri_path)

    window.close()

if __name__ == "__main__":
    main()
