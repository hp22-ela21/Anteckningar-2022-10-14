# Anteckningar 2022-10-14
Demonstration av flertrådad GPIO-implementering i Python.

Filen main.py innehåller ett program där två trådar implementeras för att blinka multipla 
lysdioder parallellt med olika blinkhastigheter. Lysdiodernas pin-nummer lagras i var sin
lista. Flertrådningen realiseras via objekt av klassen Thread från modulen threading.
