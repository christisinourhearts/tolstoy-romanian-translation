# R002.01 — Audit independent la rece: *Evanghelia pe scurt*

## English summary

An independent cold fidelity audit of `translations/works/v24_801_938_Evanghelia_pe_scurt.md` against the Russian source `corpus/works/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.md` (SHA-256 `87ff4a14…abf203`, verified before work began). Scope: the **whole text** — preface, introduction, chapters I–XII and conclusion — read paragraph by paragraph, Russian first, with all 1,627 paragraphs and headings paired line by line. The auditor had not seen the translation before and worked in a fresh context.

**59 findings** were confirmed and fixed (78 edits on 69 lines). Most are Romanian-language slips (agreement, broken idioms, russianisms). The meaningful ones are: two places where «până să» (*before*) reversed Tolstoy's «пока» (*while*) in the parable of the ten virgins; Peter's apprehensive «как бы … не отрекся» turned into a command; a question in Jn 9:19 turned into a statement; «добро» (*goods*) read as «bunătate» (*kindness*); «жалеть для» read as «a regreta»; and a Bible-version slippage — Tolstoy's plain «масло» (*oil*) was rendered 14 times as «mir», the Synodal/Cornilescu *myrrh*, although Tolstoy himself distinguishes «масло» from «мѵро» in ch. X. No omitted sentences or clauses were found beyond one concessive particle; no verse reference or number was miscopied.

The print check of «вражды» (Jn 6:35) is **confirmed**. The scan hosts (tolstoy.ru, rusneb.ru, archive.org, ru.wikisource.org, tolstoy-lit.ru) were blocked in the audit environment, but the project owner supplied a scan of printed vol. 24, p. 856, and it reads «…тот не будет никогда знать вражды.» The TEI archive reads the same. The source text is correct as transcribed and the Romanian «dușmănia» stands.

**Verdict: PASS AFTER REVISION.**

| Category | Count |
|---|---|
| omissions | 1 |
| additions | 3 |
| reversals / shifted meaning | 15 |
| references | 0 |
| terminology | 6 |
| Bible-version slippage | 2 |
| embellishment / smoothing | 4 |
| Romanian language | 28 |
| **total** | **59** |

---

## 1. Domeniu și metodă

- **Sursa:** `tolstoy-russian-md/corpus/works/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.md`, SHA-256 `87ff4a14066b3250011bb748bb10f8fc754e5eef251af4b75de1320d82abf203` — verificat înainte de începerea lucrului; identic.
- **Ținta:** `translations/works/v24_801_938_Evanghelia_pe_scurt.md` de pe ramura `gospel-in-brief` (commit `f9e5254`).
- **Domeniu: textul întreg**, fără eșantionare — prefața, introducerea, capitolele I–XII și încheierea. Scheletul de rânduri al celor două fișiere este identic (decalaj constant de 8 rânduri de antet), așa că fiecare paragraf rusesc a fost citit alături de paragraful românesc corespunzător, de la rusă spre română, apoi românește, ca text de sine stătător.
- **Standard:** `project/docs/TRANSLATION.md`, `DECISIONS.md` (D0001–D0009), `TERMINOLOGY.md`, `NAMES.md`: fidelitate conservatoare, fără omisiuni, fără adaosuri, fără înfrumusețare.
- **Verificări mecanice suplimentare:** numărarea termenilor-cheie (соблазн/искушение față de *ispită/ispitire*; Отец față de *Tatăl*; *duh*; *Iisus*; *mir*), scanarea diacriticelor (ș/ț cu virgulă, â/î, ortografia veche *sînt/cînd*), validatorul proiectului.
- **Independență:** auditorul nu a scris traducerea și a lucrat într-un context nou, pornind de la rusă. Este totuși tot un model, nu un vorbitor nativ; o lectură umană rămâne recomandată (TRANSLATION §12).

## 2. Numărătoare pe categorii

| Categorie | Constatări |
|---|---|
| omisiune | 1 |
| adaos | 3 |
| sens inversat / deplasat | 15 |
| trimiteri | 0 |
| terminologie | 6 |
| Biblie (Cornilescu / sinodală) | 2 |
| netezire / înfrumusețare | 4 |
| limba română | 28 |
| **total** | **59** |

Toate cele 59 constatări au fost corectate în fișierul românesc (78 de înlocuiri pe 69 de rânduri), câte un commit pentru fiecare capitol modificat. Încheierea nu a necesitat corecturi.

