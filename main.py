import time
import math
from getpass import getpass


# ============================================================
# NEXUS // HELPER FUNCTIONS
# ============================================================

def scan_module(name):
    print(f"Scanning {name}........")
    time.sleep(1)
    print(f"{name}.........ACTIVE")


def check_sequential_numbers(password):
    sequences = [
        "123",
        "234",
        "345",
        "456",
        "567",
        "678",
        "789"
    ]

    for sequence in sequences:
        if sequence in password:
            return True

    return False


def check_alphabet_sequence(password):
    password = password.lower()

    for i in range(len(password) - 2):

        if not (
            password[i].isalpha()
            and password[i + 1].isalpha()
            and password[i + 2].isalpha()
        ):
            continue

        first = ord(password[i])
        second = ord(password[i + 1])
        third = ord(password[i + 2])

        if second == first + 1 and third == second + 1:
            return True

    return False


def check_repetition(password):
    for i in range(len(password) - 2):

        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False


def check_common_password(password):
    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "welcome",
        "letmein",
        "password123",
        "MyPassword123!",
        "123456789",
        "1234567890",
        "qwerty123",
        "admin123",
        "welcome123",
        "iloveyou",
        "monkey",
        "dragon",
        "football",
        "master",
        "login",
        "princess",
        "sunshine",
        "shadow",
        "superman",
        "trustno1",
        "passw0rd",
        "abc123",
        "000000",
        "111111",
        "654321",
        "123123",
        "HelloWorld",
        "Hello123",
        "hello@123",
        "whoareyou"
    ]

    password = password.lower()

    for common in common_passwords:
        if common.lower() in password:
            return True

    return False


# ============================================================
# NEXUS // VERDICT ENGINE
# ============================================================

def generate_verdict(
    vulnerability_count,
    threat_level,
    final_score,
    entropy_level,
    detected_weaknesses
):

    print()
    print("╔══════════════════════════════════════════════╗")
    print("║                NEXUS VERDICT                ║")
    print("╚══════════════════════════════════════════════╝")
    print()

    if final_score >= 86:
        security_status = "SECURE"

    elif final_score >= 71:
        security_status = "LOW RISK"

    elif final_score >= 51:
        security_status = "MODERATE RISK"

    elif final_score >= 31:
        security_status = "HIGH RISK"

    else:
        security_status = "CRITICAL RISK"

    print("SECURITY STATUS :", security_status)
    print("Vulnerabilities :", vulnerability_count)

    print()
    print("SECURITY EXPLANATION")
    print("──────────────────────────────────────────────")

    if vulnerability_count == 0:

        print("[+] No major predictable patterns were detected.")
        print("[+] Password structure appears resistant to common patterns.")

    else:

        print("[!] Predictable patterns were detected.")
        print("[!] These weaknesses reduced the overall security score.")
        print("[!] Strong entropy alone does not guarantee strong security.")
        print()

        if detected_weaknesses:
            print("[!] Detected Weaknesses:")

            for weakness in detected_weaknesses:
                print("    →", weakness)

    print()

    if final_score >= 86:

        print("[+] Password security is strong.")
        print("[+] No major security weaknesses detected.")

    elif final_score >= 71:

        print("[+] Password security is good.")
        print("[!] Minor improvements are recommended.")

    elif final_score >= 51:

        print("[!] Password security is moderate.")
        print("[!] Some weaknesses may reduce resistance to attacks.")

    elif final_score >= 31:

        print("[!] Password security is weak.")
        print("[!] Multiple weaknesses are reducing password security.")
        print(
            "[+] Recommendation : "
            "Create a longer and more unpredictable password."
        )

    else:

        print("[CRITICAL] Password security is extremely weak.")
        print("[!] The password contains significant security weaknesses.")
        print(
            "[+] Recommendation : "
            "Replace this password immediately."
        )

    print()
    print("Security Score :", final_score, "/ 100")
    print("Entropy Level  :", entropy_level)
    print("Threat Level   :", threat_level)


# ============================================================
# NEXUS // ADVISORY ENGINE
# ============================================================

