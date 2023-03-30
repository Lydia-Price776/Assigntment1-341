# Assignment 1 159.341
Write a parser/interpreter for a simple, imperative string-processing language.

This paser/interpreter can be run from the `main` file

Please see the `requirements.txt` for the required modules 
### Grammar:
```
program    := { statement }
statement  :=
           | append id expression end list end
           | exit end
           | print expression end 
           | printlength expression end 
           | printwords expression end 
           | printwordcount expression end 
           | set id expression end 
           | reverse id end
expression :=
value := id | constant | literal
```

### Tokens:

```
  append            = append
  exit              = exit 
  list              = list
  print             = print
  printlength       = printlength 
  printwords        = printwords
  printwordcount    = printwordcount
  reverse           = reverse
  set               = set
  constant          = SPACE|TAB|NEWLINE
  end               = ;
  plus              = + 
  id                = [a-zA-Z][a-zA-Z0-9]*
  literal           = (["])([^\\]*?(?:\\.[^\\]*?)*)(["])
```