def palindrome(m):
	if m[::-1]==m:
		print ("True")
	else:
		print("False")
print("please enter a string")
m=input()
palindrome(m)
