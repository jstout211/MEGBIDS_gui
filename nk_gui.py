#!/usr/bin/env python
import PySimpleGUI as sg
import subprocess
import write_bids as wb

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter the path to mri'), sg.InputText()],
            [sg.Text('Enter the path to MEG .ds folder'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
            ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    sg.Popup("Welcome! In the next window, you will select the path to\
        your MEG .ds folder. You will also be prompted to specify naming convention.", keep_on_top=True)

    event, values = window.read()
    if event == "Ok":
        subprocess.run(f'freeview {values[0]}'.split(' '))
        wb.write_ctf_bids(values[1], run='01', session='0001', task='test',
                        bids_subject='tester', bids_root = '/Users/kuznetsovn2/Desktop')
        break
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
