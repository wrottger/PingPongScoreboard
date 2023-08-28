import PySimpleGUI as sg
import serial
from serial.tools import list_ports
from serial import SerialException
from time import sleep

pA_Column = [
    [sg.Text("Player A", font=("Helvetica", 25))],
    [sg.Button("+1 A", size=(40, 15))],
    [sg.Button("-1 A", size=(40, 15))]
]

pB_Column = [
    [sg.Text("Player B", font=("Helvetica", 25))],
    [sg.Button("+1 B", size=(40, 15))],
    [sg.Button("-1 B", size=(40, 15))]
]

layout = [
    [
        sg.Column(pA_Column),
        sg.VSeperator(),
        sg.Column(pB_Column),
        sg.Button("reset")
    ]
]
# Create the window
window = sg.Window("PING PONG COUNTER", layout, size=(1500, 1000))

# Create an event loop

p1 = 0
p2 = 0


def get_com_ports():
    return [comport.device for comport in list_ports.comports()]


ser = serial.Serial(get_com_ports()[0], 9600, timeout=1)


def set_numbers(p1, p2):
    ser.write(f"{p1} {p2}\n".encode())
    print(f'{p1} {p2}')


while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    if event == "reset":
        p1 = 0
        p2 = 0
        set_numbers(p1, p2)

    if event == "+1 A":
        p1 += 1
        set_numbers(p1, p2)
    if event == "-1 A":
        p1 -= 1
        set_numbers(p1, p2)

    if event == "+1 B":
        p2 += 1
        set_numbers(p1, p2)
    if event == "-1 B":
        p2 -= 1
        set_numbers(p1, p2)

window.close()
