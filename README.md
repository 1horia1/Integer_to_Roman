# Roman Numerals Converter

## Description
This program converts Arabic numbers (decimal numbers) into Roman numerals based on standard conversion rules.

## Roman Numeral Symbols

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

## Conversion Rules
1. If the value does not start with 4 or 9, select the largest symbol that can be subtracted from the number, append it to the result, subtract its value, and convert the remainder.
2. If the value starts with 4 or 9, use the subtractive notation:
   - 4 → IV (5 - 1)
   - 9 → IX (10 - 1)
   - 40 → XL (50 - 10)
   - 90 → XC (100 - 10)
   - 400 → CD (500 - 100)
   - 900 → CM (1000 - 100)
3. Only powers of 10 (I, X, C, M) can be repeated up to three times. Symbols like V, L, and D cannot be repeated.

## Examples

### Example 1
**Input:** `num = 3749`

**Output:** `MMMDCCXLIX`

**Explanation:**
- 3000 = MMM
- 700 = DCC
- 40 = XL
- 9 = IX

### Example 2
**Input:** `num = 58`

**Output:** `LVIII`

**Explanation:**
- 50 = L
- 8 = VIII

### Example 3
**Input:** `num = 1994`

**Output:** `MCMXCIV`

**Explanation:**
- 1000 = M
- 900 = CM
- 90 = XC
- 4 = IV

## Usage
To use the program, provide an integer, and it will return the corresponding Roman numeral.


