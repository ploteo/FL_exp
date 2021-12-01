


**To be inputed before starting**

- Nome e ubicazione delle associazioni - > institutions.csv in FL_Welcome
- Scelte delle associazioni nel TG - > choices_inst.csv in FL_Welcome
- Tasso di conversione dei token in soldi reali -> da definire in settings.py -> real_world_currency_per_point=0.01
- Show up fee (espressa già in mount reale) -> da definire in settings.py participation_fee=int(4)
- Number of participants -> settings.py


# General 

- Implement a version that does the randomization at the group level @DONE:
  - change init.py for PGG
  - change settings.py
    - see NOTE: in the demo dev
- Check "Your Choice" and "Continue" in FL_risk, the % sign in DG instructions and "Choice #" in FL_trust
- Check 'How much do you trust that you will receive the money in 2 or 4 weeks\' time?' 

# Translation

## Tunisia

- Implement new rando at group level @TODO:



## Morocco (MO)

### Arabic

- Ask to translate basic oTree recevied from the developer 
- Set a meeting to understand the issue with Arabic (ltr)
  - Proposed a solution to partners https://foodland-demo-ar-morocco.herokuapp.com/demo @WAIT
    - Added a new translation DONE 23/11/21
- Implement new rando at group level @DONE:
  
### French

- Received feedback and revised 
  - Changed the wording of the identity task to accommodate translation @DONE
  - Still some problem with the article of the institution (check when real names are available) @DONE:
- Revised version available on https://foodland-demo-fr.herokuapp.com/demo  @WAIT
- Implement new rando at group level @DONE:

## Tunisia (TN)

- Need to understand the issue with Arabic @TODO:
- Implement new rando at group level @TODO:
  
## Etiopia (ET)

- Waiting for first translation  @WAIT:

## 3) Kenya (KE)

- [ ] Ultimi cambi per Kenya (solo nel onedrive in KE/2 round perché troppo pesanti da allegare). 
  - [ ] Trovi i cambi richiesti ed inviati nello scorso giro formattati in word (più screenshot) in maniera che sia più semplice inserirli. @DONE:
    - [ ] Still some issue when info about organizations is imported @TODO:
- Implement new rando at group level @DONE:
- Implement identity task @DONE:
  - Identity_task_feedback.html
  - Identity_task_ALT.html
  - init.py
- Minor changes, conversion rate @TODO:


It can be cold or warm.
(1) Inaweza (2) kuwa (3) baridi (4) au ya joto.

It can be transparent.
(1) Inaweza (2) kuwa (3) ya (4) uwazi.

It can be salty.
(1) Inaweza (2) kuwa (3) na (4) chumvi.

It makes thirst go away.
(1) Ina (2) fanya (3) kiu (4) iende.
 
 
Water can be cold or warm.
(1) Maji (2) inaweza (3) kuwa baridi (4) au ya joto.

Water can be transparent.
(1) Maji (2) inaweza (3) kuwa (4) wazi.

Water can be salty.
(1) Maji (2) inaweza (3) kuwa (4) na chumvi.

Water makes thirst go away.
(1) Maji (2) hufanya (3) kiu (4) kuondoka.

- Implement grammar corrections @DONE:
  - Check "Your Choice" and "Continue" in FL_risk,  the % sign in DG instructions and "Choice #" in FL_trust
  
## 2) Tanzania (TZ)

- We sent the wrong address, now available online at https://foodland-demo-sw-tanzania.herokuapp.com/demo for feedback 
  - [ ] See messages-Tanzania-3.docx @DONE:
  - [ ] revise identity task @DONE:
  - [ ] New randomization at group level #DONE:
 
- New sentence break DONE
English	Swahili
It can be cold or warm.	(1)Kinaweza (2)kuwa  (3)baridi (4)au joto
It can be transparent.	(1)Kinaweza (2)kuwa (3)chenye (4)uangavu
It can be salty.	(1)Kinaweza (2)kuwa (3)na (4)chumvi
It makes thirst go away.	(1)Kinafanya (2)kiu (3)iweze (4)kuondoka
	
Water can be cold or warm.	(1)Maji yanaweza (2)kuwa (3)ya baridi (4)au ya joto
Water can be transparent.	(1)Maji (2)yanaweza (3)kuwa (4)na uangavu
Water can be salty.	(1)Maji (2)yanaweza (3)kuwa (4)ya chumvi
Water makes thirst go away.	(1)Maji (2)yanafanya (3)kiu (4)iondoke

OLD ones
      It can be cold or warm.
      (1)kina(2)weza (3)kuwa (4)baridi au ya moto

      It can be transparent.
      (1)kina(2)weza (3)kuwa (4)angavu

      It can be salty.
      (1)kina(2)weza (3)kuwa (4)ya chumvi

      It makes thirst go away.
      (1)ina(2)fanya (3)kiu (4) iondoke

      Water can be cold or warm.
      (1)maji (2)yanaweza (3)kuwa (4)baridi au ya moto

      Water can be transparent.
      (1)maji (2)yanaweza (3)kuwa (4)angavu

      Water can be salty.
      (1)maji (2)yanaweza (3)kuwa (4)ya chumvi

      Water makes thirst go away.
      (1)maji (2)yanafanya (3)kiu (4)iondoke

