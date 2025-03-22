---

### File 1: monday_march_24_intro_setup.md
# Introduction and Setup for Monday, March 24, 2025: Masterclass—Python 3.12.3 & AI Model Poisoning

## Welcome, Student
Your resolve is fierce, and I’m honored as your Grok Sensei from xAI to guide you. This is your Stanford/CMU-caliber Masterclass for March 24, 2025, on .101 (Ubuntu_ai), teaching Python 3.12.3 and AI model poisoning. You’ve demanded a *gigantic, glorious masterpiece*, but xAI’s session cutoffs threaten to chop it mid-flight. You’ll restart fresh—maybe 2-3 times—Monday, with only these files and `cyber_notes.txt`. “Outside, it’s ash,” you said, and your “Why this ash?” nailed my errors—gold must stay inside. So, we’re splitting it: this intro/setup, plus one file per module. Copy each into `monday_march_24_masterclass.md` on .101, building your dojo piece by piece. Every explanation, code, and meditation is here—wield it through any cutoff and sharpen your AI Security Engineering blade!

## Course Overview
- Institution: Your Personal Cyber Dojo (Stanford/CMU-Inspired)  
- Instructor: Grok Sensei (xAI)  
- Date: March 24, 2025  
- Duration: 10-12 hours (pace yourself—hydrate, stretch)  
- Platform: .101 (Ubuntu_ai) - Direct dev, no SSH  
- Objective: Master Python 3.12.3 from zero, build an Iris poisoning sim, expose AI vulnerabilities via code, theory, and analysis.  
- Prerequisites: Basic terminal (`cd`, `nano`). No Python/ML needed—I teach it all. Week 2 (Git, Flask poisoning) helps but isn’t required—this stands alone.  
- Learning Outcomes:  
  - Write Python—variables, functions, loops, conditionals, files—from nothing.  
  - Grasp ML—data handling, training, metrics.  
  - Simulate poisoning—random and targeted—analyze impacts.  
  - Forge QA into AI security—data as your shield.  

## Why This Matters
AI models are fragile giants—bad data (poisoning) can ruin them silently. Imagine a self-driving car misreading signs or a chatbot spewing garbage from tainted training. Week 2’s Flask API dropped 15% accuracy with targeted flips—this scales that lesson. As an AI Security Engineer, you’ll *cut* these flaws with Python, exposing them to defend them. This isn’t just code—it’s your mindset: QA precision meets ML’s frontier. By day’s end, your poisoning sim will be a blade—pierce or protect, your call.

## Tools
- Python 3.12.3: Your katana—fast, modern, pre-installed on Ubuntu 24.04 LTS.  
- scikit-learn 1.5.2: ML toolkit—data, models, metrics.  
- NumPy 2.0.0: Array math—randomness, structure.  
- Virtualenv: `sklearn_env`—isolates deps, QA-style sandbox.  
- Git: Tracks progress—portfolio at https://github.com/MrClocSecAI/16week-upskill.  
- nano: Your editor—simple, sharp.  

## Setup: Your Dojo Prep
- Machine: .101 (Ubuntu_ai) - Direct, no SSH.  
- Steps:  
  1. Terminal: Ctrl+Alt+T. `whoami`—expect your username (e.g., `ubuntu`). Your dojo lives.  
  2. Directory: `cd ~/Documents/16week-upskill/Notes`. Missing?  
     - `mkdir -p ~/Documents/16week-upskill/Notes` (creates it).  
     - `cd ~/Documents/16week-upskill/Notes`.  
  3. Git: `git status`. “Not a git repository”?  
     - `git clone https://github.com/MrClocSecAI/16week-upskill ~/Documents/16week-upskill`.  
     - `cd ~/Documents/16week-upskill/Notes`.  
     - No Git? `sudo apt update && sudo apt install git`.  
  4. Python: `python3 --version`—expect “Python 3.12.3”. Else:  
     - `sudo apt update && sudo apt install python3.12 python3-pip`.  
  5. Virtualenv: `ls -a`—see `sklearn_env`? If not:  
     - `python3 -m venv sklearn_env`.  
     - `source sklearn_env/bin/activate` (prompt: `(sklearn_env)`).  
  6. Deps: `pip list | grep scikit-learn` (1.5.2), `pip list | grep numpy` (2.0.0). If not:  
     - `pip install scikit-learn==1.5.2 numpy==2.0.0`.  
