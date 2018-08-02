# Character Sets
- -v is the complement for grep ie. `grep -v "blah" somefile` and returns the inverse of the matches (non-matches)
- most matchers such as the word matcher \w, digits \d, and spaces (\s, \t, \n) have an inverse which is the capatilized version eg. \W, \D, \S
- regex inside parens is called a 'capture group'
- quantifiers are denoted with {1} or some other number and defines how many repeats of a pattern to look for, you can specify a range with {n1, n2}
- specify a set with brackets ie. [aeiou]
- if you want to get the complement of a set, you can put a caret at the begining ie. [^aeiou] defines all consonants

