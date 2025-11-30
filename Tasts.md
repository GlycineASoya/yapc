# Tasks

## Library

Create a library! The program should support the following actions:
- lend a book
- return a book
- list all books managed by the library
- list all books available for lending
- list all books lended to a given client

Asking for an action can be done using the `input` built-in function.

## String parsing

Create a function `parse_string` in  Python that will convert a string into an integer. Examples:
- `parse_string("fifty three")` -> 53
- `parse_string("one hundred twenty six")` -> 126
- `parse_string("three hundred seventy six thousand eighty seven")` -> 376087

The function should be defined for all numbers between 1 and 999999 (inclusive). For other numbers or non-parseable arguments it should raise `ValueError`.

## String parsing #2

Implement another version of the `parse_string` function that will use an external module of your choice.