**Trimiteri și cifre:** nicio trimitere biblică sau cifră copiată greșit. Trimiterea «Лук. XII, 41» din cap. VI (de fapt Mc 12:41, banul văduvei) este o greșeală a sursei, nesemnalată în R002.01; a fost păstrată cum e tipărită (D0007) și adăugată în `project/qa/source_suspected/`.

**Ce nu s-a găsit:** nicio frază sau propoziție omisă, nicio negație pierdută, niciun vorbitor încurcat; termenii fixați (înțelegere, spirit, ispită/ispitire, fiul omului, împărăția cerului / lui Dumnezeu, voia tatălui, viață) sunt folosiți consecvent (cu o singură scăpare, «ispitindu-l», constatarea 45). Diacriticele sunt corecte peste tot (nicio sedilă, nicio formă *sînt/cînd*).

## 3. Constatările

Fiecare constatare: locul, rusa, româna veche, româna nouă, motivul.

### 1. Prefață (p. 808) — *netezire / înfrumusețare*

- **RU:** «что его трудно видеть под их толстым слоем»
- **RO vechi:** «încât ea abia se poate vedea sub stratul lor gros»
- **RO nou:** «încât e greu s-o vezi sub stratul lor gros»
- **Motiv:** «трудно» = greu; «abia» intensifică.

### 2. Prefață (p. 813) — *sens inversat / deplasat*

- **RU:** «а только в том, чтó проповедывал этот человек такое особенное, что заставило людей…»
- **RO vechi:** «ci numai în ceea ce propovăduia acest om atât de deosebit, încât…»
- **RO nou:** «ci numai în ce lucru atât de deosebit propovăduia acest om, încât…»
- **Motiv:** «особенное» califică învățătura, nu omul; vechea topică se citea «acest om atât de deosebit».

### 3. Introducere, cuprins — *sens inversat / deplasat*

- **RU:** «признание основой всего, — разумения в себе»
- **RO vechi:** «a înțelegerii din sine»
- **RO nou:** «a înțelegerii aflate în sine»
- **Motiv:** «в себе» = în sine (locul), nu «din sine» (proveniența).

### 4. Introducere, In 1:11 — *limba română*

- **RU:** «Он являлся в своем, но свое не удерживало его.»
- **RO vechi:** «Ea s-a arătat într-ale sale»
- **RO nou:** «Ea se arăta într-ale sale»
- **Motiv:** Aspect imperfectiv, în pereche cu «nu o păstrau».

### 5. Cap. I, Lc 4:4 — *omisiune*

- **RU:** «если я и не могу сделать из камней хлеба»
- **RO vechi:** «dacă nu pot face pâine din pietre»
- **RO nou:** «chiar dacă nu pot face pâine din pietre»
- **Motiv:** Particula concesivă «и» omisă.

### 6. Cap. II, Mt 15:9 (Isaia) — *terminologie*

- **RU:** «разум его разумников померкнет»
- **RO vechi:** «mintea celor cu minte ai lui se va întuneca»
- **RO nou:** «rațiunea deștepților lui se va întuneca»
- **Motiv:** разум = rațiune (TERMINOLOGY); locul nu este printre excepțiile cu «minte».

### 7. Cap. II, Mc 7:19; cap. III, In 3:4 — *netezire / înfrumusețare*

- **RU:** «не в душу, но в брюхо. В брюхо входит…; влезть в брюхо матери»
- **RO vechi:** «ci în pântece. În pântece intră…; să intre iar în pântecele mamei»
- **RO nou:** «ci în burtă. În burtă intră…; să se vâre iar în burta mamei»
- **Motiv:** D0008: registrul grosolan se păstrează; «pântece» e cuvântul biblic, mai nobil decât «брюхо»; «влезть» ≠ «a intra».

### 8. Cap. II, In 4:25 — *adaos*

- **RU:** «Он тогда всё расскажет.»
- **RO vechi:** «El atunci ne va spune totul.»
- **RO nou:** «El atunci va povesti totul.»
- **Motiv:** «ne» adăugat; расскажет = va povesti.

### 9. Cap. II, In 3:27 — *sens inversat / deplasat*

- **RU:** «человек сам собой не может ничему учить»
- **RO vechi:** «omul nu poate învăța singur nimic»
- **RO nou:** «omul nu poate de la sine să învețe pe nimeni nimic»
- **Motiv:** «a învăța» fără obiect se citea «a învăța (pentru sine)»; учить = a-i învăța pe alții.