def generate_advisory(
    alphabet_sequence,
    sequential,
    repetition,
    common,
    entropy_level,
    final_score,
    has_lower,
    has_upper,
    has_number,
    has_special
):

    recommendations = []

    # --------------------------------------------------------
    # Pattern Recommendations
    # --------------------------------------------------------

    if common:

        recommendations.append(
            (
                100,
                "Common Password",
                "Use a completely unique password."
            )
        )

    if repetition:

        recommendations.append(
            (
                90,
                "Repetition",
                "Avoid repeating the same character multiple times."
            )
        )

    if sequential:

        recommendations.append(
            (
                80,
                "Sequential Numbers",
                "Avoid predictable number sequences."
            )
        )

    if alphabet_sequence:

        recommendations.append(
            (
                70,
                "Alphabet Sequence",
                "Avoid predictable alphabet patterns."
            )
        )

    # --------------------------------------------------------
    # Character Composition Recommendations
    # --------------------------------------------------------

    if not has_upper:

        recommendations.append(
            (
                50,
                "Missing Uppercase",
                "Add uppercase characters."
            )
        )

    if not has_lower:

        recommendations.append(
            (
                50,
                "Missing Lowercase",
                "Add lowercase characters."
            )
        )

    if not has_number:

        recommendations.append(
            (
                50,
                "Missing Number",
                "Add numbers."
            )
        )

    if not has_special:

        recommendations.append(
            (
                50,
                "Missing Special",
                "Add special characters."
            )
        )

    # --------------------------------------------------------
    # Entropy Recommendation
    # --------------------------------------------------------

    if entropy_level in ["VERY WEAK", "WEAK", "MODERATE"]:

        recommendations.append(
            (
                40,
                "Entropy Weakness",
                "Increase password length and character diversity."
            )
        )

    # --------------------------------------------------------
    # Sort Highest Priority First
    # --------------------------------------------------------

    recommendations.sort(reverse=True)

    # --------------------------------------------------------
    # Advisory UI
    # --------------------------------------------------------

    print()
    print("──────────────────────────────────────────────")
    print("NEXUS ADVISORY")
    print("──────────────────────────────────────────────")
    print("SMART RECOMMENDATIONS")
    print("──────────────────────────────────────────────")
    print()

    # --------------------------------------------------------
    # Weaknesses Exist
    # --------------------------------------------------------

    if recommendations:

        priority, weakness, recommendation = recommendations[0]

        print("PRIMARY WEAKNESS")

        if weakness == "Common Password":
            print("[CRITICAL] Common password pattern detected.")

        elif weakness == "Repetition":
            print("[!] Repeated characters detected.")

        elif weakness == "Sequential Numbers":
            print("[!] Sequential number pattern detected.")

        elif weakness == "Alphabet Sequence":
            print("[!] Alphabet sequence detected.")

        elif weakness == "Entropy Weakness":
            print("[!] Entropy weakness detected.")

        elif weakness == "Missing Uppercase":
            print("[!] Uppercase characters are missing.")

        elif weakness == "Missing Lowercase":
            print("[!] Lowercase characters are missing.")

        elif weakness == "Missing Number":
            print("[!] Numbers are missing.")

        elif weakness == "Missing Special":
            print("[!] Special characters are missing.")

        print("[+] Recommendation :", recommendation)

        # ----------------------------------------------------
        # Additional Weaknesses
        # ----------------------------------------------------

        if len(recommendations) > 1:

            print()
            print("──────────────────────────────────────────────")
            print("ADDITIONAL WEAKNESSES")
            print("──────────────────────────────────────────────")

            for priority, weakness, recommendation in recommendations[1:]:

                if weakness == "Common Password":
                    print("[CRITICAL] Common password pattern detected.")

                elif weakness == "Repetition":
                    print("[!] Repeated characters detected.")

                elif weakness == "Sequential Numbers":
                    print("[!] Sequential number pattern detected.")

                elif weakness == "Alphabet Sequence":
                    print("[!] Alphabet sequence detected.")

                elif weakness == "Entropy Weakness":
                    print("[!] Entropy weakness detected.")

                elif weakness == "Missing Uppercase":
                    print("[!] Uppercase characters are missing.")

                elif weakness == "Missing Lowercase":
                    print("[!] Lowercase characters are missing.")

                elif weakness == "Missing Number":
                    print("[!] Numbers are missing.")

                elif weakness == "Missing Special":
                    print("[!] Special characters are missing.")

                print("[+] Recommendation :", recommendation)

    else:

        print("PRIMARY WEAKNESS")
        print("[+] No major predictable patterns detected.")

    # --------------------------------------------------------
    # Composition Analysis
    # --------------------------------------------------------

    print()
    print("──────────────────────────────────────────────")
    print("COMPOSITION ANALYSIS")
    print("──────────────────────────────────────────────")

    if not has_lower:
        print("[!] Lowercase characters : MISSING")

    if not has_upper:
        print("[!] Uppercase characters : MISSING")

    if not has_number:
        print("[!] Numbers : MISSING")

    if not has_special:
        print("[!] Special characters : MISSING")

    if has_lower and has_upper and has_number and has_special:
        print("[+] All major character types are present.")


# ============================================================
# NEXUS // MAIN PROGRAM
# ============================================================

