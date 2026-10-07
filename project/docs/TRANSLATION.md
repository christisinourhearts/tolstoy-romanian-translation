# Constituția traducerii românești

Acest fișier guvernează toată munca de traducere în română din acest depozit. Agenții și editorii umani trebuie să-l citească înainte de a modifica orice fișier.

Constituția preia, cu adaptări pentru română, principiile din `project/docs/TRANSLATION.md` al depozitului `tolstoy-english-translation`. Când cele două diferă, acest fișier guvernează traducerea românească.

## 1. Scop

O traducere românească completă și verificabilă a corpusului rusesc Tolstoi, păstrând o legătură permanentă, unu-la-unu, cu fișierele-sursă auditate.

Ținta este o română contemporană limpede, fidelă cuvintelor, gândirii, tonului, structurii și gradului de simplitate ale lui Tolstoi. Ținta nu este să imite româna veche, să-l „îmbunătățească” pe Tolstoi sau să-l facă mai literar decât este.

## 2. Ierarhia surselor

1. Tolstoy Digital TEI/XML este sursa de arhivă.
2. `tolstoy-russian-md` (auditat) este stratul Markdown folosit pentru traducere și comparație.
3. Fișierul românesc este un derivat legat de un singur fișier rusesc exact, prin cale relativă și SHA-256.

**Se traduce întotdeauna din rusă.** Traducerea engleză din `tolstoy-english-translation` poate fi folosită ca aliniere de control (pentru a verifica dacă nu s-a omis nimic), dar nu este niciodată sursa. Unde româna și engleza diferă, decide rusa.

## 3. Identitate și structură

Fișierele se păstrează în `translations/` în aceleași categorii ca proiectul englez: `works`, `letters`, `diaries`, `notes`, `primer`, `circle_of_reading`. Numele fișierului folosește prefixul volum/pagină al ediției tipărite, urmat de titlul românesc fără diacritice.

```text
Sursă rusă:  corpus/works/v29_003_046_Hozjain_i_rabotnik.md
Română:      translations/works/v29_003_046_Stapan_si_sluga.md
```

Antetul YAML păstrează `source_ru_path`, `source_ru_sha256` și, când există, `english_companion`.

Marcajele de pagină se păstrează exact și în aceeași ordine:

```md
<!-- vol. 29, p. 3 -->
```

Se păstrează ierarhia titlurilor, citatele, versurile, tabelele, marcajele de ștergere/adăugare și identificatorii notelor de subsol.

## 4. Reguli de fidelitate

- Se traduce fiecare parte substanțială a sursei. Nimic nu se omite pentru că e repetitiv, stângaci sau aparent neimportant.
- Nu se adaugă în text explicații pe care Tolstoi nu le-a scris.
- Nu se intensifică emoția, judecata morală, imaginile sau retorica.
- Nu se netezește repetiția semnificativă.
- Nu se rezolvă pe tăcute ambiguitatea reală din rusă.
- Se păstrează diferențele dintre certitudine, probabilitate, zvon, ironie, citat și presupunere.
- Se verifică toate numele, cifrele, datele, măsurile, trimiterile biblice și citatele.
- Schimbările de timp, persoană și punct de vedere se păstrează când au sens (de pildă trecerea la prezent în visul și moartea lui Vasili Andreici).

## 5. Stilul românesc

Postura implicită este **fidelitatea conservatoare** (decizia D0001, preluată din proiectul englez): când o redare apropiată este limpede în română, se păstrează cuvintele concrete, imaginile, repetițiile și întorsăturile neobișnuite ale sursei.

- Diacriticele se scriu cu virgulă dedesubt: **ș, ț, Ș, Ț** — niciodată cu sedilă (ş, ţ). Se folosesc **â** și **î** după normele actuale.
- Dialogul se marchează cu linie de dialog (—), ca în rusă; incisele („spuse el”) se despart prin virgulă, fără a doua linie, după uzul românesc obișnuit.
- Gândurile și citatele în text se pun între ghilimele românești „…”.
- Narațiunea se scrie la **perfectul compus**, ca în povestirile românești de pe christisinourhearts.com, gândite pentru lectura cu voce tare (D0004). Imperfectul și mai-mult-ca-perfectul se păstrează acolo unde arată durata sau ordinea acțiunilor, iar trecerile lui Tolstoi la prezent se păstrează. Perfectul simplu se folosește doar când o ediție anume o cere și decizia este înregistrată.
- Graiul personajelor țărănești se sugerează discret (*păi*, *las’ că*, *nenică*), fără să se imite un anumit grai regional românesc.
- Nu se înlocuiesc realiile rusești cu echivalente românești care ar muta acțiunea (o *isbă* rămâne casă țărănească, nu „bordei”; *verstă*, *stânjen*, *desetină*, *rublă*, *copeică* rămân).
- Se evită arhaismele fără motiv textual și neologismele care sună anacronic.

