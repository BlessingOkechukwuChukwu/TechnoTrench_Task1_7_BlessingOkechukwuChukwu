import re

def check_password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        score += len(password)

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 5
    else:
        feedback.append("Include uppercase letters for a stronger password.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 5
    else:
        feedback.append("Include lowercase letters for a stronger password.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 5
    else:
        feedback.append("Include numbers for a stronger password.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 5
    else:
        feedback.append("Include special characters for a stronger password.")

    # Evaluate strength based on score
    if score < 20:
        strength = "Weak"
    elif score < 30:
        strength = "Moderate"
    elif score < 40:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback

def main():
    while True:
        password = input("Enter a password to check its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            break

        strength, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        
        if feedback:
            print("Suggestions for improvement:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("Great job! Your password is very strong.")

        print()

if __name__ == "__main__":
    main()