- Meditate: Tools are steel—if a step breaks, pause, reread, retry. You’ve only this and module files—no outside crutch.

---

### File 2: monday_march_24_module_1.md
### Module 1: Python 3.12.3 Foundations—Your Katana (1.5 hrs)
**Goal**: Master Python basics—variables, functions, logic—to wield code like a weapon.  
**Steps**:  
1. **Terminal Warm-Up (15 min)**  
   - Type: `python3` (opens shell).  
   - Enter: `print("Wax on, wax off!")`—see it echo.  
   - Try: `2 + 3`—expect 5.  
   - Play: `10 * 2`—expect 20.  
   - Exit: `exit()`.  
   - Cut: Python’s live—no compile delay. `print()` is your debug voice.  
   - Wax On: Reopen `python3`, `print("I am the student!")`—claim it.  
   - Wax Off: `5 - 1`, then `print(4 * 3)`—feel the flow.  
   - Meditate: Commands are breaths—steady, direct.  
2. **First Script—Variables (30 min)**  
   - `nano hello.py`:  
     ```python
     # Comments with #—your notes
     name = "Student"  # Text variable
     age = 25  # Number variable
     print("Hello,", name, "you are", age)
     ```
   - Save: Ctrl+O, Enter, Ctrl+X.  
   - Run: `python3 hello.py`—expect “Hello, Student you are 25”.  
   - Chop: `=` assigns—variables are boxes. Strings use quotes, numbers don’t. `print()` joins with commas.  
   - Wax On: Edit `name = "Sensei"`, `age = 1000`, rerun—see it shift.  
   - Wax Off: Add `skill = "Python"`, `print("Learning", skill)`—expand it.  
   - Meditate: Variables hold intent—simple, mighty.  
3. **Functions & Logic—Reusable Power (45 min)**  
   - `nano math_fun.py`:  
     ```python
     def add(a, b):  # Function—takes inputs
         result = a + b
         return result  # Outputs result

     x = 5
     y = 10
     total = add(x, y)  # Call it
     print("Total:", total)

     if total > 12:  # Condition
         print("Big total!")
     else:
         print("Small total.")
     ```
   - Run: `python3 math_fun.py`—expect “Total: 15” and “Big total!”.  
   - Slice: `def` builds functions—reusable blocks. `return` delivers. `if/else` decides—like QA checks.  
   - Wax On: Change `y = 2`, rerun—see “Small total.”  
   - Wax Off: Add `def subtract(a, b): return a - b`, `diff = subtract(x, y)`, print it—test your grip.  
   - Meditate: Functions are techniques—logic steadies your hand.  
**Theory**: Python’s interpreted—runs top-down, line-by-line. Variables are dynamic—no type needed (`name` can switch from text to number). 3.12.3’s fast—PEP 684 boosts loops, ideal for ML.

---

### File 3: monday_march_24_module_2.md
### Module 2: Iris Dataset—Your ML Playground (2 hrs)
**Goal**: Load and dissect Iris—data as your raw material.  
**Steps**:  
1. **First Contact (15 min)**  
   - `nano iris_intro.py`:  
     ```python
     from sklearn.datasets import load_iris  # Dataset tool
     iris = load_iris()  # Load it
     print("Iris loaded—let’s cut!")
     ```
   - Run: `python3 iris_intro.py`.  
   - Cut: `import` grabs tools—`load_iris()` fetches 150 flowers.  
   - Wax On: Add `print(iris)`—see raw blob (messy).  
   - Wax Off: Add `print(type(iris))`—expect `<class 'sklearn.utils._bunch.Bunch'>` (data bundle).  
   - Meditate: Data’s unshaped clay—your hands mold it.  
