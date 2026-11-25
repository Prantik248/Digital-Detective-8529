# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 was to practise core command-line operations inside the assignment repository, safely create, modify, copy, and rename files inside a dedicated practice directory, understand how flags and pipes alter command output, and learn what a package manager (Homebrew on macOS) does.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
|---|---|---|
| Current-directory display (`pwd`) | Prints the full path of the working directory I am currently inside. | Displayed `/Users/[redacted]/.../Digita-Detective-8529/mission-02-terminal` (and changed when I moved folders). |
| Directory listing (`ls`) | Lists visible files and subfolders in the current directory. | Showed `README.md` and `terminal-practice`. |
| Detailed listing (`ls -l`) | Shows permissions, link count, owner, size in bytes, modification date, and name. | Showed `-rw-r--r--` for files and `drwxr-xr-x` for directories. |
| Change directory (`cd ..` / `cd <folder>`) | Moves the shell session to the parent folder or a target subfolder. | Running `cd ..` stepped up one directory level; running `pwd` confirmed the new location. |
| Create directory (`mkdir terminal-practice`) | Creates a new folder at the specified path. | Created `terminal-practice` cleanly inside `mission-02-terminal`. |
| Create empty file (`touch journal.txt`) | Creates an empty file (or updates its timestamp if it already exists). | Created a 0-byte `journal.txt` file inside `terminal-practice`. |
| Copy file (`cp journal.txt journal-backup.txt`) | Duplicates an existing file to a new path or filename without deleting the original. | Both `journal.txt` and `journal-backup.txt` existed with identical content (`97B`). |
| Move / rename file (`mv journal-backup.txt journal-archive.txt`) | Renames a file or relocates it to another folder. | `journal-backup.txt` disappeared and `journal-archive.txt` appeared with the same contents. |
| Display file contents (`cat journal.txt`) | Prints the full text content of a file directly into the Terminal. | Printed both lines stored inside `journal.txt`. |

---

### Task 2.2 — Practise file changes safely
Inside `mission-02-terminal/terminal-practice/`:
1. Created `journal.txt` with `touch journal.txt`.
2. Wrote the first line using `echo "Day 1: Exploring basic Terminal commands safely." > journal.txt`.
3. Appended a second line using `echo "Day 2: Appending text without erasing line one." >> journal.txt`.
4. Verified both lines with `cat journal.txt`.
5. Copied `journal.txt` to `journal-backup.txt` with `cp`, then renamed the copy to `journal-archive.txt` with `mv`.

**Answers to Task 2.2 questions:**
- **Replacing vs appending (`>` vs `>>`):** Single redirection (`>`) overwrites the target file from the beginning and erases previous lines, whereas double redirection (`>>`) appends new text to the end while keeping existing content intact.
- **Copying vs moving (`cp` vs `mv`):** `cp` creates a second independent copy so both original and copy exist, whereas `mv` renames or relocates the existing file so it only exists at the destination.
- **What `pwd` provides:** It prints the exact absolute path from the root directory `/` down to your current working directory so you always know where commands will execute.
- **Why `ls` is useful:** It lets you verify what files and folders exist in a directory before creating, editing, copying, or removing anything.

---

### Task 2.3 — Understand flags and pipes
- **Normal `ls` vs `ls -lah`:** A plain `ls` displays only visible file and folder names. Adding `-l` shows long-format metadata (permissions, size, timestamp), `-a` reveals hidden entries such as `.` and `..`, and `-h` converts raw byte counts into human-readable units (like `128B` or `97B`).
- **Pipe (`ls -la | head -n 5`):** The pipe symbol (`|`) connects the standard output of the command on the left directly into the standard input of the command on the right. Here, `ls -la` produces the complete detailed directory listing, and `head -n 5` filters that stream to display only the first five lines.

---

### Task 2.4 — Understand package managers
Checked Homebrew with `brew --version` (`Homebrew 7.0.10`) and listed managed packages using `brew list --formula` without installing or uninstalling any software.

A package manager automates finding, downloading, verifying, installing, updating, and removing software tools along with all their required dependencies from trusted repositories. Instead of manually searching websites for installers and tracking updates for each program individually, a single command keeps tools consistent and up to date.

## 3. Commands / tools used
- `pwd`, `ls`, `ls -l`, `ls -lah`, `cd`, `mkdir`, `touch`, `echo`, `cat`, `cp`, `mv` — Used to inspect directories and safely create, edit, copy, rename, and view practice files.
- `|` and `head -n 5` — Used to pipe directory listing output into a line-limiting filter.
- `brew --version` and `brew list --formula` — Used to inspect the installed Homebrew version and existing formula list safely.

## 4. My understanding
The Terminal gives direct, precise control over folders, files, and developer tools. Small syntax differences—like `>` versus `>>` or combining flags like `-lah`—dramatically change what a command does, and pipes let simple single-purpose commands be chained together cleanly.

## 5. Difficulties faced
Remembering to verify my current directory (`pwd`) before running `cp` and `mv` with relative paths took careful attention so files were placed inside `terminal-practice/` rather than the parent folder.

## 6. How I resolved them
I ran `pwd` and `ls -lah` after each step to confirm my exact location and verify that `journal.txt` and `journal-archive.txt` were created in the intended directory.

## 7. Evidence / files
- `mission-02-terminal/README.md`
- [Practice file: journal.txt](terminal-practice/journal.txt)
- [Archived backup: journal-archive.txt](terminal-practice/journal-archive.txt)
- [Basic terminal operations screenshot](../evidence/mission-02/01-basic-terminal-ops.png)
- [Flags, pipes, and Homebrew screenshot](../evidence/mission-02/02-flags-pipes-homebrew.png)

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Status:** Committed locally on `main` (ready to push to GitHub).