### 10. Cap. II, Lc 7:39 — *limba română*

- **RU:** «едва ли он пророк»
- **RO vechi:** «cu greu să fie el profet»
- **RO nou:** «greu de crezut că el e profet»
- **Motiv:** Construcție neidiomatică.

### 11. Cap. III, cuprins — *sens inversat / deplasat*

- **RU:** «Зло — это подобие жизни.»
- **RO vechi:** «Răul — este o închipuire de viață.»
- **RO nou:** «Răul — este o aparență de viață.»
- **Motiv:** подобие = asemănare, aparență; «închipuire» = fantezie.

### 12. Cap. III, In 3:2 — *terminologie*

- **RU:** «не велишь чистоту соблюдать»
- **RO vechi:** «să se păstreze curățenia»
- **RO nou:** «să se păstreze curăția»
- **Motiv:** Curăția rituală e redată «curăție» în rest (cap. II).

### 13. Cap. III, In 3:8 — *limba română*

- **RU:** «и то, чему ты не знаешь ни начала, ни конца»
- **RO vechi:** «și ceea ce nu-i cunoști nici începutul»
- **RO nou:** «și lucrul căruia nu-i cunoști nici începutul»
- **Motiv:** «ceea ce … nu-i» este agramatical.

### 14. Cap. III, In 3:11 — *adaos*

- **RU:** «не мудрости какие-нибудь толкую я»
- **RO vechi:** «nu tâlcuiesc eu vreo înțelepciune deosebită»
- **RO nou:** «nu tâlcuiesc eu cine știe ce înțelepciuni»
- **Motiv:** «deosebită» adăugat; pluralul sursei păstrat.

### 15. Cap. III, Mt 13:8 — *limba română*

- **RU:** «наверстывают за пропащие зерна»
- **RO vechi:** «recuperează pentru boabele pierdute»
- **RO nou:** «compensează boabele pierdute»
- **Motiv:** Calc nefiresc.

### 16. Cap. IV, cuprins și Mt 19:9 — *sens inversat / deplasat*

- **RU:** «не оставлять той жены, с какой сошелся; живи с той, с которой ты сошелся»
- **RO vechi:** «cu care te-ai împreunat (×2)»
- **RO nou:** «cu care te-ai însoțit (×2)»
- **Motiv:** «сойтись» = a se lua, a trăi împreună; «a se împreuna» numește actul sexual. Cf. Mt 19:12 «сойдись» = «să se însoțească».

### 17. Cap. IV, cuprins; cap. IX, Mt 5:25 — *terminologie*

- **RU:** «ни на кого не иметь злобы; со всякой злобой… злоба худое дело»
- **RO vechi:** «să nu ai ură pe nimeni; cu orice ură… ura e un lucru rău»
- **RO nou:** «să nu ai răutate față de nimeni; cu orice răutate… răutatea e un lucru rău»
- **Motiv:** злоба = răutate (Mc 7:21; cap. IX, cuprins); «ură» rămâne pentru ненависть.

### 18. Cap. IV, Mt 5:39 — *limba română*

- **RU:** «и не только не бери судом»
- **RO vechi:** «și nu numai că să nu iei»
- **RO nou:** «și nu numai să nu iei»
- **Motiv:** Construcție agramaticală.

### 19. Cap. IV, Mc 11:25; cap. IX, Lc 18:17, Lc 17:3 — *limba română*

- **RU:** «не держите зла; не держат зла на людей; не иметь зла на людей»
- **RO vechi:** «să nu țineți răul asupra nimănui; nu țin răul pe oameni; să nu ai rău pe oameni»
- **RO nou:** «să nu purtați rău nimănui; nu poartă rău oamenilor; să nu porți rău oamenilor»
- **Motiv:** Rusisme (calc «держать зло на»); «rău» (зло) păstrat.

### 20. Cap. V, In 6:63 — *limba română*

- **RU:** «я ведь больше ничего не сказал»
- **RO vechi:** «eu n-am spus doar nimic altceva»
- **RO nou:** «eu doar n-am spus nimic altceva»
- **Motiv:** Topica particulei «doar».

### 21. Cap. V, Mt 10:28 — *limba română*

