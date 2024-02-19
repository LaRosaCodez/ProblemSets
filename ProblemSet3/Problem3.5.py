print("Enter the songs tempo:")
bpm = float(input())

print("Enter the duration of the song in seconds:")
songdurationseconds = int(input())

beatspersecond = bpm / 60

total_beats = 0

for second in range(1, songdurationseconds + 1):
    # Calculate beats played in current second
    beats_in_second = beatspersecond * second
    total_beats += beats_in_second
    print(f"At second {second}, Total beats: {beats_in_second:.2f} ")

print(f"Total number of beats in the song: {total_beats:.2f}")