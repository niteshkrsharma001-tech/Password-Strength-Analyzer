# NEXUS // Password Intelligence

## Description

NEXUS // Password Intelligence is a local-only cybersecurity tool designed to analyze password security and identify common weaknesses.

It evaluates password length, character composition, estimated entropy, predictable patterns, sequential numbers, repeated characters, and common password patterns.

NEXUS then calculates a security score, determines the threat level, identifies vulnerabilities, and provides smart security recommendations to help users create stronger and more unpredictable passwords.

All password analysis is performed locally on the user's system.

Passwords are not stored or transmitted by the application.

## Features

- 🔐 Hidden password input using secure terminal input
- 📊 Password strength scoring from 0–100
- 🧮 Estimated password entropy analysis
- 🔎 Alphabet sequence detection
- 🔢 Sequential number detection
- 🔁 Repetition pattern detection
- 🚨 Common password detection
- ⚠️ Vulnerability tracking and threat assessment
- 🧠 Smart security recommendations
- 📋 Detailed password security profile
- 🛡️ Local-only password analysis
- 💻 Hacker-style terminal interface

## How It Works

NEXUS follows a multi-stage password analysis process:

1. **Password Input**
   - Accepts the password through hidden terminal input.

2. **Basic Analysis**
   - Checks password length.
   - Detects lowercase, uppercase, numbers, and special characters.
   - Calculates the estimated character pool.

3. **Entropy Analysis**
   - Estimates password entropy in bits.
   - Classifies entropy from `VERY WEAK` to `VERY STRONG`.

4. **Pattern Detection**
   - Detects alphabet sequences.
   - Detects sequential numbers.
   - Detects repeated characters.
   - Checks for common password patterns.

5. **Threat Assessment**
   - Tracks detected vulnerabilities.
   - Applies pattern and entropy penalties.
   - Calculates the final security score.
   - Assigns a threat level.

6. **Security Verdict**
   - Generates an overall security status.
   - Explains detected weaknesses.

7. **Smart Advisory**
   - Identifies the primary weakness.
   - Lists additional weaknesses.
   - Provides security recommendations.
   - Generates a password security profile.

## Tech Stack

- **Language:** Python
- **Libraries:** `math`, `time`, `getpass`
- **Interface:** Command-Line / Terminal
- **Platform:** Windows / Cross-platform Python environment
- **Version Control:** Git & GitHub

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/niteshkrsharma001-tech/Password-Strength-Analyzer.git
cd Password-Strength-Analyzer

### 2.Run NEXUS

 python main.py

### 3. Analyze a Password

NEXUS will securely request the password through hidden terminal input and guide you through the analysis process.

Use the following commands when prompted:

R — Reveal password
H — Hide password
C — Continue to analysis 

## Security & Privacy

NEXUS is designed with a local-only password analysis approach.

- 🔒 Passwords are processed locally on the user's system.
- 🚫 Passwords are not stored in files or databases.
- 🚫 Passwords are not transmitted to external servers.
- 🚫 No external API is used for password analysis.
- 👁️ Password input is hidden by default using Python's `getpass`.
- ⚠️ Passwords are displayed only when the user explicitly chooses the `R` (Reveal) option.

> **Note:** NEXUS is an educational cybersecurity project and should not be treated as a replacement for enterprise-grade password auditing or dedicated password-security tools.

## Sample Output

```text
╔══════════════════════════════════════════════╗
║        N E X U S  //  SECURITY CORE          ║
║          PASSWORD INTELLIGENCE               ║
╚══════════════════════════════════════════════╝

[ SYSTEM BOOT ]

Nexus Core Online.

THREAT ENGINE ........ ACTIVE
ANALYSIS CORE ........ READY

Password Length : 13
Lowercase Status : DETECTED
Uppercase Status : DETECTED
Number Status : DETECTED
Special Character Status : DETECTED

Estimated Entropy : 85.41 bits
Entropy Level : STRONG

Base Security Score : 100 / 100

Alphabet Sequence Pattern : NOT DETECTED
Sequential Number Pattern : NOT DETECTED
Repetition Pattern : NOT DETECTED
Common Password Pattern : NOT DETECTED

Vulnerabilities Detected : 0

Final Score : 100 / 100
THREAT LEVEL : SECURE

NEXUS VERDICT

SECURITY STATUS : SECURE

## Project Structure

```text
Password-Strength-Analyzer/
│
├── main.py          # Main NEXUS application
├── README.md        # Project documentation
└── .gitignore       # Git ignored files

## Limitations

NEXUS is an educational password-analysis project and has some intentional limitations:

- Entropy is an estimated theoretical value, not a real-world cracking-time prediction.
- Pattern detection currently focuses on selected common patterns.
- The common-password database is a curated local list.
- NEXUS does not perform live credential or breach-database checks.
- The tool does not store or transmit passwords.

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

