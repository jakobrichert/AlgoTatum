# Contributing to AlgoTatum

First off, thank you for considering contributing to AlgoTatum! This project was created as a learning experience in blockchain development, and contributions from the community help make it better for everyone.

## 🎯 Project Vision

AlgoTatum aims to be an educational resource for developers learning about:
- Algorand blockchain development
- NFT marketplace architecture
- Django web application development
- API integration patterns (specifically Tatum API)

## 📋 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Be patient with questions and different skill levels

## 🚀 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, Django version)

Example:
```markdown
**Bug**: Wallet generation fails with API error

**Steps to Reproduce**:
1. Navigate to /wallet.html
2. Click "Generate Wallet"
3. Error appears: "API connection failed"

**Expected**: Wallet should be generated successfully
**Actual**: Error message displayed

**Environment**:
- OS: Ubuntu 22.04
- Python: 3.10
- Django: 4.0
```

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear use case** - Why is this enhancement needed?
- **Expected behavior** - How should it work?
- **Alternative solutions** - Any other approaches you considered?

### Pull Requests

#### Before You Start

1. Check if there's already an issue for what you want to work on
2. If not, create an issue to discuss the change
3. Wait for feedback before investing significant time

#### Development Process

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AlgoTatum.git
   cd AlgoTatum
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # OR
   git checkout -b fix/your-bug-fix
   ```

3. **Set up development environment**
   ```bash
   source env/bin/activate
   cd env/algorandtatum
   python manage.py migrate
   ```

4. **Make your changes**
   - Write clear, commented code
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation as needed

5. **Test your changes**
   ```bash
   python manage.py test
   python manage.py runserver
   # Manually test the functionality
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template

#### Pull Request Guidelines

- **Title**: Clear and descriptive
- **Description**: Explain what and why, not just how
- **Link issues**: Use "Fixes #123" or "Closes #123"
- **Screenshots**: Add if UI changes are involved
- **Testing**: Describe how you tested the changes

Example PR description:
```markdown
## Description
Implements NFT minting functionality using Tatum API

## Related Issue
Fixes #42

## Changes Made
- Added `mint_nft()` function in tatum.py
- Created NFT model in models.py
- Added minting view and template
- Updated user model to track owned NFTs

## Testing
- Tested wallet generation
- Successfully minted test NFT
- Verified NFT appears in user profile

## Screenshots
[Add screenshots here]
```

## 🔧 Development Guidelines

### Code Style

**Python (PEP 8)**
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use descriptive variable names
- Add docstrings to functions

```python
def generate_algorand_wallet(user_id):
    """
    Generate a new Algorand wallet for a user via Tatum API.

    Args:
        user_id (int): The ID of the user requesting the wallet

    Returns:
        dict: Wallet information with 'address' and 'secret' keys

    Raises:
        TatumAPIError: If the API request fails
    """
    # Implementation here
    pass
```

**JavaScript**
- Use ES6+ features
- Use camelCase for variables
- Add comments for complex logic

**HTML/CSS**
- Use semantic HTML5 elements
- Follow BEM naming for CSS classes
- Keep templates DRY (Don't Repeat Yourself)

### Django Best Practices

1. **Models**
   - Use descriptive model names
   - Add helpful `__str__` methods
   - Include validators where appropriate

2. **Views**
   - Keep views thin, move logic to models/services
   - Use class-based views for CRUD operations
   - Add proper error handling

3. **Templates**
   - Extend base templates
   - Use template tags for reusable components
   - Escape user input properly

4. **Security**
   - Never commit secrets or API keys
   - Use Django's CSRF protection
   - Validate and sanitize all input
   - Use parameterized queries

### Tatum API Integration

When adding new Tatum API endpoints:

```python
def new_tatum_function():
    """
    Brief description of what this function does.

    Tatum API Endpoint: /v3/endpoint/path
    Documentation: https://docs.tatum.io/...
    """
    conn = http.client.HTTPSConnection("api-eu1.tatum.io")
    headers = {
        'x-api-key': env('TATUM_API_KEY'),
        'content-type': 'application/json'
    }

    try:
        # API call implementation
        pass
    except Exception as e:
        # Proper error handling
        logger.error(f"Tatum API error: {e}")
        raise
```

## 📝 Documentation

- Update README.md if you change functionality
- Add docstrings to new functions
- Update ARCHITECTURE.md for architectural changes
- Include code comments for complex logic

## 🧪 Testing

### Manual Testing Checklist

Before submitting a PR, test:

- [ ] User registration works
- [ ] User login/logout works
- [ ] Wallet generation functions
- [ ] No console errors in browser
- [ ] Responsive design on mobile
- [ ] No broken links
- [ ] Database migrations apply cleanly

### Automated Tests (Future)

We encourage adding tests:

```python
# tests.py
from django.test import TestCase
from .models import User
from .tatum import generatewallet

class WalletTestCase(TestCase):
    def test_wallet_generation(self):
        """Test that wallet generation returns valid data"""
        wallet = generatewallet()
        self.assertIn('address', wallet)
        self.assertIn('secret', wallet)
```

## 🎓 Learning Resources

New to these technologies? Here are some great resources:

### Algorand & Blockchain
- [Algorand Developer Docs](https://developer.algorand.org/)
- [Blockchain Basics](https://www.ibm.com/topics/what-is-blockchain)

### Django
- [Django Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)

### Tatum API
- [Tatum Documentation](https://docs.tatum.io/)
- [Tatum API Reference](https://tatum.io/apidoc)

### Git & GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)

## 📫 Communication

- **Questions**: Open an issue with the "question" label
- **Discussions**: Use GitHub Discussions (if enabled)
- **Security Issues**: Email jakobquantum@tuta.io directly

## 🏆 Recognition

Contributors will be recognized in:
- README.md acknowledgments section
- Release notes for significant contributions
- Project documentation

## 📜 License

By contributing to AlgoTatum, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions, whether big or small, make this project better for everyone. We appreciate your time and effort in improving AlgoTatum!

---

**Questions?** Don't hesitate to ask! Open an issue or reach out to the maintainers.

**Ready to contribute?** Pick an issue labeled "good first issue" and get started!
