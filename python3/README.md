REXEG
=====
Per tenir nocions bàsiques.
```
import re
help(re)
```

## Aprendre
- `(?:a{6})*`

## Interès
- `re.X` mode verbós.

## Proves
- `'{([^{}]*({[^{}]*})*[^{}]*)}'`
> Funciona: `'hola { int v[] = {2,3,4}; return 0;}'`
> Falla: `{int l[][3][3] = {{{1,2,3},{2,3,4},{3,4,5}}, {{4,5,6},{5,6,7},{6,7,8}},{{7,8,9},{8,9,0},{9,0,0}}};}`
-

## Recursions
- [font](http://www.regular-expressions.info/recurse.html#balanced)
- [stack](https://stackoverflow.com/questions/546433/regular-expression-to-match-outer-brackets)
- Google: regex recursion python
- [font2 Egg](http://www.rexegg.com/regex-recursion.html)

# Informació Adicional REGEX
- [Sembla un tokenizer](https://docs.python.org/3.6/library/re.html#re-objects)

# Informació més adequada
- Google: tokenize python example
- [Crec que ja està](https://docs.python.org/3/library/tokenize.html)
- python -m tokenize <nomfitxer>
