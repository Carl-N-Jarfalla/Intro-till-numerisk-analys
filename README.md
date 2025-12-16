# Numerisk analys ma3c

## Uppgift 1
För uppgift 1 har du fått en .txt fil med data från en löprunda i kallhälls el-ljus spår.
Filen innehåller distansen i meter från start och höjden över havet. Din uppgift är att räkna ut var
längs spåret det lutar mest.

## Uppgift 2

I uppgift 1 fick vi en funktion i form av en värdetabell. För tillämpningar så händer det att detta är 
det enda sättet funktioner kan beskrivas, i denna kurs kommer vi dock oftare hantera funktioner som kan ges 
som ett uttryck. I denna uppgift ska vi först arbeta med funktionen $f(x)=\frac{x^3+1}{x^2-1}$, den är
definierad för alla $x$ förutom $x=\pm 1$ och finns redan i filen uppgift 2.py.

### Lutning mellan punkter

För linjära funktioner ges lutningen av $k=\frac{y_2 - y_1}{x_2 - x_1}$. $f$ är dock inte linjär.
Vi kan dock prata om medellutning mellan två punkter, och denna ges av en snarlik formel $k=\frac{f(x_2 ) - f(x_1 )}{x_2 - x_1}$.
- Räkna ut medellutningen för funktion $f$ mellan $x=2$ och $x=4$.
- Skriv en funktion (i python) som räknar ut medellutningen om den får en funktion och de två punkterna.

### Lutning runt en punkt

Ofta vill vi veta hur en funktion beter sig i en punkt. Frågan är i sig lite konstig, en punkt kan inte luta. Men en snarlik fråga
"Hur snabbt åker en bil just när den passerar en hastighetskontroll?" finner de flesta inget ovanligt med. Vi ska ändå närma oss
frågan försiktigt och kommer börja att undersöka hur lutningen ser ut i ett litet område runt en punkt.
- Räkna ut medellutningen för funktion $f$ mellan $x=2$ och $x=2.1$.
- Med hjälp av en loop, räkna ut medellutningen för mindre och mindre intervall. Gå dock inte mindre än $10^{-12}$ då avrundningsfel
i flyttals matten kommer börja påverka resultatet.
- Hur litet behöver intervallet vara för att du (i detta fall) ska kunna bestämma lutningen runt punkten med tre decimaler?

## Uppgift 2.5

I samma fil finns det en funktion till definierad, $g(x)$. Vi ska nu undersöka hur den beter sig runt $x=2$.
- Räkna ut medellutningen för funktion $g$ mellan $x=2$ och $x=2.1$.
- Med hjälp av en loop, räkna ut medellutningen för mindre och mindre intervall. Gå dock inte mindre än $10^{-12}$ då avrundningsfel
i flyttals matten kommer börja påverka resultatet.
- Räkna ut medellutningen för funktion $g$ mellan $x=1.9$ och $x=2$.
- Med hjälp av en loop, räkna ut medellutningen för mindre och mindre intervall. Gå dock inte mindre än $10^{-12}$ då avrundningsfel
i flyttals matten kommer börja påverka resultatet.