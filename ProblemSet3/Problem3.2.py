print("Enter MIDI number between 0 and 127")
midinumber= int(input())

if 0 <= midinumber <= 127:
    frequency = 2 ** ((midinumber - 69) / 12) * 440       # MIDI to frequency equation
    print ("The frequency of the MIDI note", midinumber, "is", frequency, "Hz.")
else:
    print("number is invalid, please enter integer between 0 and 127")