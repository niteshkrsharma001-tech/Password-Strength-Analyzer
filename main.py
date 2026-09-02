import getpass
import time
import math
from getpass import getpass

from numpy import rint

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

    def check_alphabet_sequence(password):
        password = password.lower()

        for i in range(len(password) - 2):
            first = ord(password[i])
            second = ord(password[i + 1])
            third = ord(password[i + 2])

            if second == first + 1 and third == second + 1:
                return True
        return False

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

def generate_verdict(vulnerability_count, threat_level, final_score, entropy_level, detected_weaknesses):

    print()
    print("╔══════════════════════════════════════════════╗")
    print("║                NEXUS VERDICT                 ║")
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
        # print()
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
        print("[+] Recommendation : Create a longer and more unpredictable password.")

    else:
        print("[CRITICAL] Password security is extremely weak.")
        print("[!] The password contains significant security weaknesses.")
        print("[+] Recommendation : Replace this password immediately.")
        # print()
        print()
    print("Security Score :", final_score, "/ 100")
    print("Entropy Level  :", entropy_level)
    print("Threat Level   :", threat_level)

def generate_advisory(alphabet_sequence, sequential, repetition, common,entropy_level, final_score, has_lower, has_upper, has_number, has_special ):
    print()
    print("NEXUS ADVISORY")
    print("──────────────────────────────────────────────")
    print("SMART RECOMMENDATIONS")
    print("──────────────────────────────────────────────")
    print()

    # if final_score >= 86:
    #     print("[+] Password security is strong.")
    #     print("[+] No major improvements required.")

    # elif final_score >= 71:
    #     print("[+] Password security is good.")
    #     print("[!] Minor improvements can make it stronger.")

    # elif final_score >= 51:
    #     print("[!] Password security is moderate.")
    #     print("[+] Consider increasing length and character diversity.")

    # elif final_score >= 31:
    #     print("[!] Password security is weak.")
    #     print("[+] Create a longer and more unpredictable password.")

    # else:
    #     print("[CRITICAL] Password security is extremely weak.")
    #     print("[+] Replace this password with a stronger one.")

    # if common:
    #     print("[CRITICAL] Common password pattern detected.")
    #     print("[+] Recommendation : Use a completely unique password.")

    # elif repetition:
    #     print("[!] Repeated characters detected.")
    #     print("[+] Recommendation : Avoid repeating the same character multiple times.")

    # elif sequential:
    #     print("[!] Sequential number pattern detected.")
    #     print("[+] Recommendation : Avoid predictable number sequences.")

    # elif alphabet_sequence:
    #     print("[!] Alphabet sequence detected.")
    #     print("[+] Recommendation : Avoid predictable alphabet patterns.")

    # else:
    #     print("[+] No major predictable patterns detected.")
    # if alphabet_sequence:
    #     print("[!] Alphabet sequence detected.")
    #     print("[+] Recommendation : Avoid predictable alphabet patterns.")

    # if common:
    #     print("[!] Your password contains a common password pattern.")
    #     print("[+] Recommendation : Use a unique password.")

    # if sequential:
    #     print("[!] Sequential numbers detected.")
    #     print("[+] Recommendation : Avoid predictable number sequences.")

    # if repetition:
    #     print("[!] Repeated characters detected.")
    #     print("[+] Recommendation : Avoid repeating the same character multiple times.")

    # if common:
    #     print("PRIMARY WEAKNESS")
    #     print("[CRITICAL] Common password pattern detected.")
    #     print("[+] Recommendation : Use a completely unique password.")

    # elif repetition:
    #     print("PRIMARY WEAKNESS")
    #     print("[!] Repeated characters detected.")
    #     print("[+] Recommendation : Avoid repeating the same character multiple times.")

    # elif sequential:
    #     print("PRIMARY WEAKNESS")
    #     print("[!] Sequential number pattern detected.")
    #     print("[+] Recommendation : Avoid predictable number sequences.")

    # elif alphabet_sequence:
    #     print("PRIMARY WEAKNESS")
    #     print("[!] Alphabet sequence detected.")
    #     print("[+] Recommendation : Avoid predictable alphabet patterns.")

    # else:
    #     print("[+] No major predictable patterns detected.")
    # print()

    primary_weakness = None

    if common:
        primary_weakness = "Common Password"
        print("PRIMARY WEAKNESS")
        print("[CRITICAL] Common password pattern detected.")
        print("[+] Recommendation : Use a completely unique password.")

    elif repetition:
        primary_weakness = "Repetition"
        print("PRIMARY WEAKNESS")
        print("[!] Repeated characters detected.")
        print("[+] Recommendation : Avoid repeating the same character multiple times.")

    elif sequential:
        primary_weakness = "Sequential Numbers"
        print("PRIMARY WEAKNESS")
        print("[!] Sequential number pattern detected.")
        print("[+] Recommendation : Avoid predictable number sequences.")

    elif alphabet_sequence:
        primary_weakness = "Alphabet Sequence"
        print("PRIMARY WEAKNESS")
        print("[!] Alphabet sequence detected.")
        print("[+] Recommendation : Avoid predictable alphabet patterns.")

    else:
        print("PRIMARY WEAKNESS")
        print("[+] No major predictable patterns detected.")
        print()
    if primary_weakness and vulnerability_count > 1:
        print()
        print("──────────────────────────────────────────────")
        print("ADDITIONAL WEAKNESSES")
        print("──────────────────────────────────────────────")

    if common and primary_weakness != "Common Password":
        print("[CRITICAL] Common password pattern detected.")
        print("[+] Recommendation : Use a completely unique password.")

    if repetition and primary_weakness != "Repetition":
        print("[!] Repeated characters detected.")
        print("[+] Recommendation : Avoid repeating the same character multiple times.")

    if sequential and primary_weakness != "Sequential Numbers":
        print("[!] Sequential number pattern detected.")
        print("[+] Recommendation : Avoid predictable number sequences.")

    if alphabet_sequence and primary_weakness != "Alphabet Sequence":
        print("[!] Alphabet sequence detected.")
        print("[+] Recommendation : Avoid predictable alphabet patterns.")
        print()
        print("──────────────────────────────────────────────")
        print("COMPOSITION ANALYSIS")
        print("──────────────────────────────────────────────")

    if not has_lower:
        print("[!] Lowercase characters are missing.")
        print("[+] Recommendation : Add lowercase characters.")

    if not has_upper:
        print("[!] Uppercase characters are missing.")
        print("[+] Recommendation : Add uppercase characters.")

    if not has_number:
        print("[!] Numbers are missing.")
        print("[+] Recommendation : Add numbers.")

    if not has_special:
        print("[!] Special characters are missing.")
        print("[+] Recommendation : Add special characters.")

    if has_lower and has_upper and has_number and has_special:
        print("[+] All major character types are present.")
        
    if entropy_level == "VERY WEAK":
        print("[!] Password entropy is very weak.")
        print("[+] Recommendation : Increase password length and complexity.")

    elif entropy_level == "WEAK":
        print("[!] Password entropy is weak.")
        print("[+] Recommendation : Increase password length and character diversity.")

    elif entropy_level == "MODERATE":
        print("[!] Password entropy is moderate.")
        print("[+] Recommendation : Increase password length and randomness.")

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
        print("Base Security Score : ", score, "/ 100")

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

