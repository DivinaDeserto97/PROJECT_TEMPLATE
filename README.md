# PROJECT_TEMPLATE – Standard-Vorlage für neue Python-Projekte

Diese Vorlage ist dafür gedacht, dass du **neue Projekte schnell, sauber und reproduzierbar** starten kannst – mit:

* eigenem `.venv`
* Linter (**Ruff**)
* Code-Formatter (**Black** – „Prettier für Python“)
* klarer Projektstruktur

---

## 📁 Empfohlene Ordnerstruktur (Template)

```text
PROJECT_TEMPLATE/
├─ .vscode/
│  └─ settings.json
├─ src/
│  ├─ main.py
│  └─ tools/
│     └─ __init__.py
├─ tests/
│  ├─ __init__.py
│  └─ test_basic.py
├─ .env
├─ .gitignore
├─ README.md
└─ requirements.txt
```

⚠️ **Wichtig:**

* `.venv/` gehört **NICHT** ins Template.
* `.venv/` wird **für jedes Projekt neu erstellt**.

---

## 🔁 Neues Projekt aus dem Template erstellen (KOPIEREN)

1. **Template-Ordner kopieren**

   ```text
   PROJECT_TEMPLATE  →  MEIN_NEUES_PROJEKT
   ```

2. In den neuen Projektordner wechseln

   ```powershell
   cd MEIN_NEUES_PROJEKT
   ```

3. **Virtual Environment neu erstellen**

   ```powershell
   python -m venv .venv
   ```

4. **.venv aktivieren**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. **Alle Tools automatisch installieren**

   ```powershell
   pip install -r requirements.txt
   ```

✅ Danach sind **Black + Ruff + Abhängigkeiten** direkt einsatzbereit.

---

## 🔧 Lint & Formatter – Prinzip

### ✅ Ruff = Linter

* Prüft deinen Code auf:

  * Syntaxfehler
  * unbenutzte Variablen
  * falsche Imports
* Meldet Fehler direkt in VS Code

### ✅ Black = Code-Formatter (Prettier für Python)

* Formatiert deinen Code **automatisch beim Speichern**
* Einheitlicher Stil im ganzen Projekt

Du musst **nichts manuell starten**, wenn:

* Ruff-Extension installiert ist
* Python-Extension installiert ist
* `.vscode/settings.json` korrekt gesetzt ist

---

## 🔄 Projekt aktualisieren (Tools erneuern)

Wenn du später neue Tools installierst (z.B. pytest):

```powershell
pip install pytest
pip freeze > requirements.txt
```

Danach haben **alle neuen Projekte automatisch** auch dieses Tool.

---

## ♻️ Bestehendes Projekt neu aufsetzen

Wenn dein `.venv` kaputt ist oder du alles sauber neu willst:

```powershell
rmdir /s /q .venv
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 🚀 Hallo-Welt für `src/main.py`

```python
def main():
    print("Hallo Welt – Projekt gestartet!")


if __name__ == "__main__":
    main()
```

Starten mit:

```powershell
python src/main.py
```

---

## 🧠 Merksätze

* `.venv` → **niemals kopieren**
* `requirements.txt` → **immer kopieren**
* Black = Formatierer
* Ruff = Linter
* Template = nur Struktur + Konfiguration

---

✅ Dieses Dokument gehört in dein Template, damit du **in 30 Sekunden** ein neues sauberes Projekt starten kannst.
