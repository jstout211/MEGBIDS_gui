#!/usr/bin/env python

import os
import subprocess

import PySimpleGUI as sg

import write_bids as wb

sg.theme("LightGrey3")  # Add a touch of color


def deface_mri(undefaced_mri_path):
    """Deface MRI and save out into temp directory.

    Args:
        undefaced_mri_path (str): path to mri that needs defacing

    Returns:
        str: path to defaced mri
    """

    fs_home = os.environ["FREESURFER_HOME"]
    face = os.path.join(fs_home, "average/face.gca")
    talairach = os.path.join(fs_home, "average/talairach_mixed_with_skull.gca")
    temp = "/tmp/deface"
    if not os.path.exists(temp):
        os.mkdir(temp)
    fname_local = os.path.basename(undefaced_mri_path)

    # establish path to defaced mri files
    defaced_mri_path = f"{temp}/defaced_{fname_local}"

    # check if they already exist, delete them if they do
    if os.path.exists(defaced_mri_path):
        os.remove(defaced_mri_path)
    cmd = f"mri_deface {undefaced_mri_path} {talairach} {face} {temp}/defaced_{fname_local}"
    subprocess.run(cmd.split(" "))

    return defaced_mri_path


def open_window(defaced_mri_path=None):
    """Called in main() to open Create BIDS window.

    Args:
        defaced_mri_path (str, optional): path to defaced MRI. Defaults to None.
    """

    layout = [
        [
            sg.Text(f"Path to defaced MRI:"),
            sg.InputText(defaced_mri_path),
            sg.FileBrowse(),
        ],
        [sg.Button("View Defaced MRI")],
        [
            sg.Text("Select the path to MEG .fif file"),
            sg.InputText(),
            sg.FolderBrowse(),
        ],
        # commented for demo purposes
        # [sg.Text('Select the path to MEG .ds folder'), sg.InputText(), sg.FolderBrowse()],
        [
            sg.Text("Select the path to Transform Matrix"),
            sg.InputText(),
            sg.FileBrowse(),
        ],
        [
            sg.Text("Select the path to BIDS output directory"),
            sg.InputText(),
            sg.FolderBrowse(),
        ],
        [sg.Text("Type bids subject"), sg.InputText()],
        [sg.Text("Type session number"), sg.InputText()],
        [sg.Text("Type task name"), sg.InputText()],
        [sg.Text("Type run number"), sg.InputText()],
        [sg.Button("Ok"), sg.Button("Cancel")],
    ]

    window = sg.Window("Create BIDS", layout, modal=True)

    while True:
        event, values = window.read()
        defaced_mri_path = values[0]

        if event == "Ok":
            window["Ok"].update(disabled=True)

            meg_ds_path = values[1]
            transform_matrix_path = values[2]
            bids_root_path = values[3]
            bids_subj = values[4]
            session_num = values[5]
            task_name = values[6]
            run_num = values[7]

            wb.write_ctf_bids(
                meg_ds_path,
                run=run_num,
                session=session_num,
                task=task_name,
                bids_subject=bids_subj,
                bids_root=bids_root_path,
            )

            wb.write_mri_bids(
                meg_fname=meg_ds_path,
                mri_deface_fname=defaced_mri_path,
                session=session_num,
                bids_subject=bids_subj,
                bids_root=bids_root_path,
                transform_fname=transform_matrix_path,
            )

            window["Ok"].update(disabled=False)
            sg.Popup("BIDS Complete!", keep_on_top=True)
            window.close()
            main()
        if event == "View Defaced MRI":
            subprocess.run(f"freeview {defaced_mri_path}".split(" "))
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    """Run main script."""

    layout = [
        [sg.Text("Select the path to MRI file"), sg.InputText(), sg.FileBrowse()],
        [
            sg.Button("Deface + Continue", key="open"),
            sg.Button("Skip"),
            sg.Button("Cancel"),
        ],
    ]
    window = sg.Window("Defacing MRI", layout)
    while True:
        event, values = window.read()

        undefaced_mri_path = values[0]
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "Skip":
            mri_path = ""
            window.close()
            open_window(mri_path)
        if event == "open":
            defaced_mri_path = deface_mri(undefaced_mri_path)  # deface the mri files
            window.close()
            open_window(defaced_mri_path)

    window.close()


def test_deface():
    """Test deface MRI script for pytest."""

    # TODO: MAKE undefaced_mri_path A GLOBAL VARIABLE
    defaced_mri = deface_mri(undefaced_mri_path)
    assert os.path.exists(defaced_mri)


if __name__ == "__main__":
    main()
