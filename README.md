## Add

1. Function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

- modify add to accept and "add" any number of lists-of-lists.
- raise a ValueError if the given lists-of-lists aren't all the same shape.


## Circle

2. Class that represents a circle. The circle should have a radius, a diameter, and an area. It should also have a nice string representation.

- additionally the radius should default to 1 if no radius is specified when creating a circle
- make sure when the radius of class changes that the diameter and area both change as well
- make sure to set the diameter attribute and the radius will update accordingly
- make sure that you cannot set the area (setting area should raise an AttributeError)
- make sure radius cannot be set to a negative number. Raise a ValueError exception with the error message "Radius cannot be negative".


## Starting with a vowel

3. Function that accepts a list of names and returns a new list containing all names that start with a vowel.


## Power List By Index

4. Function that accepts a list of numbers and returns a new list that contains each number raised to the i-th power where i is the index of that number in the given list.


## Flatten a Matrix

5. Funtion that will take a matrix (a list of lists) and return a flattened version of the matrix.


## Reverse Difference

6. Function that accepts a list of numbers and returns a new copy of the list with the reverse of the list subtracted.


## Transpose

7. Function that accepts a list of lists and returns the transpose of the list of lists.


## Factors

8. The function get_factors returns the factors of a given number.


## Pythagorean Triples

9. Function that takes a number and returns a list of tuples of 3 integers where each tuple is a Pythagorean triple, and the integers are all less then the input number. A Pythagorean triple is a group of 3 integers a, b, and c, such that they satisfy the formula a**2 + b**2 = c**2.


## Primality

10. Funtion that returns True if a number is prime and False otherwise.


## All Together

11. Function that takes any number of iterables and strings them together.


## Interleave

12. Function that accepts two iterables and returns a generator object with each of the given items "interleaved" (item 0 from iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).


## Transliteration

13. Function that takes a string in one language and transliterates each word into another language, returning the resulting string.


## Parse Number Ranges

14. Function that accepts a string containing ranges of numbers and returns a generator of the actual numbers contained in the ranges. The range numbers are inclusive.


## Primes Over

15. Function that returns a first prime number over a given number.


## Anagrams

16. Function that accepts two strings and returns True if the two strings are anagrams of each other. The function should also ignore spaces and punctuation.


## Flipped Dictionary

17. Function that flips dictionary keys and values.


## ASCII Strings

18. Function that accepts a list of strings and returns a dictionary containing the strings as keys and a list of corresponding ASCII characters codes as values.


## Double-valued Dictionary

19. Function that accepts a list of three-item tuples and returns a dictionary where the keys are the first item of each tuple and the values are a two-tuple of the remaining two items of each input tuple.


## Multi-valued Dictionary 

20. Edit the function dict_from_tuple by starting with the code from dict_from_tuple function, above, and modify it to accept a list of tuples of any length and return a dictionary which uses the first item of each tuple as keys and all subsequent items as values.


## All Factors

21. Function that takes a set of numbers and makes a dictionary containing the numbers as keys and a list of factors as values


## Matrix From String

22. Function that accepts a string and returns a list of lists of integers (found in the string).


## Atbash Cipher

23. Implementation of the Atbash Cipher, an ancient encryption system created in the Middle East. 

The Atbash Cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such that resulting aplhabet is backwards. The first letter is replaced with the last letter, the second wih the second-last, and so on.

An Atbash Cipher for the Latin alphabet would be as follows:

- Plain: abcdefghijklmnopqrstuvwxyz
- Cipher: zyxwvutsrqponmlkjihgfedcba

Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, and punctuation is excluded. This is to make it harder to guess things based on word boundaries.

- Encoding test gives gvhg
- Decoding gvhg gives test
- Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog


## Memory-efficient CSV

24. Function that accepts a file object which contains a CSV file (including a header row) and returns a list of namedtuples representing each row.