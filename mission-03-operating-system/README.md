# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 was to inspect the active operating system, account identity, storage space, and running processes using Terminal, understand how absolute and relative paths work, interpret file permission letters (`r`, `w`, `x`), and explain the core responsibilities of an operating system in my own words.

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
|---|---|---|
| Operating system / system details | Shows the OS name, version, build number, kernel name, and CPU architecture. | `sw_vers` reported `macOS 27.2.1 (Build 26B131)`; `uname -srm` reported `Darwin 27.2.0 arm64`. |
| Current account identity | Identifies which local user account owns the current Terminal session and its permissions. | `whoami` returned `[redacted]` (standard non-root local user account). |
| Available and used storage | Displays total disk size, used space, free capacity, and mount point for the filesystem. | `df -h .` showed `460Gi` total size, `13Gi` used, `300Gi` available (`5%` capacity) mounted on `/`. |
| System activity snapshot | Lists active system daemons and user programs currently managed by the kernel. | `ps -eo pid,ppid,stat,comm` showed PID `1` (`/sbin/launchd`) and background services like `logd` and `configd`. |

---

### Task 3.2 — Understand processes
- **What is a process?** A process is an active, running instance of a program loaded into memory with its own allocated CPU time, memory space, and system resources.
- **What does the PID column represent?** `PID` stands for **Process Identifier**—a unique number assigned by the operating system kernel to distinguish and track each running process (for example, `1` for `/sbin/launchd`).
- **Two examples of processes running on my computer:**
  1. `/sbin/launchd` (PID `1`) — macOS's foundational service manager that launches and supervises system and user processes.
  2. `zsh` / `Safari` / `TextEdit` — interactive user-facing shell or application processes running under the active user session.

---

### Task 3.3 — Understand paths and permissions
- **Absolute vs relative paths:**
  - An **absolute path** starts from the filesystem root `/` and works regardless of your current directory. Example: `/Users/[redacted]/Digita-Detective-8529/mission-03-operating-system`
  - A **relative path** starts from your current working directory (`.` or `..`). Example from inside the repo root: `./mission-03-operating-system` (or `../mission-02-terminal` from inside `mission-03-operating-system`).
- **Inspecting permissions (`ls -l` on `journal.txt`):**
  - Output observed: `-rw-r--r--@ 1 [redacted] staff 97 Nov 25 18:51 journal.txt`
  - Owner permission characters (positions 2–4): `rw-`. This means the file owner can **read** (`r`) and **write/modify** (`w`) the file, while execute (`-`) is disabled because it is a plain text document rather than a runnable script.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows a file's contents to be read (or a directory's names to be listed). | Opening `journal.txt` with `cat`. |
| `w` — Write | Allows a file's contents to be changed (or files created/deleted inside a directory). | Appending a line to `journal.txt`. |
| `x` — Execute | Allows a file to be run as a program; on a directory, allows entering/traversing it. | Running a script or `cd` into a folder. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| Process management | Schedules CPU time among running programs, starts and terminates tasks, and isolates processes from interfering with each other. | Switching smoothly between Terminal, a browser, and background daemons via `launchd`. |
| Memory management | Allocates RAM to active programs, keeps track of free memory, and frees memory when a program closes. | Giving Python and Safari separate RAM regions so one app cannot corrupt another's data. |
| Device management | Communicates with physical hardware components through drivers so apps can use them safely without knowing hardware details. | Handling keyboard input, trackpad gestures, audio speakers, and SSD reads/writes. |
| File management | Organizes data into hierarchical folders and files on storage drives and tracks metadata like sizes and timestamps. | Storing `README.md` inside `mission-03-operating-system` on the APFS filesystem. |
| User interface / shell | Provides a visual desktop or text-based command shell so people can launch apps and issue instructions. | Clicking icons in Finder/macOS GUI or typing commands inside `zsh` in Terminal. |
| Security and permissions | Verifies user identity and enforces read/write/execute rules so unauthorized users or programs cannot alter protected files. | Restricting system folders under `/` while giving the owner `rw-` access to `journal.txt`. |

## 3. Commands / tools used
- `sw_vers` & `uname -srm` — Checked macOS version, build, Darwin kernel release, and `arm64` architecture.
- `whoami` — Checked the current user identity (redacted in public documentation).
- `df -h .` — Displayed human-readable disk usage and available space.
- `ps -eo pid,ppid,stat,comm` — Listed running processes along with their PIDs and parent PIDs.
- `pwd`, `cd`, and `ls -l` — Practised navigating relative/absolute paths and inspecting file permissions.

## 4. My understanding
The operating system acts as the essential bridge between physical hardware and user software. Without it managing processes, RAM, devices, files, and permissions simultaneously, multiple applications could not share one computer safely or reliably.

## 5. Difficulties faced
Interpreting the 10-character permission string (`-rw-r--r--`) and understanding why directories need `x` (execute) permission just to `cd` into them took some review.

## 6. How I resolved them
I broke the permission string into four groups—file type (`-` or `d`), owner (`rwx`), group (`rwx`), and others (`rwx`)—and compared a file (`-rw-r--r--`) against a directory (`drwxr-xr-x`) using `ls -l`.

## 7. Evidence / files
- `mission-03-operating-system/README.md`
- [OS, storage, and process inspection screenshot](../evidence/mission-03/01-os-storage-processes.png)
- [Paths and file permissions screenshot](../evidence/mission-03/02-paths-and-permissions.png)

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Status:** Committed locally on `main` (ready to push to GitHub).