# pattern_penalty
pattern_penalty = 0
vulnerability_count = 0
detected_weaknesses = []
alphabet_sequence = check_alphabet_sequence(password)

if alphabet_sequence:
    print("[!] Alphabet Sequence Pattern : DETECTED")
    pattern_penalty += 10
    vulnerability_count += 1
    detected_weaknesses.append("Alphabet Sequence")
else:
    print("[+] Alphabet Sequence Pattern : NOT DETECTED")
sequential_numbers = check_sequential_numbers(password)

if sequential_numbers:
    print("[!] Sequential Number Pattern : DETECTED")
    pattern_penalty += 10
    vulnerability_count += 1
    detected_weaknesses.append("Sequential Numbers")
else:
    print("[+] Sequential Number Pattern : NOT DETECTED")

repetition_pattern = check_repetition(password)

if repetition_pattern:
    print("[!] Repetition Pattern : DETECTED")
    pattern_penalty += 10
    vulnerability_count += 1
    detected_weaknesses.append("Repetition")
else:
    print("[+] Repetition Pattern : NOT DETECTED")

common_password = check_common_password(password)

if common_password:
    print("[!] Common Password Pattern : DETECTED")
    pattern_penalty += 10
    vulnerability_count += 1
    detected_weaknesses.append("Common Password")
else:
    print("[+] Common Password Pattern : NOT DETECTED")
print()
# print()
print("Vulnerabilities Detected :", vulnerability_count)
print("Detected Weaknesses :")
for weakness in detected_weaknesses:
    print(f"  - {weakness}")
# ENTROPY PENALTY
entropy_penalty = 0

if entropy < 30:
    entropy_penalty += 30
elif entropy < 50:
    entropy_penalty += 10
elif entropy < 70:
    entropy_penalty += 5

# FINAL SCORE

final_score = score - pattern_penalty - entropy_penalty

if final_score < 0:
    final_score = 0

# SCORE BREAKDOWN    
print()
print("SCORE BREAKDOWN")
print("──────────────────────────────────────────────")
print("Base Score       : ",  score)
print("Pattern Penalty  : ", "-", pattern_penalty)
print("Entropy Penalty  : ", "-", entropy_penalty)
print("──────────────────────────────────────────────")
print("Final Score      : ", final_score, "/ 100")

# THREAT LEVEL

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
print("FINAL SCORE    :", final_score, "/ 100")

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