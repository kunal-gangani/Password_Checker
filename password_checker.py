import re
import math
from collections import Counter

class PasswordStrengthChecker:
    def __init__(self):
        self.common_passwords = ['password', '123456', '12345678', 'qwerty', 'abc123', 
                                 'monkey', '1234567', 'letmein', 'trustno1', 'dragon']
        self.common_patterns = [r'123', r'abc', r'qwerty', r'password']
    
    def check_length(self, password):
        """Check if password meets minimum length requirement"""
        length = len(password)
        if length < 8:
            return 0, "Too short (minimum 8 characters)"
        elif length < 12:
            return 1, "Acceptable length"
        elif length < 16:
            return 2, "Good length"
        else:
            return 3, "Excellent length"
    
    def check_character_variety(self, password):
        """Check for variety of character types"""
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        variety_count = sum([has_lower, has_upper, has_digit, has_special])
        
        if variety_count == 4:
            return 3, "Excellent variety"
        elif variety_count == 3:
            return 2, "Good variety"
        elif variety_count == 2:
            return 1, "Moderate variety"
        else:
            return 0, "Poor variety"
    
    def check_common_patterns(self, password):
        """Check for common patterns"""
        password_lower = password.lower()
        
        # Check for common passwords
        if password_lower in self.common_passwords:
            return 0, "Common password detected"
        
        # Check for sequential patterns
        for pattern in self.common_patterns:
            if pattern in password_lower:
                return 0, f"Common pattern detected: {pattern}"
        
        return 3, "No common patterns detected"
    
    def check_repetition(self, password):
        """Check for repeated characters"""
        # Check for 3 or more repeated characters
        if re.search(r'(.)\1{2,}', password):
            return 0, "Repeated characters detected"
        
        # Check for too many of the same character
        char_counts = Counter(password)
        max_count = max(char_counts.values())
        if max_count > len(password) / 3:
            return 1, "Character repetition detected"
        
        return 3, "No repetition issues"
    
    def calculate_entropy(self, password):
        """Calculate password entropy (bits)"""
        charset_size = 0
        
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'\d', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            charset_size += 32
        
        if charset_size == 0:
            return 0
        
        entropy = len(password) * math.log2(charset_size)
        return entropy
    
    def estimate_crack_time(self, entropy):
        """Estimate time to crack password (assuming 1 billion guesses/second)"""
        guesses = 2 ** entropy
        seconds = guesses / 1_000_000_000
        
        if seconds < 1:
            return "Less than 1 second"
        elif seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.2f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.2f} hours"
        elif seconds < 31536000:
            return f"{seconds/86400:.2f} days"
        else:
            years = seconds / 31536000
            if years > 1_000_000:
                return f"{years:.2e} years"
            return f"{years:.2f} years"
    
    def get_strength_level(self, score):
        """Convert score to strength level"""
        if score < 5:
            return "🔴 Weak"
        elif score < 10:
            return "🟡 Moderate"
        elif score < 15:
            return "🟢 Strong"
        else:
            return "🔵 Very Strong"
    
    def analyze_password(self, password):
        """Comprehensive password analysis"""
        if not password:
            return {"error": "Password cannot be empty"}
        
        results = {}
        total_score = 0
        feedback = []
        
        # Run all checks
        length_score, length_msg = self.check_length(password)
        total_score += length_score
        feedback.append(f"Length: {length_msg}")
        
        variety_score, variety_msg = self.check_character_variety(password)
        total_score += variety_score
        feedback.append(f"Variety: {variety_msg}")
        
        pattern_score, pattern_msg = self.check_common_patterns(password)
        total_score += pattern_score
        feedback.append(f"Patterns: {pattern_msg}")
        
        repetition_score, repetition_msg = self.check_repetition(password)
        total_score += repetition_score
        feedback.append(f"Repetition: {repetition_msg}")
        
        # Calculate entropy
        entropy = self.calculate_entropy(password)
        crack_time = self.estimate_crack_time(entropy)
        
        # Get overall strength
        strength = self.get_strength_level(total_score)
        
        results = {
            "password_length": len(password),
            "strength": strength,
            "score": total_score,
            "max_score": 12,
            "entropy_bits": round(entropy, 2),
            "estimated_crack_time": crack_time,
            "feedback": feedback
        }
        
        return results


# Example usage
if __name__ == "__main__":
    checker = PasswordStrengthChecker()
    
    # Test passwords
    test_passwords = [
        "password",
        "Pass123!",
        "MySecureP@ssw0rd2024",
        "kR9$mP2#vL5@nX8&tQ4"
    ]
    
    print("=" * 60)
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    
    for pwd in test_passwords:
        print(f"\nTesting: {pwd}")
        print("-" * 60)
        result = checker.analyze_password(pwd)
        
        print(f"Strength: {result['strength']}")
        print(f"Score: {result['score']}/{result['max_score']}")
        print(f"Entropy: {result['entropy_bits']} bits")
        print(f"Estimated crack time: {result['estimated_crack_time']}")
        print("\nFeedback:")
        for item in result['feedback']:
            print(f"  • {item}")