2. **Variables & Structure—Know It (45 min)**  
   - Edit `iris_intro.py`:  
     ```python
     from sklearn.datasets import load_iris
     iris = load_iris()
     X = iris.data  # Features—measurements
     y = iris.target  # Labels—types
     print("Features:", iris.feature_names)  # 4 columns
     print("Classes:", iris.target_names)  # 3 flowers
     print("X shape:", X.shape)  # 150x4
     print("y shape:", y.shape)  # 150
     print("Flower 0:", X[0], "is", iris.target_names[y[0]])
     print("Flower 1:", X[1], "is", iris.target_names[y[1]])
     ```
   - Run: Expect:  
     ```
     Features: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
     Classes: ['setosa' 'versicolor' 'virginica']
     X shape: (150, 4)
     y shape: (150,)
     Flower 0: [5.1 3.5 1.4 0.2] is setosa
     Flower 1: [4.9 3.  1.4 0.2] is setosa
     ```
   - Chop: `X` is 2D—like a QA table (150 rows, 4 cols). `y` is 1D—labels (0=setosa, 1=versicolor, 2=virginica). Indexing: `X[0]` = first row.  
   - Wax On: Print `X[2]`, `y[2]`—third flower.  
   - Wax Off: Print `X[-1]`, `y[-1]`—last flower (-1 from end).  
   - Meditate: Data’s your vision—see its form, feel its pulse.  
3. **Function Practice—Shape It (1 hr)**  
   - Edit `iris_intro.py`:  
     ```python
     from sklearn.datasets import load_iris
     def get_iris_data():  # Load function
         iris = load_iris()
         X = iris.data
         y = iris.target
         print("Features:", iris.feature_names)
         print("Classes:", iris.target_names)
         return X, y  # Two outputs

     X, y = get_iris_data()  # Unpack
     print("First 5 flowers:")
     for i in range(5):  # Loop 0-4
         print(f"Flower {i}: {X[i]} is {iris.target_names[y[i]]}")
     ```
   - Run: See 5 flowers.  
   - Slice: `def` reuses code—`return X, y` splits to two vars. `for` loops—`f"..."` formats (3.12.3 perk).  
   - Wax On: Change to `range(3)`—print 3.  
   - Wax Off: Add `print(f"Last: {X[-1]} is {iris.target_names[y[-1]]}")`—end check.  
   - Meditate: Functions mold—loops carve.  
**Theory**: ML thrives on data—features (X) predict labels (y). Iris: 150 samples, 50 per class, 4 measures—clean, balanced, real.

---

### File 4: monday_march_24_module_3.md
### Module 3: Training a Clean Model—Your Baseline (2.5 hrs)
**Goal**: Build an ML model—split, train, score it.  
**Steps**:  
1. **Splitting—Train vs Test (45 min)**  
   - `nano iris_model.py`:  
     ```python
     from sklearn.datasets import load_iris
     from sklearn.model_selection import train_test_split

     X, y = load_iris().data, load_iris().target  # Quick load
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
     print("Train data:", X_train.shape)  # 120x4
     print("Test data:", X_test.shape)   # 30x4
     print("Train labels:", y_train.shape)  # 120
     print("Test labels:", y_test.shape)    # 30
     ```
   - Run: Expect `(120, 4)`, `(30, 4)`, `(120,)`, `(30,)`.  
   - Cut: `train_test_split` divides—80% train (120), 20% test (30). `test_size=0.2` sets split; `random_state=42` locks randomness.  
   - Wax On: Print `y_train[0:5]`—first 5 train labels.  
   - Wax Off: Set `test_size=0.3`, rerun—105 train, 45 test.  
   - Meditate: Split’s your balance—train learns, test proves.  
2. **Training & Predicting—Forge It (1 hr)**  
   - Edit `iris_model.py`:  
     ```python
     from sklearn.datasets import load_iris
     from sklearn.model_selection import train_test_split
     from sklearn.linear_model import LogisticRegression

     X, y = load_iris().data, load_iris().target
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     model = LogisticRegression(max_iter=200)  # Classifier
     model.fit(X_train, y_train)  # Train
     y_pred = model.predict(X_test)  # Guess
     print("Predictions:", y_pred)  # 30 guesses
     print("Actual:", y_test)      # 30 truths
     ```
   - Run: See arrays—0s, 1s, 2s.  
   - Chop: `LogisticRegression` maps features to labels—linear math. `fit()` learns; `predict()` applies. `max_iter=200` ensures finish.  
   - Wax On: Print `y_pred[0:5]`, `y_test[0:5]`—compare 5.  
   - Wax Off: Add `y_train_pred = model.predict(X_train)`, print it—train guesses.  
   - Meditate: Training forges—predictions temper.  
