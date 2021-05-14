# Autografy
Aby uruchamiać poszczególne pakiety prosimy przejść do głównego folderu projektu

---


# Pisanie własnych testów
Proponujemy edytować gotowe testy.

W nowych testach musi zostać dodany ten kawałek kodu w pierwszych linijkach
```python
#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below
```
Pozwala to na importowanie pakietów z głównego folderu **(patrz "Przykłady uruchomienia")** 


# Przykłady uruchomienia

**Znajdując się w folderze**
```
.../Autografy
```

**Testy pierwszego zestawu**
```bash
python tests/p1/conversionTest.py
python tests/p1/plotTest.py
```

**Testy drugiego zestawu**
```bash
python tests/p2/<nazwaTestu.py>
```

itd...