## 6. Vocabularul recurent

Termenii lui Tolstoi nu se traduc mecanic, dar se urmăresc deliberat (vezi `project/metadata/TERMINOLOGY.md`): насилие, зло, добро, совесть, разум, вера, дух, душа, жизнь, любовь, закон, власть, истина / правда.

## 7. Nume și forme de adresare

Transliterarea urmează uzul românesc consacrat pentru Tolstoi și este înregistrată în `project/metadata/NAMES.md`:

| Rusă | Română | Exemplu |
|---|---|---|
| ё | io | Семён → Semion, Фёдор → Fiodor |
| е inițial / după vocală | e | Ефим → Efim, Матвеев → Matveev |
| ж | j | |
| х | h | Брехунов → Brehunov |
| ч | ci / ce | Андреич → Andreici, Молчановка → Molceanovka |
| ш / щ | ș / șci | Гришкино → Grișkino |
| ы | î | Мухортый → Muhortîi, Карамышево → Karamîșevo |
| я | ia / ea | Телятино → Teleatino, Горячкино → Goriacikino |
| ю | iu | |
| й final | i | Василий → Vasili |

Patronimicele contrase se păstrează cum le scrie Tolstoi (Andreici, nu Andreevici; Stepanîci, nu Stepanovici). Diminutivele (Nikitușka, Arinușka, Petrușka) și formele populare (Mikit, Mikita, Mikolavna) se păstrează.

## 8. Note de subsol și aparat editorial

Ca în proiectul englez: `translation_status` urmărește textul lui Tolstoi, `apparatus_translation_status` aparatul editorial. O afirmație a editorului nu se transformă niciodată în vocea lui Tolstoi.

## 9. Variante, ciorne și text neterminat

Se traduce starea reală a textului. Nu se reconstruiește o versiune „terminată” ipotetică.

## 10. Protocolul de sursă suspectă

Se aplică întocmai protocolul `SOURCE_SUSPECTED` din constituția engleză (§11). Înregistrările se țin în `project/qa/source_suspected/`. Depozitul rusesc nu se corectează niciodată pe tăcute. Când aceeași unitate a fost deja examinată în proiectul englez, înregistrarea se copiază și se citează.

## 11. Dovada de acoperire bilingvă

Fiecare unitate acceptată are o înregistrare structurată în `project/qa/coverage/`, cu aceleași câmpuri ca în proiectul englez: metoda (`exhaustive_source_to_target_pass`), omisiuni cunoscute (de regulă zero), adaosuri nesusținute (de regulă zero), nume/cifre/date verificate, structură verificată, ambiguități, rezultat (`PASS`, `NEEDS_REVIEW`, `SOURCE_SUSPECTED`).

Verificarea pornește de la rusă spre română, apoi se face o trecere inversă, de la română spre rusă, după explicații adăugate, intensificări sau sensuri fără sprijin în sursă. Numărătorile mecanice (paragrafe, marcaje) sunt doar semnale de avertizare.

## 12. Fluxul de lucru

1. **Traducere** — din sursa rusă auditată.
2. **Audit de fidelitate** — rusă față de română.
3. **Revizie** — corectarea problemelor dovedite.
4. **Redactare românească** — citirea textului ca text românesc; eliminarea calcurilor și a stângăciilor accidentale, fără libertăți noi.
5. **Audit final de sursă / dovadă de acoperire.**
6. **Validare mecanică** — `project/tools/validate_translation.py`.
7. **Commit** — actualizarea manifestului și a `WORKBENCH.md`.

O verificare făcută de același model în același context nu se prezintă ca verificare independentă.

## 13. Schimbarea regulilor

Regulile se îmbunătățesc când exemple reale arată că sunt nepotrivite. Schimbările importante se înregistrează în `project/metadata/DECISIONS.md` și în Git.