- **RU:** «душам вашим они ничего не могут сделать»
- **RO vechi:** «ele nu le pot face nimic»
- **RO nou:** «ei nu le pot face nimic»
- **Motiv:** Dezacord: subiectul este «cei care» (masc.).

### 22. Cap. VI, cuprins — *limba română*

- **RU:** «хозяин разочтет его»
- **RO vechi:** «stăpânul îl va concedia»
- **RO nou:** «stăpânul îi va face socoteala»
- **Motiv:** «a concedia» — neologism anacronic (TRANSLATION §5).

### 23. Cap. VI, cuprins — *netezire / înfrumusețare*

- **RU:** «безумно пролила ему на ноги масла»
- **RO vechi:** «i-a turnat, fără socoteală, pe picioare mir»
- **RO nou:** «i-a turnat nebunește pe picioare untdelemn»
- **Motiv:** «безумно» = nebunește; «fără socoteală» atenuează.

### 24. Cap. VI, cuprins — *limba română*

- **RU:** «что на это можно бы накормить многих»
- **RO vechi:** «că din aceștia s-ar fi putut hrăni mulți»
- **RO nou:** «că din asta s-ar fi putut hrăni mulți»
- **Motiv:** «aceștia» nu are antecedent (rublă e feminin).

### 25. Cap. VI (cuprins, Mt 26:7–12), cap. X (cuprins, In 12:3–5) — *Biblie (Cornilescu / sinodală)*

- **RU:** «масло (дорогое, цельное, пахучее масло)»
- **RO vechi:** «mir (×14)»
- **RO nou:** «untdelemn; «мѵро» din cap. X, cuprins rămâne «mir»»
- **Motiv:** Tolstoi scrie «масло» (untdelemn), nu «миро» al Bibliei sinodale; în același paragraf din cap. X deosebește el însuși «масло» de «мѵро». «mir» este cuvântul Cornilescu/sinodal (D0007). Cf. Lc 7:46 «масла» = «untdelemn», deja corect.

### 26. Cap. VI, Lc 12:16 — *limba română*

- **RU:** «родилось у него много хлеба»
- **RO vechi:** «i s-a născut multă pâine»
- **RO nou:** «i-a rodit multă pâine»
- **Motiv:** Rusism: «родился хлеб» = a rodit grâul.

### 27. Cap. VI, Lc 14:29 — *limba română*

- **RU:** «Чтобы не случилось того, что начал строить и не кончил»
- **RO vechi:** «Ca să nu se întâmple că a început»
- **RO nou:** «Ca să nu se întâmple așa: a început»
- **Motiv:** Construcție agramaticală; timpurile sursei păstrate.

### 28. Cap. VI, Lc 16:10 — *sens inversat / deplasat*

- **RU:** «если мы таких пустяков… жалеем для жизни духа»
- **RO vechi:** «dacă regretăm asemenea fleacuri»
- **RO nou:** «dacă ne pare rău să dăm asemenea fleacuri»
- **Motiv:** «жалеть для» = a se îndura greu să dai; «a regreta» schimbă sensul.

### 29. Cap. VI, Lc 16:28 — *limba română*

- **RU:** «А то как бы и они не попали в эту муку.»
- **RO vechi:** «Altfel să nu ajungă și ei»
- **RO nou:** «Ca nu cumva să ajungă și ei»
- **Motiv:** Temere exprimată idiomatic.

### 30. Cap. VI, Mt 26:8 — *sens inversat / deplasat*

- **RU:** «вот даром сколько пропало добра!»
- **RO vechi:** «câtă bunătate s-a pierdut degeaba!»
- **RO nou:** «câte bunuri s-au pierdut degeaba!»
- **Motiv:** добро = avere, bunuri; «bunătate» = calitate morală.

### 31. Cap. VII, cuprins — *limba română*

- **RU:** «делает нас несвободными»
- **RO vechi:** «ne face nelibere»
- **RO nou:** «ne face neliberi»
- **Motiv:** Dezacord de gen.

### 32. Cap. VII, cuprins — *limba română*

- **RU:** «требовать доказательств у слепого о том, почему и как он увидал свет»
- **RO vechi:** «să ceară dovezi de la un orb despre de ce și cum»
- **RO nou:** «să ceară de la un orb dovezi: de ce și cum»
- **Motiv:** «despre de ce» agramatical.

### 33. Cap. VII, In 7:8 — *limba română*

