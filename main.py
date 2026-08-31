import getpass
import time
import math
from getpass import getpass

def scan_module(name):
    print(f"Scanning {name}........")
    time.sleep(1)
    print(f"{name}.........ACTIVE")

print("╔══════════════════════════════════════════════╗")
print("║                                              ║")
print("║        N E X U S  //  SECURITY CORE          ║")
print("║          PASSWORD INTELLIGENCE               ║")
print("║                                              ║")
print("╚══════════════════════════════════════════════╝")

print("[ SYSTEM BOOT ]")
print()

print()
print("Nexus Core Online.")
print()

print("Scanning security environment...")
time.sleep(1)
print()

modules = ["CORE","PATTERN","THREAT","POLICY"]

for module in modules:
    scan_module(module)
    print()

    def check_sequential_numbers(password):
        sequences = ["123", "234", "345", "456", "567", "678", "789"]

        for sequence in sequences:
            if sequence in password:
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
            "password",
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
        ]

        password = password.lower()

        for common in common_passwords:
            if common in password:
                return True

        return False
        password = password.lower()
        for common in common_passwords:
            if common in password:
                return True

        return False

def generate_advisory(sequential, repetition, common):
    print()
    print("NEXUS ADVISORY")
    print("──────────────────────────────────────────────")

    if common:
        print("[!] Your password contains a common password pattern.")
        print("[+] Recommendation : Use a unique password.")

    if sequential:
        print("[!] Sequential numbers detected.")
        print("[+] Recommendation : Avoid predictable number sequences.")

    if repetition:
        print("[!] Repeated characters detected.")
        print("[+] Recommendation : Avoid repeating the same character multiple times.")

print()
print("THREAT ENGINE ........ ACTIVE")
# print()
print("ANALYSIS CORE ........ READY")
print()
password = getpass("Enter your Password: ")
print("Password captured successfully.")
print()

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
    print("Password Length: ", length)

    if length <8:
        print("Password Length Status : WEAK")
    elif length <12:
        print("Password Length Status : GOOD")
    else:
        print("Password Length Status : STRONG")

    has_lowercase = any(char.islower() for char in password)
    if has_lowercase:
        print("Lowercase Status : DETECTED")
    else:
        print("Lowercase Status : NOT DETECTED")

    has_uppercase = any(char.isupper() for char in password)
    if  has_uppercase:
        print("Uppercase status : DETECTED")
    else:
        print("Uppercase status : NOT DETECTED")

    has_number = any(char.isdigit() for char in password)
    if has_number:
        print("Number Status : DETECTED")
    else:
        print("Number Status : NOT DETECTED")

    has_special = any(not char.isalnum() for char in password)
    if has_special:
        print("Special Character Status : DETECTED")
    else:
        print("Special Character Status : NOT DETECTED")

    character_pool = 0

    if has_lowercase:
        character_pool += 26

    if has_uppercase:
        character_pool += 26

    if has_number:
        character_pool += 10

    if has_special:
        character_pool += 33  # Assuming 33 special characters

    print("Character Pool :", character_pool)

    entropy = length * math.log2(character_pool)
    print("Estimated Entropy :", round(entropy, 2), "bits")

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
        print("Security Score : ", score)

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

pattern_penalty = 0

sequential_numbers = check_sequential_numbers(password)

if sequential_numbers:
    print("[!] Sequential Number Pattern : DETECTED")
    pattern_penalty += 10
else:
    print("[+] Sequential Number Pattern : NOT DETECTED")

repetition_pattern = check_repetition(password)

if repetition_pattern:
    print("[!] Repetition Pattern : DETECTED")
    pattern_penalty += 10
else:
    print("[+] Repetition Pattern : NOT DETECTED")

common_password = check_common_password(password)

if common_password:
    print("[!] Common Password Pattern : DETECTED")
    pattern_penalty += 10
else:
    print("[+] Common Password Pattern : NOT DETECTED")

final_score = score - pattern_penalty


if final_score < 0:
    final_score = 0

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

entropy_penalty = 0
if entropy < 30:
    entropy_penalty += 30
elif entropy < 50:
    entropy_penalty += 20
elif entropy < 70:
    entropy_penalty += 10
final_score = score - pattern_penalty - entropy_penalty

print()
print("Threat Level :", threat_level)
print("Security Score :", final_score, "/ 100")

generate_advisory(
    sequential_numbers,
    repetition_pattern,
    common_password
)
