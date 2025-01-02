import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback, score

if __name__ == "__main__":
    while True:
        password = input("Enter your password to check its strength: ")
        strength, feedback, score = check_password_strength(password)

        if score == 5:
            print(f"\nPassword Strength: {strength}")
            print("Your password is strong and meets all the criteria!")
            break
        else:
            print(f"\nPassword Strength: {strength}")
            print("Feedback for improvement:")
            for f in feedback:
                print(f"- {f}")
            print("\nPlease try again.")
