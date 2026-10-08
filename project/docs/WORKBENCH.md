# Workbench

Registrul de predare. O sesiune nouă citește, în ordine:

1. `project/docs/TRANSLATION.md`
2. `project/metadata/DECISIONS.md`
3. `project/docs/WORKBENCH.md`
4. `project/translation_manifest.jsonl`

## Sursa

Depozit rusesc: `christisinourhearts/tolstoy-russian-md` (doar pentru citire). Fiecare unitate fixează calea și SHA-256 a fișierului-sursă.

## Lucrări încheiate

### R001.01 — *Stăpân și slugă* (2026-10-07)

- Sursa: `corpus/works/v29_003_046_Hozjain_i_rabotnik.md` (vol. 29, pp. 3–46), SHA-256 `1e5299b6…0faf0d`.
- Fișier: `translations/works/v29_003_046_Stapan_si_sluga.md` (~17.400 de cuvinte).
- Însoțitor englez: `tolstoy-english-translation`, `translations/works/v29_003_046_Master_and_Man.md`.
- 44/44 marcaje de pagină în ordine; 409/409 paragrafe aliniate cu sursa și cu engleza.
- Înregistrare de acoperire: PASS. Șapte artefacte de transcriere nesubstanțiale, aceleași ca în proiectul englez, sunt în `project/qa/source_suspected/`.
- Tradusă, auditată și redactată de același model într-un singur context; se recomandă o lectură independentă (de preferat a unui vorbitor nativ de română care citește rusa) înainte de tipărire.

### R002.01 — *Evanghelia pe scurt* (2026-10-08)

- Sursa: `corpus/works/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.md` (vol. 24, pp. 801–938, 1881/1883), SHA-256 `87ff4a14…abf203`.
- Fișier: `translations/works/v24_801_938_Evanghelia_pe_scurt.md` (~55.500 de cuvinte românești; sursa are ~47.500).
- Fără însoțitor englez: traducerea engleză a aceleiași unități se făcea în paralel, deci nu a existat aliniere de control (D0002).
- 138/138 marcaje de pagină în ordine (133 în interiorul paragrafelor); 1627/1627 paragrafe și titluri aliniate cu sursa, scheletul de rânduri identic.
- Înregistrare de acoperire: PASS. Treizeci și două de constatări în `project/qa/source_suspected/`: greșeli de tipar citite corect, trimiteri biblice greșite păstrate, citatul francez din prefață și o lectură posibil greșită («вражды», In 6:35) de verificat pe ediția tipărită.
- Decizii noi: D0005 (titlul), D0006 (termenii-cheie: înțelegere, spirit, ispită/ispitire, fiul omului, voia tatălui), D0007 (textele evanghelice după Tolstoi, nu după o Biblie românească), D0008 (anacronismele și realiile), D0009 (greșelile de tipar).
- Tradusă, auditată și redactată de același model într-un singur context; se recomandă o lectură independentă (de preferat a unui vorbitor nativ de română care citește rusa) și compararea cu traducerea engleză, când va fi gata.
- **Audit independent la rece (2026-10-08)**, ramura `gospel-in-brief-cold-audit`, raport `project/qa/reports/R002_COLD_AUDIT.md`: textul întreg recitit paragraf cu paragraf, de la rusă, într-un context nou. 59 de constatări corectate (78 de înlocuiri pe 69 de rânduri; un commit pe capitol): 1 omisiune, 3 adaosuri, 15 sensuri inversate sau deplasate (între care «пока» = «până să» în Mt 25:5, 10, temerea din In 13:38 făcută poruncă, întrebarea din In 9:19 făcută afirmație), 6 terminologie, 2 alunecări spre Biblie («масло» = «mir» de 14 ori, acum «untdelemn»; «a se blestema» din Cornilescu, Mt 26:74), 4 netezeri, 28 de limbă română; 0 trimiteri greșite. **Verdict: PASS AFTER REVISION.**
- Verificarea «вражды» (In 6:35, p. 856) pe vol. 24 tipărit: **confirmată** pe o scanare a p. 856 trimisă de proprietarul proiectului (gazdele cu scanări erau blocate în mediul auditului); tiparul și TEI au «вражды». Româna «dușmănia» rămâne; înregistrarea e închisă.
- `TERMINOLOGY.md` completat după audit: масло / мѵро, злоба, возвысить / возвеличить, выпытывать, сойтись.

## Starea corpusului

- Fișiere traduse și revizuite: **2**.

## URMĂTOAREA ACȚIUNE

1. Lectură independentă a *Stăpân și slugă*. Pentru *Evanghelia pe scurt* auditul la rece este făcut (`R002_COLD_AUDIT.md`); rămân: lectura unui vorbitor nativ de română care citește rusa și alinierea de control cu traducerea engleză după ce va fi publicată.
2. Următoarele unități se aleg în funcție de ce se publică pe christisinourhearts.com; paginile românești existente ale site-ului (de ex. *Doi bătrâni*, *Ilyas*) pot fi aduse în depozit ca unități noi, fiecare cu propria înregistrare de acoperire.