- **RU:** «а я пойду, когда вздумаю»
- **RO vechi:** «când îmi va veni»
- **RO nou:** «când voi socoti eu»
- **Motiv:** Idiom trunchiat («când îmi va veni [cheful]»).

### 34. Cap. VII, In 7:21 — *limba română*

- **RU:** «Я учу вас исполнению одной воли отца»
- **RO vechi:** «împlinirea singurei voi a tatălui»
- **RO nou:** «împlinirea numai a voii tatălui»
- **Motiv:** «singurei voi» se citea «unica voie»; одной = numai.

### 35. Cap. VII, In 7:34 — *limba română*

- **RU:** «А вы спрашивали у меня доказательств»
- **RO vechi:** «Iar voi îmi cereți dovezi»
- **RO nou:** «Iar voi mi-ați cerut dovezi»
- **Motiv:** Timp trecut în sursă.

### 36. Cap. VII, In 8:28 — *terminologie*

- **RU:** «когда возвеличите в себе сына человеческого»
- **RO vechi:** «îl veți înălța»
- **RO nou:** «îl veți preamări»
- **Motiv:** возвысить = a înălța, возвеличить = a preamări (In 12:32–36); două verbe deosebite.

### 37. Cap. VII, In 9:19 — *sens inversat / deplasat*

- **RU:** «Это ли ваш сын, тот, который от рождения был темный.»
- **RO vechi:** «Acesta este fiul vostru, cel care…»
- **RO nou:** «Oare acesta este fiul vostru, cel care…?»
- **Motiv:** «ли» face din frază o întrebare; româna o făcea afirmație.

### 38. Cap. VIII, cuprins — *sens inversat / deplasat*

- **RU:** «он ничего не делает такого, за что бы следовало благодарить и награждать его»
- **RO vechi:** «ar trebui să fie mulțumit și răsplătit»
- **RO nou:** «ar trebui să i se mulțumească și să fie răsplătit»
- **Motiv:** «să fie mulțumit» = să fie satisfăcut; благодарить = a-i mulțumi.

### 39. Cap. VIII, Lc 14:9 — *limba română*

- **RU:** «пусти того, кто получше тебя»
- **RO vechi:** «lasă-l pe acela, care e mai bun»
- **RO nou:** «lasă-l pe cel care e mai bun»
- **Motiv:** Relativă restrictivă — fără virgulă.

### 40. Cap. VIII, Mt 25:5 — *sens inversat / deplasat*

- **RU:** «Пока ждали жениха, они задремали.»
- **RO vechi:** «Până să-l aștepte pe mire, ele au ațipit.»
- **RO nou:** «Cât timp îl așteptau pe mire, ele au ațipit.»
- **Motiv:** «până să» = înainte să; sens inversat.

### 41. Cap. VIII, Mt 25:10 — *sens inversat / deplasat*

- **RU:** «а пока они ходили жених пришел»
- **RO vechi:** «iar până să umble ele, a venit mirele»
- **RO nou:** «iar cât timp umblau ele, a venit mirele»
- **Motiv:** Aceeași eroare: «până să» în loc de «cât timp».

### 42. Cap. IX, cuprins — *limba română*

- **RU:** «Мы делаем то, чего боимся для себя.»
- **RO vechi:** «Facem ceea ce ne temem pentru noi.»
- **RO nou:** «Facem lucrul de care ne temem pentru noi.»
- **Motiv:** «a se teme de» cere prepoziția.

### 43. Cap. IX, Mt 18:3 — *adaos*

- **RU:** «такими же, как дети»
- **RO vechi:** «la fel ca acești copii»
- **RO nou:** «la fel ca copiii»
- **Motiv:** «acești» adăugat.

### 44. Cap. IX, Mt 18:17 — *limba română*

- **RU:** «Если и собрания не послушает»
- **RO vechi:** «Dacă nici adunarea n-o va asculta»
- **RO nou:** «Dacă nu va asculta nici de adunare»
- **Motiv:** Ambiguu: se citea «adunarea nu-l va asculta».

### 45. Cap. IX, Mt 19:3 — *terminologie*

- **RU:** «выпытывая его»
- **RO vechi:** «ispitindu-l»
- **RO nou:** «iscodindu-l»
- **Motiv:** Rădăcina «ispit-» este rezervată pentru соблазн / искушение (D0006); cf. Mt 22:34 «выпытывать» = «a iscodi».

### 46. Cap. IX, Mt 22:16 — *sens inversat / deplasat*

