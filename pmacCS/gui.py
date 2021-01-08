import PySimpleGUI as sg
import datetime
import time
import serial
import io
import codecs



# Create the layout
layout = [[sg.Text('Gap_RBV: '), sg.Text('', key='_gap_', size=(20, 1))],
         [sg.Text('Centre_RBV: '), sg.Text('', key='_centre_', size=(20, 1))],
         [sg.Text('Gap_DMD: '), sg.Input('',key='_gapDemand_') ],
         [sg.Text('Centre_DMD: '),sg.Input('',key='_cenDemand_')],
         [sg.Button('GO'), sg.Button('STOP'), sg.Quit()]]

# Create the window object
window = sg.Window('Simple Clock').Layout(layout)

gap_pos_limit = 180
gap_neg_limit = 0.5
cen_pos_limit = 10.0
cen_neg_limit = -10.0

def getTime():
    return datetime.datetime.now().strftime('%H:%M:%S')
    
def getQVar(port,var):
    #Flush
    port.reset_input_buffer()
    port.write(f'&2 Q{var}\r\n'.encode())
    port.flush()
    response = port.read_until(b'\r')
    
    #Flush
    port.reset_input_buffer()
    return float(response.strip(b'\x06'))
    
def executeMove(port,gap,cen):

    if gap > gap_pos_limit:
        gap = gap_pos_limit
    if gap < gap_neg_limit:
        gap = gap_neg_limit
    if cen > cen_pos_limit:
        cen = cen_pos_limit
    if cen < cen_neg_limit:
        cen = cen_neg_limit
       
    port.write(f'&2 Q78 = {gap}\r\n'.encode())
    port.flush()
    port.write(f'&2 Q77 = {cen}\r\n'.encode())
    port.flush()
    port.write(b'&2a\r\n')
    port.flush()
    port.write(b'&2b10r\r\n')
    port.flush()
    port.reset_input_buffer()
    
    
    
def main(gui_obj):
    
    synced = False
    # Event loop
    while True:
        event, values = gui_obj.Read(timeout=1000)
        #print(f'Moving {values[0]},{values[1]}\r')
            
        time.sleep(0.1)
        # Exits program cleanly if user clicks "X" or "Quit" buttons
        if event in (None,'Quit'):
            break
        if event == 'GO':
            print("go\r")
        if event == 'STOP':
            print("stop\r")


if __name__ == '__main__':
    main(window)