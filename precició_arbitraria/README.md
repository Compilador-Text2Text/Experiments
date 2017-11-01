Fent accés a l'alta precisió
============================

- [manual](https://gmplib.org/manual/)
- [oficial](http://gmplib.org/)

Codi
====
## Valors
- mpz enters
- mpq fraccions
- mpf floats

## Inicialitzar i acabar
- mpz\_init → valor 0
- mpz\_inits→ valor 0
- mpz\_clear	Allibera memòria
- mpz\_clears

## Definir valors
- mpz\_set (amb un mpz)
- mpz\_set\_ui	(unsigned int)
- mpz\_set\_si	(signed int)
- mpz\_set\_str	(string)

## Recuperar els valors
- mpz\_get\_[us]i
- mpz\_get\_str

## Operacions aritmètiques
- mpz\_add{\_ui}
- mpz\_sub{\_[us]i}
- mpz\_mul{\_[us]i}
- mpz\_neg
- mpz\_abs
- mpz\_[cft]div\_(qr|q|r){\_ui}
> - On c 'ceil' ↑
> - On f 'floor' ↓
> - On t 'truncate'
> - n=q\*d+r
- mpz\_mod
- mpz\_powm{\_ui}
- mpz\_root
- mpz\_sqrt
- mpz\_fac
- mpz\_cmp

## Funcions de sortida i entrada
- mpz\_out\_str
- mpz\_inp\_str
