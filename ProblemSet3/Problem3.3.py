print("Enter BPM:")
BPM = int(input())

if 1 <= BPM:
    interval = 60000 // BPM
    print("A quarter note delay in milliseconds for", BPM, "BPM is", interval, "milliseconds.")
else:
    print("Please enter a value above 1.")

# Included else statement as to not calculate "negative" BPM's