- NEW changes in translation DONE

1. use "kete" instead of "Tokeni".DONE
2. put the number after the word. e.g. "kete 100" instead of "100 Tokeni" (Please effect this in all tokens)


Specific corrections

1. use "Chama cha Msingi cha Wakulima" instead of "Local Farmers Association"DONE
2. use " TAJA JINA HAPA" instead of "MANE HERE"
3. use "Mazingira mapya rafiki kiikolojia" instead of "new eco-friendly solutions"DONE
4. use "WEKA HAPA" instead of "PLACE HERE"
5. use "nne" instead of "knne" (typographic error at Mchezo 3 (TP)) DONE
6. use "chaguo" instead of "machaguo"DONE
7. use "uangalifu" instead of "ufangalifu" (typographic error at Mchezo 3 (TP))DONE
8. use "kutegemeana" instead of "kutegemana"
9. Question not translated at all: How much do you trust that you will receive the money in 2 or 4 weeks time"
 "Je! Unaamini ni kwa kiasi gani kwamba utapokea pesa kwa muda wa wiki 2 au 4"DONE
10. use " sehemu mbili" instead of "sehemu mawili"   DONE
11. use "umejipatia" instead of "umejipatika"DONE
12. use "Chaguo lako" instead of "your choice" (currently not translated in the installed version)DONE
13. use "Endelea" instead of "Continue" (currently not translated in the installed version)DONE
14. use "Sarafu (pesa) za ndani" instead of "Fedha za Kenya" DONE

## 1) Uganda (UG)

- Received feedback
- Revised version available on https://foodland-demo-ch-uganda.herokuapp.com/demo @DONE:
- [ ] New randomization at group level #DONE:

  - [ ] Sentences for the identity (see email) @DONE:
- 
      It can be cold or warm.
      (1)Kisobola (2)okunyogoga (3)oba (4)okubuguma

      It can be transparent.
      (1)Kisobola (2)okuba (3)nga (4)kitangaala

      It can be salty.
      (1)Kisobola (2)okuba (3)ekyo (4)olunyonyo

      It makes thirst go away.
      (1)Kyo (2)kiletela (3)enyonta (4)okuvawo
     
    ---

      Water can be cold or warm.
      (1)Amazzi (2)gasobola (3)okunyogoga (4)oba okubuguma

      Water can be transparent.
      (1)Amazzi (2)gasobola (3)okuba (4)nga gatangaala

      Water can be salty.
      (1)Amazzi (2)gasobola (3)okuba (4)ago olunyonyo

      Water makes thirst go away.
      (1)Amazzi (2)galetela (3)enyonta (4)okuvawo

    - [ ] In DG una pagina con delle frasi non tradotte (allegato 1) @DONE:
      - REPLY: A posto (il problema era legato al simbolo %)
    - [ ] Sempre in DG ho anche notato che nel questionario non viene riproposta la stessa scala  likert per la domanda 2-3. Da protocollo però questa scala era identica:@DONE:
        How well do you know the farmers’ association/NGO?
        Code: 1 = Not at all; 2 = Little; 3 = Average; 4 = Fairly well; 5 = Very well

        How much do you think that you understood the instructions you were given in this game?
        Code: 1 = Not at all; 2 = Little; 3 = Average; 4 = Fairly well; 5 = Very well

      - REPLY: Io ho queste scale, credo fosse una correzione fatta dal partner. Io terrei le scale che abbiamo adesso nel software. 
  
        How much do you think that you understood the instructions you were given in this game?
        gettext("Not at all"), gettext("Little"), gettext("Average"), gettext("Fairly Well"), gettext("Completely")

        How well do you know the farmers’ association/NGO?
        gettext("Not at all"), gettext("Little"), gettext("Average"), gettext("Fairly Well"), gettext("Very well")])

    - [ ] Noto poi che in generale mancano punti di domanda nelle varie domande dei questionari di comprensione. È dovuto ad un errore di programmazione?
      - REPLY: Il traduttore non ha messo i punti di domanda, anche se erano presenti nel testo in inglese

        
    - [ ] Per finire, anche provando più di 20 volte e da computer diversi, non riusciamo ad accedere al PGG group identity treatment group (quello con IT per capirci), in quanto il sistema fornisce solo il gruppo controllo. È dovuto al fatto che per il momento nella versione demo i gruppi non vengono ancora randomizzati?@DONE:
      - REPLY: il trattamento identity/no identity deve essere controllato "a mano" cambiando un parametro in setting.py (così si era deciso, vedi anche il documento operativo che avevo preparato). Se vogliamo invece che sia randomizzato devo cambiare il codice. Ho caricato adesso una versione che randomizza a livello di sessione,questo semplificherebbe il lavoro degli assistenti.
 
