# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 was to explain how a computer system operates using the **IPOS** model (Input, Processing, Output, Storage), classify everyday hardware and software items (including operating system, application, and utility software), and identify computer-based systems encountered in daily life outside of laptops and phones.

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS

**Chosen activity:** Recording and saving a short voice study note using the built-in microphone and Voice Memos on a MacBook Air.

| Stage | What happens in my example? | Possible hardware / component |
|---|---|---|
| Input | Sound waves from my voice enter the laptop, and I click Record/Stop and type a title for the study note. | Built-in microphone, trackpad, and keyboard |
| Processing | The audio hardware converts analog sound waves into digital samples, and the Apple M5 processor encodes the audio stream while RAM holds the active recording buffer. | Apple M5 CPU / audio controller and 16 GB RAM |
| Output | A live moving audio waveform appears on the screen while recording, and I can hear the recorded explanation during playback. | Liquid Retina display and built-in speakers |
| Storage | When I finish recording, the encoded `.m4a` audio file is written permanently so it remains available after shutting down the laptop. | Internal NVMe SSD |

**How the activity moves through IPOS:**  
First, the **input** devices capture both my spoken voice (microphone) and control actions such as naming the note (keyboard and trackpad). Next, during **processing**, the processor and memory convert the raw sound signals into compressed digital audio data and prepare visual waveform frames. Those processed frames and audio signals are sent to **output** hardware (screen and speakers) so I can inspect and listen to the recording immediately. Finally, **storage** saves the resulting file onto the SSD so it persists for future study sessions.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
|---|---|---|---|
| Built-in Keyboard | Hardware | Not applicable | Sends keystrokes and shortcut commands to the computer. |
| Force Touch Trackpad | Hardware | Not applicable | Controls the pointer and registers clicks and gestures. |
| Internal NVMe SSD | Hardware | Not applicable | Stores the operating system, apps, and user files permanently. |
| Built-in Speakers | Hardware | Not applicable | Converts digital audio signals into audible sound output. |
| Apple M5 CPU & 16 GB RAM | Hardware | Not applicable | Executes instructions and holds active program data temporarily. |
| macOS (27.2.1) | Software | Operating system software | Manages hardware resources, memory, storage, permissions, and app scheduling. |
| Visual Studio Code | Software | Application software | Used to write, edit, and organize code and Markdown files. |
| Safari | Software | Application software | Used to browse web pages, documentation, and GitHub. |
| Disk Utility | Software | Utility software | Inspects, verifies, and manages storage volumes and disk health. |
| Terminal / zsh | Software | Utility software | Provides a command-line interface to inspect and control system tools and files. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
|---|---|---|---|
| Metro Smart-Card Fare Gate | Validates commuter tickets and controls station platform entry/exit. | Tapping a contactless smart card or scanning a QR ticket on the reader. | Opening the barrier paddles and showing remaining balance or "Go" on the screen. |
| Digital Supermarket Weighing Scale / POS | Weighs produce accurately, calculates total price, and prints a barcode label. | Placing fruit on the load-cell pan and entering the item PLU code on the keypad. | Displaying weight and price on the LCD screen and printing a price sticker. |
| Automatic Smart Washing Machine | Runs timed wash, rinse, and spin cycles using embedded sensors. | Selecting a wash mode button and water-level/temperature sensor readings. | Driving the drum motor, water valves, and displaying remaining cycle time on LED digits. |

## 3. Commands / tools used
- `sysctl -n machdep.cpu.brand_string` — Checked the processor name (`Apple M5`) without revealing personal identifiers.
- `system_profiler SPHardwareDataType` — Verified core count (`10` cores) and system memory (`16 GB`) locally (personal identifiers such as serial number and UUID omitted).
- Text editor — Created and formatted the Mission 1 IPOS, hardware/software, and everyday systems tables.

## 4. My understanding
Every computing device—whether a laptop or an embedded machine like a metro gate—follows the same IPOS cycle: it accepts raw data as **input**, transforms it through **processing**, presents results via **output**, and optionally saves data in **storage**. Hardware provides the physical circuitry to perform these actions, while software tells the hardware what to do across three clear layers: operating system software (managing resources), application software (user tasks), and utility software (maintenance and diagnostics).

## 5. Difficulties faced
Distinguishing between utility software and application software was slightly confusing at first, especially for developer tools like Terminal.

## 6. How I resolved them
I compared their primary roles: application software helps a user complete end-user work (such as editing documents or browsing), whereas utility software helps inspect, configure, maintain, or manage the computer itself.

## 7. Evidence / files
- `mission-01-computer-basics/README.md`
- [IPOS cycle diagram](../evidence/mission-01/01-ipos-flow-diagram.png)
- [Privacy-safe hardware inspection screenshot](../evidence/mission-01/02-system-hardware-check.png)

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Status:** Committed locally on `main` (ready to push to GitHub).
