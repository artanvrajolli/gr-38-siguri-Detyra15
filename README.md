# gr-38-siguri-Detyra15
Zhvillimi i nje API (application programming interface) me disa funksione bazike, duke implementuar authentifikimin bazik ose me token.

* Python GIU me Tkinter

# Hyrje ne Python GUI  
Nderfaqja GUI ose Graphical User është një formë e ndërfaqes së përdoruesit që përfshin elemente grafike të tilla si dritaret, ikonat dhe butonat.  
Çdo gjuhë programimi ka grupin e vet të librarive unike GUI. Në Python, Tkinter është libraria më e zakonshme GUI që përdoret për të krijuar Graphical User Interfaces.  
Tkinter është një librari me burim të hapur Python GUI e njohur për thjeshtësinë dhe fleksibilitetin e saj. Ajo vjen e instaluar paraprakisht në Python 3.  

# Instalimi  
Per ta instaluar kete aplikacion duhet qe ta keni te instaluar [Python](https://www.python.org/downloads/) ose [Python3](https://www.python.org/downloads/).  
Perveq python duhet instaluar [GIT](https://git-scm.com/downloads).  
Pasi qe te instalohet Python, hapim nje folder ku deshirojme aplikacionin dhe bejme clone projektin permes komandes:  
```
git clone 'https://github.com/artanvrajolli/gr-38-siguri-Detyra15.git'
```  
Kjo kompleton pjesen e instalimit.  

# Disa nga metodat e përdorura te Python Tkinter  
* Frame – Skicon kornizën për dritaren Tkinter me madhësi fikse.  
* Buttons – Përdoret si një mënyrë për përdoruesin për të bashkëvepruar me User Interface.  
* Entry – Përdoret për të marrë të dhëna nga përdoruesi përmes User Inteface.Pra jepet një kuti e thjeshtë ku përdoruesi jep tekst.  
* Label – Përdoret për të shfaqur tekst në një GUI.  
* Canvas – Përdoret për të vizatuar grafikë dhe skema.  

# Përshkrimi  
Përmes këtij aplikacioni përdoruesit do të mund të kryejnë këto veprime:  
* Register  
* Login with password  
* Login with token  

Meqenëse është një aplikacion që implementon vërtetimin me token atëherë kemi importuar librarin JWT(JSON Web Token).  
Për çdo përdorues që llogohet duke dhënë emrin dhe password-in , në rast suksesi lëshohet një token i nënshkruar i cili përdoret për autentifikim të shfrytëzuesit.  

# Implementimi  
Në kuadër të API-të kemi ndarë pjesën e UI(User Interface) dhe pjesën e Eventeve në fajlla të veqantë, pra si module :  
* screens.py  
* events.py  
Këto module të krijuara i përdorim në fajllin app.py duke përdorur deklaratën e importit ku edhe bëhet ekzekutimi i programit.  
Procedura e vertetimit të përdoruesit:  
*	Kontrollimi nëse fjalëkalimet përputhen.  
*	Në rast se përdoruesi nuk ekziston ose fjalkalimi nuk përputhet atëherë kthejmë përgjigjen me mesazh gabimi.  
*	Krijojmë një token si payload ku ruhet emri i përdoruesit për të identifikuar përdoruesin.  
*	Enkodojmë payload-in me një string sekret dhe algoritëm të specifikuar.  

String sekret dhe algoritmi i specifikuar janë ruajtur në një fajll të veçantë constants.py i cili modul është i importur tek events.py  
Pas marrjes se token-it përdoruesi duhet të kopjojë atë dhe ta vendosë në fushën qe i kërkohet. Dekodojmë tokenin me të njëjtin string sekret dhe me algoritmin e specifikuar , në rast se tokeni nuk është i njejtë atëherë kthejmë përgjigjen me mesazh gabimi.  
