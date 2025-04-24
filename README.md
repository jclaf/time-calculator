# Time calculator project

Cet algorithme permet d’additionner une durée à une heure de départ, en tenant compte du format 12h/24h, du changement de jour, et éventuellement du jour de la semaine.

---

## Description du Code

### 1. Fonction `add_time`

#### a. **Initialisation et Parsing des Paramètres**

```python
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

start_hour = int(start.split(" ")[0].split(":")[0])
start_minute = int(start.split(" ")[0].split(":")[1])
start_format = start.split(" ")[1]
```
- **`start`** : Heure de départ, ex. `'8:16 PM'`.
- **`duration`** : Durée à ajouter, ex. `'466:02'`.
- **`day`** (optionnel) : Jour de la semaine, ex. `'Tuesday'`.
- **`week`** : Liste des jours pour le calcul du jour final.
- On extrait l'heure, les minutes et le format (`AM` ou `PM`) de l'heure de départ.

#### b. **Conversion au format 24h**

```python
if start_format == "PM" and start_hour != 12:
    start_hour += 12
if start_format == "AM" and start_hour == 12:
    start_hour = 0
```
- Pour faciliter les calculs, on convertit l'heure de départ en format 24h.

#### c. **Parsing de la durée**

```python
duration_hour = int(duration.split(" ")[0].split(":")[0])
duration_minute = int(duration.split(" ")[0].split(":")[1])
```
- On extrait les heures et minutes de la durée à ajouter.

#### d. **Addition des minutes et gestion du dépassement**

```python
new_time_minute = start_minute + duration_minute
if new_time_minute >= 60:
    new_time_minute -= 60
    start_hour += 1
```
- On additionne les minutes. Si on dépasse 60, on ajoute 1 à l'heure et on ajuste les minutes.

#### e. **Calcul des heures et des jours écoulés**

```python
countHours = (start_hour + duration_hour) % 12
countDay = (start_hour + duration_hour) // 24
remaining = (start_hour + duration_hour) % 24
```
- **`countDay`** : Nombre de jours entiers passés.
- **`remaining`** : Heure finale en format 24h.

#### f. **Conversion au format 12h**

```python
if remaining == 0:
    new_time_hour = 12
    new_time_format = "AM"
elif 1  12
    new_time_hour = remaining - 12
    new_time_format = "PM"
```
- On convertit l'heure finale en format 12h avec le bon suffixe AM/PM.

#### g. **Calcul du jour de la semaine (si précisé)**

```python
if day:
    day_index = week.index(day.capitalize())
    new_index = (day_index + countDay) % 7
    new_day_name = week[new_index]
    day_name = f', {new_day_name}'
else:
    day_name = ''
```
- Si un jour est donné, on calcule le nouveau jour après avoir ajouté le nombre de jours écoulés.

#### h. **Affichage du nombre de jours passés**

```python
if countDay == 0:
    new_day = ''
elif countDay == 1:
    new_day = f' (next day)'
else:
    new_day = f' ({countDay} days later)'
```
- On ajoute une mention si on est passé au(x) jour(s) suivant(s).

#### i. **Construction et retour du résultat**

```python
new_time = f"{new_time_hour}:{new_time_minute:02d} {new_time_format}{day_name}{new_day}"
print(new_time)
return new_time
```
- On assemble la chaîne finale à retourner et à afficher.

---

### 2. Exemple d’Appel

```python
if __name__ == "__main__":
    add_time('8:16 PM', '466:02')
```
- Additionne 466 heures et 2 minutes à 8:16 PM.

---

## Algorithme Utilisé

### **Addition d'heures et de minutes avec gestion du format 12h/24h et du jour de la semaine**

- **Parsing** : On extrait les composantes de l’heure et de la durée.
- **Conversion** : On travaille en format 24h pour simplifier l’addition.
- **Addition** : On additionne heures et minutes, en reportant les dépassements.
- **Jour de la semaine** : Si besoin, on utilise l’arithmétique modulaire pour trouver le nouveau jour.
- **Formatage** : On convertit le résultat au format 12h, avec gestion d’AM/PM, du jour, et du nombre de jours passés.
