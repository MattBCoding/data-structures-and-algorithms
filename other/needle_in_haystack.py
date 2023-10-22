# Finding a needle in a haystack


# Write a function find_needle() that takes a list full of junk but containing one "needle"
def find_needle(needle, haystack):
    needle_index = 0
    haystack_index = 0

    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True

            while needle_index < len(needle):
                if (
                    needle[needle_index]
                    != haystack[haystack_index + needle_index]
                ):
                    found_needle = False
                    break
                needle_index += 1

            if found_needle:
                return True
            needle_index = 0
        haystack_index += 1
    return False


# Test the function
needle = "def"
haystack = "abcdefghijklmnopqrstuvwxyz"
needle2 = "hello"


result = find_needle(needle, haystack)
print(result)
result = find_needle(needle2, haystack)
print(result)
