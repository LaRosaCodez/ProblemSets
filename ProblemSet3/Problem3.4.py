print("Enter song duration in minutes:")
duration = int(input())

if 0 <= duration < 2:
    print("Short Song")
if 2 <= duration < 4:
    print("Medium Song")
if 4 <= duration:
    print("Long Song")