print("╔══════════════════════════════════════════════╗")
print("║                                              ║")
print("║        N E X U S  //  SECURITY CORE          ║")
print("║          PASSWORD INTELLIGENCE               ║")
print("║                                              ║")
print("╚══════════════════════════════════════════════╝")

print()
print("[ SYSTEM BOOT ]")
print()

print("Nexus Core Online.")
print()

print("Scanning security environment...")
time.sleep(1)
print()


# ============================================================
# MODULE SCAN
# ============================================================

modules = [
    "CORE",
    "PATTERN",
    "THREAT",
    "POLICY"
]

for module in modules:

    scan_module(module)
    print()


print("THREAT ENGINE ........ ACTIVE")
print("ANALYSIS CORE ........ READY")
print()


# ============================================================
# PASSWORD INPUT
# ============================================================

password = getpass("Enter your Password: ")

if not password:

    print()
    print("[!] No password entered.")
    print("[!] NEXUS cannot perform security analysis.")
    print("[+] Please enter a password and try again.")

    exit()
    # return


print()
print("Password captured successfully.")
print()


# ============================================================
# PASSWORD VISIBILITY / BASIC ANALYSIS
# ============================================================

while True:

    print()
    print("╔══════════════════════════════════════════════╗")
    print("║           PASSWORD VISIBILITY                ║")
    print("╚══════════════════════════════════════════════╝")
    print()

    print("[R] Reveal Password")
    print("[H] Hide Password")
    print("[C] Continue to Analysis")
    print()

    length = len(password)

    print("Password Length :", length)

    if length < 8:
        print("Password Length Status : WEAK")

    elif length < 12:
        print("Password Length Status : GOOD")

    else:
        print("Password Length Status : STRONG")


    # --------------------------------------------------------
    # CHARACTER COMPOSITION
    # --------------------------------------------------------

    has_lowercase = any(
        char.islower()
        for char in password
    )

    if has_lowercase:
        print("Lowercase Status : DETECTED")
    else:
        print("Lowercase Status : NOT DETECTED")


    has_uppercase = any(
        char.isupper()
        for char in password
    )

    if has_uppercase:
        print("Uppercase Status : DETECTED")
    else:
        print("Uppercase Status : NOT DETECTED")


    has_number = any(
        char.isdigit()
        for char in password
    )

    if has_number:
        print("Number Status : DETECTED")
    else:
        print("Number Status : NOT DETECTED")


    has_special = any(
        not char.isalnum()
        for char in password
    )

    if has_special:
        print("Special Character Status : DETECTED")
    else:
        print("Special Character Status : NOT DETECTED")


    # --------------------------------------------------------
    # CHARACTER POOL
    # --------------------------------------------------------

    character_pool = 0

    if has_lowercase:
        character_pool += 26

    if has_uppercase:
        character_pool += 26

    if has_number:
        character_pool += 10

    if has_special:
        character_pool += 33

    print("Character Pool :", character_pool)


    # --------------------------------------------------------
    # ENTROPY
    # --------------------------------------------------------

    entropy = length * math.log2(character_pool)

    print(
        "Estimated Entropy :",
        round(entropy, 2),
        "bits"
    )


    if entropy < 30:
        entropy_level = "VERY WEAK"

    elif entropy < 50:
        entropy_level = "WEAK"

    elif entropy < 70:
        entropy_level = "MODERATE"

    elif entropy < 90:
        entropy_level = "STRONG"

    else:
        entropy_level = "VERY STRONG"

    print("Entropy Level :", entropy_level)


    # --------------------------------------------------------
    # BASE SECURITY SCORE
    # --------------------------------------------------------

    score = 0

    if length >= 8:
        score += 20

    if length >= 12:
        score += 10

    if has_lowercase:
        score += 15

    if has_uppercase:
        score += 15

    if has_number:
        score += 20

    if has_special:
        score += 20

    print("Base Security Score :", score, "/ 100")


    # --------------------------------------------------------
    # PASSWORD VISIBILITY COMMAND
    # --------------------------------------------------------

    choice = input("NEXUS > ").lower()

    if choice == "r":

        print("Password:", password)

    elif choice == "h":

        print("Password: *************")

    elif choice == "c":

        print("Continuing To Analysis........")
        break

    else:

        print("Unknown command. NEXUS is judging you. 😏")


# ============================================================
# THREAT ANALYSIS
# ============================================================

if choice == "c":

    print()
    print("╔══════════════════════════════════════════════╗")
    print("║              THREAT ANALYSIS                 ║")
    print("╚══════════════════════════════════════════════╝")
    print()

    print("NEXUS THREAT ENGINE")
    print()

    print("[+] Checking password entropy.............. DONE")
    print("[+] Checking common patterns............... DONE")
    print("[+] Checking sequential characters......... DONE")
    print("[+] Checking repetition patterns........... DONE")
    print("[+] Evaluating password complexity......... DONE")
    print()

    print("THREAT ASSESSMENT")
    print("──────────────────────────────────────────────")


