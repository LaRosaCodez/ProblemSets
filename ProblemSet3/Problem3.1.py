
print("What is the song duration in seconds?")

number = int(input())

minute = number // 60
seconds = number % 60

print("The song is" , minute , "minutes and" , seconds , "seconds.")