# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 was to write and execute a simple one-line Python program (`hello.py`) that prints `"Hello from Python"`, and to compare how compilers and interpreters translate and execute computer programs.

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created `mission-04-programs/hello.py` containing `print("Hello from Python")`.
- Executed the script in Terminal using `python3 hello.py` and verified that `Hello from Python` printed cleanly to the screen.

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates the entire source code file into machine code **before** the program runs. | Reads, translates, and executes instructions **at runtime** while the program is running. |
| Typical output | Produces a standalone compiled binary or executable file (such as an `.exe` or macOS Mach-O binary). | Produces direct runtime behavior and console/UI output without generating a standalone binary executable. |
| One example | `clang` / `gcc` (C, C++), Rust (`rustc`) | Python (`python3`), Ruby, Node.js (with JIT) |
| One advantage | Compiled programs usually run much faster and do not require the original source code or compiler on the user's machine to run. | Easier and faster to test small changes immediately, and the same source script runs on any OS that has the interpreter installed. |

**Explanation in my own words:**  
As shown in the comparison table, a compiler translates the whole program ahead of time into a standalone executable file before any user runs it, which makes execution very fast later. An interpreter instead reads and runs instructions on the fly at runtime, so you can edit a file like `hello.py` and run `python3 hello.py` right away without a separate build step. Because of this difference, compilers excel at high-speed finished applications, while interpreters excel at rapid development, scripting, and portability. Modern languages like Python often combine ideas—compiling source into internal bytecode first and then interpreting that bytecode.

## 3. Commands / tools used
- `which python3` — Located the Python 3 interpreter executable on the system (`/usr/bin/python3`).
- `cat hello.py` — Displayed the single-line source code inside `hello.py`.
- `python3 hello.py` — Ran the Python interpreter on `hello.py` and printed `Hello from Python`.

## 4. My understanding
Source code is human-readable text, whereas the CPU only executes low-level machine instructions. Compilers and interpreters solve that gap in two different ways: compilers translate everything up front into an executable, while interpreters execute instructions dynamically when you run the script.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [hello.py](hello.py)
- `mission-04-programs/README.md`
- [Running hello.py in Terminal](../evidence/mission-04/01-hello-python-run.png)
- [Compiler vs Interpreter pipeline diagram](../evidence/mission-04/02-compiler-vs-interpreter.png)

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Status:** Committed locally on `main` (ready to push to GitHub).
