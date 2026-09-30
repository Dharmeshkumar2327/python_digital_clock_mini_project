# 🕐 Python Digital Clock

A simple and interactive **Digital Clock application built using Python and Tkinter**. The project displays the current time, day, date, and year in a clean desktop GUI and updates automatically every second.

## 🚀 Project Overview

This project is a beginner-friendly Python GUI application designed to demonstrate how **Tkinter**, Python functions, and the `strftime()` function can be used to create a real-time digital clock.

The application creates a **700 × 350** desktop window with a dark-themed interface.

The clock continuously updates the displayed time and date using Tkinter's scheduling mechanism.

---

## ✨ Features

* ⏰ Real-time digital clock
* 📅 Displays current day and date
* 🔄 Automatically updates every second
* 🖥️ Desktop GUI application
* 🎨 Dark-themed interface
* 🐍 Built using Python
* 📦 No external Python packages required

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter**
* **time module**
* **`strftime()`**

---

## 📂 Project Structure

```text
Python-Digital-Clock/
│
├── 01_Python_Digital_clock_mini_Project.py
├── README.md
└── screenshots/
    └── digital-clock.png
```

---

## ⚙️ How It Works

The project imports Tkinter for creating the graphical interface and `strftime` for obtaining the current time and date.

```python
import tkinter as tk
from time import strftime
```

The main application window is then created using Tkinter.

### ⏰ Time Display

The current time is formatted using:

```python
time = strftime("%I:%M:%S %p")
```

This displays the time in **12-hour format with AM/PM**.

Example:

```text
01:45:32 PM
```

### 📅 Date Display

The current date is formatted using:

```python
date = strftime("%A, %d %B %Y")
```

Example:

```text
Wednesday, 30 September 2026
```

### 🔄 Automatic Updates

The clock refreshes every second using:

```python
root.after(1000, update_clock)
```

This allows the displayed time to remain synchronized with the system clock.

---

## 🎨 User Interface

The application uses a dark background and large typography for the clock display.

The main components include:

* **DIGITAL CLOCK** title
* Large time display
* Current date display
* Dark background
* High-contrast text

The time is displayed using a large **60-point bold font**.

---

This project helps demonstrate:

* Python GUI programming
* Tkinter widgets
* Python functions
* Date and time formatting
* Real-time GUI updates
* Event scheduling
* `strftime()` formatting
* Basic desktop application development

---

## 🔮 Future Enhancements

Some features that can be added in future versions:

* ⏱️ Stopwatch
* ⏳ Countdown timer
* 🔔 Alarm clock
* 🌍 World clock
* 🌙 Dark/Light mode
* 🎨 Custom themes
* ⚙️ Customizable fonts and colors
* 📅 Calendar integration

---

## 👨‍💻 Author

### Dharmesh Kumar

**Data Analyst | Python | SQL | Power BI | Machine Learning | DSA**

GitHub:
https://github.com/Dharmeshkumar2327

---

## ⭐ Show Your Support

If you found this project useful or interesting, please consider giving the repository a ⭐ **Star**.

---

## 📄 License

This project is licensed under the MIT License.

You are free to use, copy, modify, merge, publish, distribute,
sublicense, and sell copies of this project, subject to the
conditions of the MIT License.

See the LICENSE file for the complete license text.