- **RU:** «православные сошлись с царскими чиновниками»
- **RO vechi:** «s-au înțeles cu funcționarii»
- **RO nou:** «s-au întovărășit cu funcționarii»
- **Motiv:** «сойтись» = a se aduna, a se întovărăși; «a se înțelege» adaugă complotul.

### 47. Cap. IX, In 8:7 — *limba română*

- **RU:** «что он присудит этой женщине?»
- **RO vechi:** «ce va osândi pentru această femeie?»
- **RO nou:** «ce osândă îi va da acestei femei?»
- **Motiv:** Construcție agramaticală.

### 48. Cap. IX, Lc 20:35 — *sens inversat / deplasat*

- **RU:** «Те же, которые заслужат жизнь вечную»
- **RO vechi:** «vor dobândi»
- **RO nou:** «vor merita»
- **Motiv:** заслужить = a merita; «a dobândi» șterge ideea de merit.

### 49. Cap. X, cuprins — *limba română*

- **RU:** «малейшее неосторожное слово»
- **RO vechi:** «neprevăzător»
- **RO nou:** «nechibzuit»
- **Motiv:** «neprevăzător» = care nu prevede; неосторожный = nechibzuit.

### 50. Cap. X, cuprins — *limba română*

- **RU:** «с ненавистными язычниками»
- **RO vechi:** «păgânii urâți»
- **RO nou:** «păgânii odioși»
- **Motiv:** «urâți» se citește «hidoși».

### 51. Cap. X, cuprins; cap. X, In 13:1 — *limba română*

- **RU:** «предаст меня на смерть; обещал выдать его на смерть»
- **RO vechi:** «mă va vinde la moarte; să-l vândă la moarte»
- **RO nou:** «mă va da la moarte; să-l dea la moarte»
- **Motiv:** «a vinde la moarte» nu e românesc; «a vinde» (= a trăda) rămâne în rest.

### 52. Cap. X, In 11:53 — *limba română*

- **RU:** «решили, что нечего думать и надо непременно убить Иисуса»
- **RO vechi:** «că n-ai la ce te mai gândi și trebuie neapărat să-l ucidă pe Isus»
- **RO nou:** «că nu mai e nimic de gândit și că Isus trebuie neapărat ucis»
- **Motiv:** Amestec de persoane (n-ai / să-l ucidă).

### 53. Cap. XI, In 13:38 — *sens inversat / deplasat*

- **RU:** «а как бы до петухов еще ты бы не отрекся от меня три раза»
- **RO vechi:** «dar să nu te lepezi tu de mine de trei ori…»
- **RO nou:** «dar ca nu cumva să te lepezi tu de mine de trei ori…»
- **Motiv:** «как бы … не» exprimă temere; româna devenise poruncă.

### 54. Cap. XII, cuprins — *sens inversat / deplasat*

- **RU:** «да, я человек — сын Бога»
- **RO vechi:** «da, eu sunt omul — fiul lui Dumnezeu»
- **RO nou:** «da, eu sunt om — fiul lui Dumnezeu»
- **Motiv:** Articolul («omul») schimbă afirmația în «Omul» generic.

### 55. Cap. XII, Mt 26:49 — *limba română*

- **RU:** «здравствуй, учитель!»
- **RO vechi:** «bună ziua, învățătorule!»
- **RO nou:** «sănătate, învățătorule!»
- **Motiv:** Scena e noaptea; «здравствуй» = salut de sănătate.

### 56. Cap. XII, Mt 26:74 — *Biblie (Cornilescu / sinodală)*

- **RU:** «начал клясться и божиться»
- **RO vechi:** «a început să se jure și să se blesteme»
- **RO nou:** «a început să se jure și să se jure pe Dumnezeu»
- **Motiv:** «a se blestema» vine din Cornilescu (Mt 26:74); божиться = a se jura pe Dumnezeu.

### 57. Cap. XII, Mc 14:59 — *limba română*

- **RU:** «Но и этой улики было мало, чтобы обвинить.»
- **RO vechi:** «Dar și această dovadă era puțin ca să-l învinuiască.»
- **RO nou:** «Dar nici această dovadă nu era de ajuns ca să-l învinuiască.»
- **Motiv:** Construcție agramaticală.

### 58. Cap. XII, Mt 27:21 — *netezire / înfrumusețare*

