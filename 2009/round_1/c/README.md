You can find the original question [here](https://code.google.com/codejam/contest/189252/dashboard#s=p0)

Just in case the question is removed, the question is:

#Problem

In A.D. 2100, aliens came to Earth. They wrote a message in a cryptic language, and next to it they wrote a series of symbols. We've come to the conclusion that the symbols indicate a number: the number of seconds before war begins!

Unfortunately we have no idea what each symbol means. We've decided that each symbol indicates one digit, but we aren't sure what each digit means or what base the aliens are using. For example, if they wrote "ab2ac999", they could have meant "31536000" in base 10 -- exactly one year -- or they could have meant "12314555" in base 6 -- 398951 seconds, or about four and a half days. We are sure of three things: the number is positive; like us, the aliens will never start a number with a zero; and they aren't using unary (base 1).

Your job is to determine the minimum possible number of seconds before war begins.

#Input

The first line of input contains a single integer, **T**. **T** test cases follow. Each test case is a string on a line by itself. The line will contain only characters in the 'a' to 'z' and '0' to '9' ranges (with no spaces and no punctuation), representing the message the aliens left us. The test cases are independent, and can be in different bases with the symbols meaning different things.

# Output

For each test case, output a line in the following format:

    Case #X: V

Where X is the case number (starting from 1) and V is the minimum number of seconds before war begins.

## Limits

1 ≤ T ≤ 100
The answer will never exceed 10<sup>18</sup>
Small dataset

1 ≤ the length of each line < 10

Large dataset

1 ≤ the length of each line < 61

# Sample

| input    | output       |
| -------- | ------------ |
| 3<br>11001001<br>cats<br>zig | Case #1: 201<br>Case #2: 75<br>Case #3: 11<br> |
