# NEXUS // Password Intelligence

> A local-only Python cybersecurity tool for password security analysis, threat assessment, and security recommendations.

---

## Overview

**NEXUS // Password Intelligence** is a Python-based cybersecurity project designed to analyze password security and identify common weaknesses.

The tool evaluates:

- Password length
- Character composition
- Estimated entropy
- Predictable patterns
- Sequential numbers
- Alphabet sequences
- Repeated characters
- Common password patterns
- Vulnerabilities
- Multiple security risk categories

NEXUS combines these findings to calculate a **security score**, determine a **threat level**, generate a **security verdict**, and provide **smart security recommendations**.

All password analysis is performed locally on the user's system.

> **Privacy:** Passwords are not stored or transmitted by the application.

## Tech Stack

- **Language:** Python
- **Libraries:** `math`, `time`, `getpass`
- **Interface:** Command-Line / Terminal
- **Platform:** Windows / Cross-platform Python environment
- **Version Control:** Git & GitHub
---
## Installation

### Requirements

Before running NEXUS, make sure you have:

- Python 3.x
- Git
- A terminal / command prompt

NEXUS uses only Python standard-library modules, so no external packages are required.

### 1. Clone the Repository

```bash
git clone https://github.com/niteshkrsharma001-tech/Password-Strength-Analyzer.git
cd Password-Strength-Analyzer
python main.py
# =============================================================================================
# python main.py       

# Enter your Password:

# Password captured successfully.

# NEXUS will then perform the security analysis and generate the final verdict.
# =============================================================================================
## Features

- 🔐 Hidden password input using Python `getpass`
- 👁️ Password reveal / hide functionality
- 📊 Security score from `0–100`
- 🧮 Estimated password entropy analysis
- 🔎 Alphabet sequence detection
- 🔢 Sequential number detection
- 🔁 Repetition pattern detection
- 🚨 Common password detection
- ⚠️ Vulnerability tracking
- 🛡️ Pattern risk assessment
- 🧠 Predictability risk analysis
- 🔐 Complexity risk analysis
- 📏 Length risk analysis
- ⚔️ Attack exposure assessment
- 🚨 Threat score and threat level
- 📋 Detailed security verdict
- 💡 Smart security advisory
- 💻 Cybersecurity-focused terminal interface
- 🔒 Local-only password analysis

---

## How It Works

NEXUS processes a password through multiple analysis stages.

### 1. Password Input

The password is collected using Python's `getpass` module so that it is hidden during normal terminal input.

The user can also choose to:

- `R` — Reveal password
- `H` — Hide password
- `C` — Continue to analysis

---

### 2. Basic Password Analysis

NEXUS analyzes the basic characteristics of the password.

It checks:

- Password length
- Lowercase characters
- Uppercase characters
- Numbers
- Special characters

It also calculates an estimated **character pool** based on the detected character types.

---

### 3. Entropy Analysis

NEXUS estimates password entropy using the detected character pool and password length.

The estimated entropy is classified into:

| Entropy | Classification |
|---|---|
| `< 30 bits` | VERY WEAK |
| `30–49 bits` | WEAK |
| `50–69 bits` | MODERATE |
| `70–89 bits` | STRONG |
| `90+ bits` | VERY STRONG |

> Entropy is an estimated theoretical measure and should not be interpreted as an exact prediction of real-world cracking time.

---

### 4. Pattern Detection

NEXUS checks for predictable password patterns including:

- Alphabet sequences
- Sequential numbers
- Repeated characters
- Common passwords

Examples of predictable patterns include sequences such as:

```text
abc
123
aaa
password123

## Future Improvements

Planned improvements for future versions include:

- Expanded common-password and pattern databases
- More advanced password pattern detection
- Improved password strength modelling
- Configurable security policies
- Password generation capabilities
- More detailed attack-resistance estimation
- Enhanced terminal UI and reporting
- Unit testing and automated test coverage

## License

This project is created for educational and portfolio purposes.