# ============================================================
# PATTERN DETECTION
# ============================================================

pattern_penalty = 0
vulnerability_count = 0
detected_weaknesses = []


# ------------------------------------------------------------
# Alphabet Sequence
# ------------------------------------------------------------

alphabet_sequence = check_alphabet_sequence(password)

if alphabet_sequence:

    print("[!] Alphabet Sequence Pattern : DETECTED")

    pattern_penalty += 10

    detected_weaknesses.append(
        "Alphabet Sequence"
    )

else:

    print("[+] Alphabet Sequence Pattern : NOT DETECTED")


# ------------------------------------------------------------
# Sequential Numbers
# ------------------------------------------------------------

sequential_numbers = check_sequential_numbers(password)

if sequential_numbers:

    print("[!] Sequential Number Pattern : DETECTED")

    pattern_penalty += 10

    detected_weaknesses.append(
        "Sequential Numbers"
    )

else:

    print("[+] Sequential Number Pattern : NOT DETECTED")


# ------------------------------------------------------------
# Repetition
# ------------------------------------------------------------

repetition_pattern = check_repetition(password)

if repetition_pattern:

    print("[!] Repetition Pattern : DETECTED")

    pattern_penalty += 10

    detected_weaknesses.append(
        "Repetition"
    )

else:

    print("[+] Repetition Pattern : NOT DETECTED")


# ------------------------------------------------------------
# Common Password
# ------------------------------------------------------------

common_password = check_common_password(password)

if common_password:

    print("[!] Common Password Pattern : DETECTED")

    pattern_penalty += 10

    detected_weaknesses.append(
        "Common Password"
    )

else:

    print("[+] Common Password Pattern : NOT DETECTED")


# ============================================================
# COMPOSITION WEAKNESSES
# ============================================================

if not has_lowercase:

    detected_weaknesses.append(
        "Missing Lowercase"
    )


if not has_uppercase:

    detected_weaknesses.append(
        "Missing Uppercase"
    )


if not has_number:

    detected_weaknesses.append(
        "Missing Number"
    )


if not has_special:

    detected_weaknesses.append(
        "Missing Special"
    )


# ============================================================
# ENTROPY WEAKNESS
# ============================================================

if entropy_level in [
    "VERY WEAK",
    "WEAK",
    "MODERATE"
]:

    detected_weaknesses.append(
        "Entropy Weakness"
    )


# ============================================================
# VULNERABILITY COUNT
# ============================================================

vulnerability_count = len(
    detected_weaknesses
)

print()
print(
    "Vulnerabilities Detected :",
    vulnerability_count
)

print("Detected Weaknesses :")

for weakness in detected_weaknesses:

    print(
        f"  - {weakness}"
    )


# ============================================================
# ENTROPY PENALTY
# ============================================================

entropy_penalty = 0

if entropy < 30:

    entropy_penalty += 30

elif entropy < 50:

    entropy_penalty += 10

elif entropy < 70:

    entropy_penalty += 5


# ============================================================
# FINAL SCORE
# ============================================================

final_score = (
    score
    - pattern_penalty
    - entropy_penalty
)


if final_score < 0:

    final_score = 0


# ============================================================
# SCORE BREAKDOWN
# ============================================================

print()
print("SCORE BREAKDOWN")
print("──────────────────────────────────────────────")

print(
    "Base Score       : ",
    score
)

print(
    "Pattern Penalty  : ",
    "-",
    pattern_penalty
)

print(
    "Entropy Penalty  : ",
    "-",
    entropy_penalty
)

print("──────────────────────────────────────────────")

print(
    "Final Score      : ",
    final_score,
    "/ 100"
)


# ============================================================
# THREAT LEVEL
# ============================================================

if final_score >= 86:

    threat_level = "SECURE"

elif final_score >= 71:

    threat_level = "LOW"

elif final_score >= 51:

    threat_level = "MEDIUM"

elif final_score >= 31:

    threat_level = "HIGH"

else:

    threat_level = "CRITICAL"


print()
print("THREAT LEVEL   :", threat_level)


# ============================================================
# VERDICT ENGINE
# ============================================================

generate_verdict(
    vulnerability_count,
    threat_level,
    final_score,
    entropy_level,
    detected_weaknesses
)


# ============================================================
# ADVISORY ENGINE
# ============================================================

generate_advisory(
    alphabet_sequence,
    sequential_numbers,
    repetition_pattern,
    common_password,
    entropy_level,
    final_score,
    has_lowercase,
    has_uppercase,
    has_number,
    has_special
)