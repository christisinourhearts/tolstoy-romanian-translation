# Tolstoi în românește

Traducere românească a operelor lui Lev Tolstoi, făcută direct din rusă, cu legătură
verificabilă către textul-sursă.

*A Romanian translation of Leo Tolstoy, made directly from the Russian and tied to the
audited source text by path and checksum. Companion to
[tolstoy-english-translation](https://github.com/christisinourhearts/tolstoy-english-translation).*

## Traduceri

- [Opere](translations/works/)
  - [*Evanghelia pe scurt*](translations/works/v24_801_938_Evanghelia_pe_scurt.md) (*Краткое изложение Евангелия*, 1881/1883), vol. 24, pp. 801–938
  - [*Stăpân și slugă*](translations/works/v29_003_046_Stapan_si_sluga.md) (*Хозяин и работник*, 1895), vol. 29, pp. 3–46

Depozitul conține în prezent **2 fișiere traduse**.

## Identitatea sursei

Fiecare traducere își păstrează în antetul YAML calea originală a textului rusesc
și suma de control SHA-256. Sursa este depozitul auditat
[tolstoy-russian-md](https://github.com/christisinourhearts/tolstoy-russian-md),
care rămâne doar pentru citire. Numele fișierelor păstrează prefixul de volum și
pagină al ediției de 90 de volume, urmat de titlul românesc fără diacritice.

## Reguli de traducere

Traducerea urmează aceleași principii ca proiectul englez (fidelitate conservatoare,
nicio omisiune, niciun adaos, fără înfrumusețare), cu reguli specifice limbii române.
Începeți cu:

- [`project/docs/TRANSLATION.md`](project/docs/TRANSLATION.md) — constituția traducerii
- [`project/docs/WORKBENCH.md`](project/docs/WORKBENCH.md) — starea curentă
- [`project/metadata/DECISIONS.md`](project/metadata/DECISIONS.md) — decizii editoriale
- [`project/metadata/NAMES.md`](project/metadata/NAMES.md) — transliterarea numelor
- [`project/translation_manifest.jsonl`](project/translation_manifest.jsonl)

Validare:

```sh
python project/tools/validate_translation.py /calea/catre/tolstoy-russian-md
```

Traducere de Andrei Evanghelușcă. Textele sunt publicate și pe
[christisinourhearts.com](https://christisinourhearts.com).
