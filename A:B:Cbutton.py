from microbit import *
def midiNoteOn(chan, n, vel):
    MIDI_NOTE_ON = 0x90
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_ON | chan, n, vel])
    uart.write(msg)
def midiNoteOff(chan, n, vel):
    MIDI_NOTE_OFF = 0x80
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_OFF | chan, n, vel])
    uart.write(msg)
def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)
Start()
lastA = False
lastB = False
lastC = False
BUTTON_A_NOTE = 35
BUTTON_B_NOTE = 39
BUTTON_C_NOTE = 43
while True:
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    c = pin1.is_touched()
    if a is True and lastA is False:
        midiNoteOn(0, BUTTON_A_NOTE, 127)
    elif a is False and lastA is True:
        midiNoteOff(0, BUTTON_A_NOTE, 127)
    if b is True and lastB is False:
        midiNoteOn(0, BUTTON_B_NOTE, 127)
    elif b is False and lastB is True:
        midiNoteOff(0, BUTTON_B_NOTE, 127)
    if c is True and lastC is False:
        midiNoteOn(0, BUTTON_C_NOTE, 127)
    elif c is False and lastC is True:
        midiNoteOff(0, BUTTON_C_NOTE, 127)

    lastA = a
    lastB = b
    lastC = c
    sleep(100)