#  Bank Queue Simulation
A **command-line bank simulation system** built in Python using core data structures — queues, stacks and dictionaries. Clients are assigned to teller windows based on priority, and every completed transaction is stored in a history log.

> A graphical interface (GUI) is planned for a future version.
---
## How It Works
When a client enters the system, they are assigned a **priority level**:
- **Priority 1** — Preferential (elderly, pregnant, disabled)
- **Priority 2** — Regular
Clients wait in their respective queue and are automatically assigned to the next available teller window. Once served, they are pushed onto that window's **history stack**.

---

## Features
| # | Feature | Description |
|---|---------|-------------|
| 1 | Add Client | Register a client with ID, name, transaction type and priority |
| 2 | Finish Service | Mark a client as served and pull the next one from the queue |
| 3 | Toggle Window | Activate or deactivate any of the 3 teller windows |
| 4 | View Queue | See all clients currently waiting, sorted by priority |
| 5 | View Windows | See the status and current client of each window |
| 6 | History by Window | View the last N clients served at a specific window |
| 7 | General History | View the last N clients served across all windows |
| 8 | Report by Count | Total clients served per priority level |
| 9 | Report by Detail | Full detail of clients served per priority level |

---

## Data Structures Used

- **Queue (list)** — Manages the waiting line for each priority level. New clients are added to the back, served clients are removed from the front (`pop(0)`).
- **Stack (list)** — Each teller window keeps a history stack. Completed clients are pushed on top and can be reviewed in reverse order (most recent first).
- **Dictionary** — Represents each teller window with its state, current client, and history stack.
---
## Menu
```
MENU
1. Add client
2. Finish service
3. Toggle window on/off
4. View queue
5. View windows
6. Last served (by window)
7. Last served (all windows)
8. Report — quantity by priority
9. Report — detail by priority
0. Exit
```
---
## Project Structure

```
banco-colas/
│
├── Main.py       # All logic and main menu loop
└── README.md
```
---
##  How to Run
### Requirements
- Python 3.8 or higher
### Run
```bash
python Main.py
`
No external libraries needed — runs with pure Python. 
---

## Business Rules

- Duplicate IDs are not allowed in the queue
- Priority 1 clients are always served before Priority 2
- When a window becomes free, the next client is assigned automatically
- indows can be toggled on/off at any time

---
## Future Plans
- [ ] Build a graphical interface using **Kivy** or **Tkinter**
- [ ] Add visual queue display with real-time updates
- [ ] Export reports to `.txt` or `.csv`
---
## Author
**Paulina Rojas** — [@paulina-rc](https://github.com/paulina-rc)

> Academic project — Data Structures & Web Development, 11th Grade