- **RU:** «Пилату хотелось выручить Иисуса»
- **RO vechi:** «Lui Pilat i-ar fi plăcut să-l scape pe Isus»
- **RO nou:** «Pilat voia să-l scape pe Isus»
- **Motiv:** «хотелось» = voia; condiționalul atenuează.

### 59. Cap. XII, Mt 27:28 — *terminologie*

- **RU:** «солдаты, те, которые секли его»
- **RO vechi:** «cei care îl biciuiseră»
- **RO nou:** «cei care îl bătuseră cu nuiele»
- **Motiv:** высечь = «a bate cu nuiele» chiar în versetul precedent.

### Observații păstrate fără modificare

- **Mt 26:50** «товарищ!» = «tovarășe!»: literal; conotația modernă e un risc, dar «prietene» ar fi forma sinodală. Lăsat.
- **Titlul cap. X** «ДОЛЖНО … БЫТЬ» (impersonal) = «OMUL TREBUIE SĂ FIE»: subiectul adăugat e minim și cerut de română. Lăsat.
- **In 5:4** «вода … начнет играть» = «apa începe să se joace»: literal și neobișnuit, dar inteligibil (D0001). Lăsat.
- **Prefața** «настоящею жизнью» (viața reală a credincioșilor) = «viață adevărată», aceeași formă ca pentru «истинная жизнь». Distincția nu se poate reda fără a forța româna. Lăsat.

## 4. Verificarea pe ediția tipărită («вражды», In 6:35)

Lectura din `project/qa/source_suspected/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.json`: cap. V, In 6:35 (vol. 24, p. 856) — «а тот, кто верит в мое учение, тот не будет никогда знать вражды», posibil «жажды» (cf. In 6:35 «не будет жаждать никогда»).

**Rezultat: lectura «вражды» este confirmată pe ediția tipărită.**

- **Martorul tipărit:** o scanare a p. 856 din vol. 24 al ediției de 90 de volume (1957), trimisă de proprietarul proiectului în timpul auditului. Numărul paginii, 856, se vede la subsol, iar pagina cuprinde In 6:7–40 în aceeași ordine ca sursa (6:7; Mt 14:17 / In 6:9; 6:10, 11, 26–33, 35–40). Versetul 35 se citește limpede: «Мое учение дает истинное питание людям. Тот, кто последует мне, тот не будет голодать, а тот, кто верит в мое учение, тот не будет никогда знать вражды.» Restul paginii coincide cu stratul Markdown.
- Gazdele cu scanări (tolstoy.ru, `/online/90/24/`; rusneb.ru; archive.org; ru.wikisource.org; tolstoy-lit.ru) au fost blocate de politica de rețea a mediului de audit (CONNECT respins, `EGRESS_BLOCKED`), de aceea scanarea a venit de la proprietar.
- O căutare web a frazei exacte, cu «вражды» sau cu «жажды», nu a găsit niciun martor.
- **Ce s-a putut verifica:** fișierul de arhivă TEI `tolstoydigital/TEI/texts/works/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.xml` (SHA-256 `b9d47b57…a29062`, descărcat de pe raw.githubusercontent.com) are același text: «…тот не будет никогда знать вражды.», urmat de `<pb n="856"/>`. Tiparul, TEI și Markdown concordă.
- **Decizie:** «вражды» este textul tipărit, nu o greșeală de transcriere. Dacă e cuvântul voit al lui Tolstoi sau o greșeală a ediției din 1957 nu se poate hotărî din tipar; conform D0009, româna rămâne «dușmănia». Înregistrarea din `source_suspected` este închisă.

Celelalte lecturi din înregistrare (greșeli de tipar, trimiteri greșite, citatul francez) au fost revăzute pe sursă: toate sunt descrise corect, iar tratamentul lor în română corespunde D0007 și D0009.

## 5. Verdict

**PASS AFTER REVISION.**

Traducerea este completă și, în ansamblu, fidelă: nicio frază lipsă, nicio trimitere greșită, terminologia fixată ținută consecvent. Auditul a găsit însă erori reale de sens pe care auditul inițial nu le prinsese — două inversări prin «până să», o temere transformată în poruncă, o întrebare transformată în afirmație, «добро» = «bunătate», «жалеть для» = «a regreta» — și o alunecare sistematică spre vocabularul biblic («mir» pentru «масло»), plus 28 de scăpări de limbă. După corecturile din această ramură, unitatea trece. Lectura «вражды» este confirmată pe ediția tipărită (p. 856).
