import PySimpleGUI as sg

class GUI:

    def __init__(self,win_title,text,_type='main',persistance=False,result='') -> None:
        if(_type=='main'):
            layout = self.main_display(text)
        elif(_type == 'initial'):
            layout = self.mode_display(text)
        elif(_type == 'Translate'):
            layout = self.translation(text,persistance,result)

        window = sg.Window(win_title, layout)
        self.event, self.values = window.read()
        window.close()

    def main_display(self,text):
        layout = [[sg.Text(text)],
                  [sg.Button('Translate')], 
                  [sg.Button('Ask something to AI')],
                  [sg.Button('Check grammar')],
                  [sg.Button('Exit')]]
        return layout
        
    def mode_display(self,text):
        layout = [[sg.Text(text)],
                  [sg.Button('Console')], 
                  [sg.Button('Application')],
                  [sg.Button('Exit')]]
        return layout
    def translation(self,text,persistance,result):
        if(persistance):
            layout = [[sg.Text(text)],[sg.InputText()],
                      [sg.Text(result)], 
                    [sg.Button('Translate'),sg.Button('Menu'), sg.Button('Exit')]]
        else:
            layout = [[sg.Text(text)],[sg.InputText()], 
                    [sg.Button('Translate'),sg.Button('Menu'), sg.Button('Exit')]]
        return layout
