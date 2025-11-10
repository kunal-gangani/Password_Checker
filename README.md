# 🔐 Password Strength Checker

A comprehensive cybersecurity project that evaluates password strength using industry-standard security criteria. This tool helps users create more secure passwords by providing real-time feedback and security analysis.

![Password Strength Demo](https://img.shields.io/badge/Security-Password_Checker-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow)
![License](https://img.shields.io/badge/License-MIT-red)

## 🎯 Features

- **Real-time Strength Analysis**: Instant feedback as passwords are typed
- **Multi-criteria Evaluation**: Checks length, variety, patterns, and repetition
- **Entropy Calculation**: Measures password randomness in bits
- **Crack Time Estimation**: Shows how long it would take to crack the password
- **Visual Feedback**: Color-coded strength meter (Weak, Moderate, Strong, Very Strong)
- **Both Python & Web Versions**: Use as a CLI tool or web application

## 🔍 Security Checks

### Basic Requirements
- ✅ Minimum length validation (8-16+ characters)
- ✅ Character variety (uppercase, lowercase, numbers, special characters)
- ✅ Common pattern detection (123, abc, qwerty)
- ✅ Dictionary word checking

### Advanced Features
- ✅ Entropy calculation for randomness measurement
- ✅ Repetition detection
- ✅ Time-to-crack estimation
- ✅ Score-based strength rating (0-12 scale)

## 🚀 Quick Start

### Python Version

**Requirements:**
- Python 3.7 or higher

## 🛠️ Technical Details
### Entropy Calculation
Entropy = Length × log2(CharacterSetSize)

Character set sizes:
- Lowercase: 26
- Uppercase: 26
- Numbers: 10
- Special characters: 32

### Crack Time Estimation
Based on 1 billion guesses per second using modern hardware.

## 🔮 Future Enhancements

- [ ] Integration with Have I Been Pwned API
- [ ] Password generation tool
- [ ] Multi-language support
- [ ] Browser extension
- [ ] Database breach checking
- [ ] Advanced dictionary attacks simulation

## 📚 Resources

- [OWASP Password Guidelines](https://owasp.org/www-community/controls/Password_Strength)
- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/)
- [Have I Been Pwned API](https://haveibeenpwned.com/API/v3)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This is an educational project. Never store or transmit passwords insecurely in production environments. Always use proper encryption and follow security best practices.

## 👤 Author

**Kunal Gangani**
- GitHub: [@kunal-gangani](https://github.com/kunal-gangani)
- Email: thekunalgangani@gmail.com

## ⭐ Show Your Support

Give a ⭐️ if this project helped you learn about password security!

---

**Made with ❤️ for better password security**
git clone https://github.com/kunal-gangani/Password_Checker

cd password-strength-checker