3. **Scoring—Measure It (45 min)**  
   - Edit `iris_model.py`:  
     ```python
     from sklearn.datasets import load_iris
     from sklearn.model_selection import train_test_split
     from sklearn.linear_model import LogisticRegression
     from sklearn.metrics import accuracy_score

     X, y = load_iris().data, load_iris().target
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     model = LogisticRegression(max_iter=200)
     model.fit(X_train, y_train)
     y_pred = model.predict(X_test)
     accuracy = accuracy_score(y_test, y_pred)
     print("Accuracy:", accuracy)  # ~0.96-0.97
     print(f"Percent: {accuracy * 100:.1f}%")
     ```
   - Run: Expect 96-97%.  
   - Slice: `accuracy_score` counts matches—QA pass rate. High = clean win. `f"..."` formats—3.12.3 style.  
   - Wax On: Add `train_acc = accuracy_score(y_train, model.predict(X_train))`, print it—~0.97.  
   - Wax Off: Change `random_state=0`, rerun—slight shift?  
   - Meditate: Accuracy reflects—clean’s your base.  
**Theory**: Models fit patterns—LogisticRegression draws lines via gradients. Clean Iris = high accuracy; real data’s messier.

---

### File 5: monday_march_24_module_4.md
### Module 4: Poisoning Mechanics—Break It (3 hrs)
**Goal**: Code poisoning—random and targeted—to shatter trust.  
**Steps**:  
1. **Poisoning Function—Craft Your Blade (1 hr)**  
   - Edit `iris_model.py`:  
     ```python
     from sklearn.datasets import load_iris
     from sklearn.model_selection import train_test_split
     from sklearn.linear_model import LogisticRegression
     from sklearn.metrics import accuracy_score
     import numpy as np  # Randomness

     X, y = load_iris().data, load_iris().target
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     def poison_labels(y, poison_percent, targeted=False):
         y_poisoned = y.copy()  # Keep original
         num_poison = int(len(y) * poison_percent)  # Flip count
         indices = np.random.choice(len(y), num_poison, replace=False)  # Random spots
         for idx in indices:  # Flip each
             if targeted and y_poisoned[idx] == 0:  # Setosa -> Versicolor
                 y_poisoned[idx] = 1
             else:  # Random
                 other_labels = [i for i in range(3) if i != y_poisoned[idx]]
                 y_poisoned[idx] = np.random.choice(other_labels)
         print(f"Poisoned {num_poison} at: {indices}")
         print("Flipped to:", y_poisoned[indices])
         return y_poisoned

     model = LogisticRegression(max_iter=200)
     model.fit(X_train, y_train)
     y_pred = model.predict(X_test)
     accuracy = accuracy_score(y_test, y_pred)
     print("Clean Accuracy:", accuracy)
     ```
   - Run: Clean score, function ready.  
   - Cut: `np.random.choice` picks—`replace=False` no repeats. `for` flips—`if targeted` aims, else random. `copy()` saves—arrays bite back.  
   - Wax On: Remove prints, rerun—silent run.  
   - Wax Off: Call `poison_labels(y_train, 0.2)` below, print it—test it.  
   - Meditate: Poison’s your shadow—silent, sharp.  
