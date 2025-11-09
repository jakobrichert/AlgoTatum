# AlgoTatum - Algorand NFT Marketplace

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django 4.0](https://img.shields.io/badge/django-4.0-green.svg)](https://www.djangoproject.com/)
[![Algorand](https://img.shields.io/badge/blockchain-Algorand-black.svg)](https://www.algorand.com/)

A decentralized NFT marketplace built on the Algorand blockchain, leveraging the Tatum API for seamless blockchain interactions. This project was developed as part of the [Algorand Foundation Gitcoin Bounty](https://gitcoin.co/issue/algorandfoundation/grow-algorand/121/100027179).

## 🎯 Project Overview

AlgoTatum is a proof-of-concept NFT marketplace that demonstrates the integration of Algorand blockchain technology with modern web development practices. The platform enables users to:

- **Create Algorand wallets** automatically upon registration
- **Browse NFT collections** in an intuitive marketplace interface
- **Authenticate securely** with Django's built-in authentication system
- **Interact with blockchain** through the Tatum API abstraction layer

## 🏗️ Architecture

### Technology Stack

**Backend:**
- **Django 4.0** - Python web framework
- **SQLite** - Development database (PostgreSQL recommended for production)
- **Tatum API** - Blockchain interaction layer

**Frontend:**
- **HTML5/CSS3** - Modern responsive design
- **Bootstrap 5** - UI framework
- **Owl Carousel** - Interactive carousels
- **Custom JavaScript** - Dynamic interactions

**Blockchain:**
- **Algorand** - Layer-1 blockchain platform
- **Tatum API** - Unified blockchain API

### Project Structure

```
AlgoTatum/
├── env/                          # Virtual environment
│   └── algorandtatum/           # Django project root
│       ├── algorand/            # Main application
│       │   ├── migrations/      # Database migrations
│       │   ├── static/          # Static files (CSS, JS, images)
│       │   ├── templates/       # HTML templates
│       │   ├── admin.py         # Admin configuration
│       │   ├── forms.py         # Django forms
│       │   ├── models.py        # Database models
│       │   ├── tatum.py         # Tatum API integration
│       │   ├── urls.py          # URL routing
│       │   └── views.py         # View controllers
│       ├── algorandtatum/       # Project settings
│       │   ├── settings.py      # Django settings
│       │   ├── urls.py          # Root URL configuration
│       │   └── wsgi.py          # WSGI configuration
│       ├── db.sqlite3           # SQLite database
│       └── manage.py            # Django management script
├── .env.example                 # Environment variables template
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🚀 Features

### Implemented
- ✅ User registration and authentication
- ✅ Algorand wallet generation via Tatum API
- ✅ Responsive marketplace UI
- ✅ User profile management
- ✅ NFT browsing interface
- ✅ Secure session management

### Planned/In Progress
- 🔄 NFT minting functionality
- 🔄 NFT buy/sell transactions
- 🔄 Smart contract deployment
- 🔄 IPFS integration for NFT metadata
- 🔄 User wallet balance display
- 🔄 Transaction history
- 🔄 Enhanced security with Tatum KMS

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Tatum API key ([Get one here](https://tatum.io/))
- Git

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jakobrichert/AlgoTatum.git
cd AlgoTatum
```

### 2. Set Up Virtual Environment

```bash
# Activate the existing virtual environment
source env/bin/activate  # On Linux/Mac
# OR
env\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example env/algorandtatum/.env

# Edit the .env file and add your Tatum API key
# You can get a free API key at https://tatum.io/
```

### 5. Update Tatum API Configuration

Edit `env/algorandtatum/algorand/tatum.py` and ensure your API key is loaded from environment variables:

```python
import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

# Your API key will be loaded from .env file
api_key = env('TATUM_API_KEY')
```

### 6. Run Database Migrations

```bash
cd env/algorandtatum/
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000/` in your web browser to see the application.

## 🎮 Usage

### For Users

1. **Sign Up**: Create a new account at `/signup.html`
2. **Sign In**: Log in at `/signin.html`
3. **Generate Wallet**: Visit `/wallet.html` to create your Algorand wallet
4. **Explore NFTs**: Browse the marketplace at `/explores.html`

### For Developers

```bash
# Access Django admin panel
# Navigate to http://localhost:8000/admin
# Login with your superuser credentials

# Run tests (when implemented)
python manage.py test

# Create new migrations after model changes
python manage.py makemigrations
python manage.py migrate
```

## 🔒 Security Considerations

⚠️ **IMPORTANT**: This is a proof-of-concept and should NOT be used in production without significant security enhancements:

1. **API Keys**: Never commit API keys to version control
2. **Secret Keys**: Rotate Django secret key for production
3. **Wallet Storage**: Implement secure key management (consider Tatum KMS)
4. **HTTPS**: Use SSL/TLS in production
5. **Database**: Migrate to PostgreSQL for production
6. **Environment Variables**: Use proper secret management solutions
7. **Input Validation**: Add comprehensive input validation
8. **CSRF Protection**: Ensure CSRF tokens are properly implemented

## 📚 API Integration

This project uses the [Tatum API](https://tatum.io/) for blockchain interactions:

- **Wallet Generation**: Create Algorand wallets
- **Account Management**: Ledger account creation
- **IPFS Storage**: Store NFT metadata (planned)
- **Smart Contracts**: Deploy and interact with contracts (planned)

### Example API Calls

```python
# Generate Algorand wallet
wallet = generatewallet()
# Returns: {'address': '...', 'secret': '...'}

# Create ledger account
account = createaccount()

# Get IPFS data (planned)
data = getifps(id)
```

## 🐛 Known Issues

As documented in the original development:

1. **Backend Incomplete**: Core NFT transaction logic needs implementation
2. **User Model**: Needs wallet address and balance fields
3. **NFT Operations**: Buy/sell features require smart contract integration
4. **Key Storage**: API keys need secure storage solution
5. **Template Scaling**: Some templates need responsive design improvements
6. **Smart Contracts**: Tatum API integration for contract deployment needed

## 🤝 Contributing

Contributions are welcome! This project is a learning exercise and open for improvements.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📖 Learning Resources

This project integrates multiple technologies. Here are some resources to get started:

- [Algorand Developer Portal](https://developer.algorand.org/)
- [Tatum API Documentation](https://docs.tatum.io/)
- [Django Documentation](https://docs.djangoproject.com/)
- [NFT Standards](https://www.algorand.com/resources/algorand-announcements/algorand-nft-standards)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Jakob Richert**
- GitHub: [@jakobrichert](https://github.com/jakobrichert)
- Email: jakobquantum@tuta.io

## 🙏 Acknowledgments

- **Algorand Foundation** - For the Gitcoin bounty opportunity
- **Tatum** - For providing the blockchain API infrastructure
- **Django Community** - For the excellent web framework
- **Open Source Community** - For the various libraries and tools used

## 🔮 Future Roadmap

- [ ] Complete NFT minting functionality
- [ ] Implement smart contract deployment
- [ ] Add transaction signing and verification
- [ ] Integrate IPFS for decentralized storage
- [ ] Add comprehensive test coverage
- [ ] Implement real-time price tracking
- [ ] Create admin dashboard for NFT management
- [ ] Add support for multiple blockchain networks
- [ ] Implement advanced search and filtering
- [ ] Add user reputation and review system

---

**Note**: This project was created as part of a learning experience with blockchain technology and is not intended for production use without significant security and functionality enhancements. The code serves as a foundation for understanding Algorand NFT marketplace development.

## 📞 Support

If you have questions or need help:

1. Check the [Issues](https://github.com/jakobrichert/AlgoTatum/issues) page
2. Open a new issue if your question hasn't been answered
3. Reach out via email for general inquiries

**Happy Building! 🚀**
