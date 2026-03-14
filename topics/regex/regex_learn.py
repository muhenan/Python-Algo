import re

"""

. (dot): Matches any single character except a newline.
*: Matches 0 or more repetitions of the preceding character or group.
+: Matches 1 or more repetitions of the preceding character or group.
?: Matches 0 or 1 repetition of the preceding character or group.
[]: Defines a character class. For example, [aeiou] matches any vowel.
| (pipe): Acts like a logical OR. For example, apple|orange matches either "apple" or "orange".

^: Matches the start of a string.
$: Matches the end of a string.

{n}: Matches exactly n repetitions.
{n,}: Matches n or more repetitions.
{n,m}: Matches between n and m repetitions.

\d: Matches any digit (0-9).
\D: Matches any non-digit character.
\w: Matches any word character (alphanumeric and underscore).
\W: Matches any non-word character.
\s: Matches any whitespace character.
\S: Matches any non-whitespace character.

"""

text = "I like apples and oranges."
pattern = "apple"
result = re.search(pattern, text)
if result:
    print("Found:", result.group())

else:
    print("Not found.")




text = "John's phone number is 123-456-7890."
pattern = "(\d{3})-(\d{3})-(\d{4})"
result = re.search(pattern, text)
if result:
    print("Full match:", result.group())
    print("Group 1:", result.group(1))
    print("Group 2:", result.group(2))
    print("Group 3:", result.group(3))

"""

re.search(pattern, string):

Searches for the first occurrence of the pattern in the string and returns a match object.
If a match is found, you can use the match object to extract information about the match.
re.match(pattern, string):

Similar to search, but it only matches at the beginning of the string.
If the pattern is not found at the beginning of the string, it returns None.
re.fullmatch(pattern, string):

Matches the entire string against the pattern. It should match from the start to the end.
If the entire string matches the pattern, it returns a match object; otherwise, it returns None.
re.findall(pattern, string):

Returns all non-overlapping matches of the pattern in the string as a list of strings.
It doesn't return match objects; instead, it returns the matched substrings.
re.finditer(pattern, string):

Returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.
You can loop through the iterator to access match objects and extract information about each match.
re.split(pattern, string):

Splits the string by the occurrences of the pattern and returns a list of substrings.
This is useful for tokenizing a string based on a specific pattern.
re.sub(pattern, replacement, string):

Replaces all occurrences of the pattern in the string with the replacement string.
Useful for performing find-and-replace operations in text.
re.subn(pattern, replacement, string):

Similar to sub, but it also returns the number of substitutions made.
re.compile(pattern):

Compiles a regular expression pattern into a regex object, which can be reused for multiple searches.
This can improve performance if you're using the same pattern multiple times.

"""



text = "The price of the item is $10.99, but the discount is $2.00."

# Find all the dollar amounts in the text
pattern = r'\$\d+\.\d{2}'
matches = re.findall(pattern, text)
print("Dollar amounts:", matches)
print(matches[1])



matches = re.search(pattern, text) # search only get the first matched one
print(matches.group())
print(matches.group(0))
