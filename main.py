import os
import openpyxl
import TkEasyGUI as sg

layout_data = [
    [
        sg.Text('ファイルの場所'),
        sg.InputText(key='data'),
        sg.FileBrowse('開く', file_types=(('Excelファイル', '*.data'),))
    ],
    [sg.Text('読み込むシート'), sg.Listbox(values=['ファイルを開いてください'], key='sheets')]
]

layout_template = [
    [
        sg.Text('ファイルの場所'),
        sg.InputText(key='template'),
        sg.FileBrowse('開く', file_types=(("All Files", "*.pptx"),))
    ]
]

layout = [
    [sg.Frame('テンプレート', layout_template)],
    [sg.Frame('名前データ', layout_data)],
    [sg.Button('OK')]
]

window = sg.Window('名札クリエイター', layout)

while window.is_alive():
    event, values = window.read()

    if event == "OK":
        break
    elif event == 'data':
        if values['data'] == '':
            window['sheets'].update(values=["ファイルを開いてください。"])
        elif os.path.isfile(values['data']):
            wb = openpyxl.load_workbook(values['data'])
            window['sheets'].update(values=wb.sheetnames)
            wb.close()
        else:
            window['sheets'].update(values=["ファイルが存在しません。", "開き直してください。"])

window.close()