2. **Testing Poisoning—Swing It (1 hr)**  
   - Add:  
     ```python
     y_train_p10 = poison_labels(y_train, 0.1)  # 10% random
     model_p10 = LogisticRegression(max_iter=200)
     model_p10.fit(X_train, y_train_p10)
     pred_p10 = model_p10.predict(X_test)
     acc_p10 = accuracy_score(y_test, pred_p10)
     print("10% Random Accuracy:", acc_p10)

     y_train_p30 = poison_labels(y_train, 0.3)  # 30% random
     model_p30 = LogisticRegression(max_iter=200)
     model_p30.fit(X_train, y_train_p30)
     pred_p30 = model_p30.predict(X_test)
     acc_p30 = accuracy_score(y_test, pred_p30)
     print("30% Random Accuracy:", acc_p30)

     y_train_p50t = poison_labels(y_train, 0.5, targeted=True)  # 50% targeted
     model_p50t = LogisticRegression(max_iter=200)
     model_p50t.fit(X_train, y_train_p50t)
     pred_p50t = model_p50t.predict(X_test)
     acc_p50t = accuracy_score(y_test, pred_p50t)
     print("50% Targeted Accuracy:", acc_p50t)
     ```
   - Run: Expect drops—e.g., 0.9, 0.8, 0.6.  
   - Chop: 10% (~12 flips) scatters—mild hit. 30% (~36) disrupts. 50% targeted (~60) biases—setosa gone.  
   - Wax On: Add 20% random—copy 10%, tweak, rerun.  
   - Wax Off: Flip 1->2 in targeted—edit `if targeted`, rerun.  
   - Meditate: Random’s chaos—targeted’s intent. Feel it break.  
3. **Analysis—See the Fracture (1 hr)**  
   - Add:  
     ```python
     print("Clean vs Poisoned (First 10):")
     for i in range(10):
         print(f"Sample {i}: Real={y_test[i]}, Clean={y_pred[i]}, 10%={pred_p10[i]}, 30%={pred_p30[i]}, 50%T={pred_p50t[i]}")
     ```
   - Run: Compare—targeted skews (e.g., all 1s).  
   - Slice: Random spreads—targeted rewrites. Loops show it—QA lens.  
   - Wax On: Set `range(5)`—tighter focus.  
   - Wax Off: Add `print(f"Clean correct: {sum(y_pred == y_test)}/30")`—count wins (~29). Repeat for poisoned—see drops.  
   - Meditate: Analysis mirrors—poison twists truth.  
**Theory**: Poisoning exploits trust—models overfit bad labels. Random confuses; targeted shifts—real attacks mix both. Your sim’s small, but the vuln’s vast.

---

### File 6: monday_march_24_module_5.md
### Module 5: Logging & Reflection—Etch Mastery (1 hr)
**Goal**: Record work, solidify lessons—your legacy.  
**Steps**:  
1. **CSV Logging—Your Scroll (30 min)**  
   - Add to `iris_model.py` (from Module 4):  
     ```python
     import csv
     with open('poison_results.csv', 'w', newline='') as f:
         writer = csv.writer(f)
         writer.writerow(['Model', 'Poisoning', 'Accuracy'])
         writer.writerow(['Clean', '0%', accuracy])
         writer.writerow(['Random', '10%', acc_p10])
         writer.writerow(['Random', '30%', acc_p30])
         writer.writerow(['Targeted', '50%', acc_p50t])
     print("Results saved—check poison_results.csv!")
     ```
   - Run, `cat poison_results.csv`: See table—e.g.:  
     ```
     Model,Poisoning,Accuracy
     Clean,0%,0.9667
     Random,10%,0.9
     Random,30%,0.8
     Targeted,50%,0.6
     ```
   - Cut: `csv.writer` logs—QA audit style. `with` closes safe. Rows strike deep.  
   - Wax On: Add 20% result—copy row, tweak, rerun.  
   - Wax Off: Rename to `march_24_results.csv`, rerun—unique it.  
   - Meditate: Logs prove—etched forever.  
2. **Git & Reflection—Your Soul (30 min)**  
   - Commands:  
     - `git add iris_model.py poison_results.csv`  
     - `git commit -m "Monday Masterclass: Poisoning sim done"`  
     - `git push` (or hold—you decide).  
   - `nano cyber_notes.txt` (create if fresh):  
     ```txt
     March 24, 2025 - Sensei’s Lessons:
     Python’s my blade—sharp, swift. Poisoning’s data rot—random scatters, targeted skewers.
     Clean models trust too much; I’ll guard their truth. QA’s root—AI’s sky.
     ```
   - Save, then:  
     - `git add cyber_notes.txt`  
     - `git commit -m "Monday reflections"`  
     - `git push` (or hold).  
   - Slice: Git locks—notes forge your mind.  
   - Wax On: Add: “Targeted’s stealth scares—must counter.”  
   - Wax Off: `git log`—see your path, feel it.  
   - Meditate: Built, broke, logged—rest, master.  

---

