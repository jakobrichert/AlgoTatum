# AlgoTatum Architecture Documentation

## 🏗️ System Architecture Overview

AlgoTatum is a Django-based web application that serves as an NFT marketplace on the Algorand blockchain. The system follows a traditional MVC (Model-View-Controller) pattern with Django's MTV (Model-Template-View) variant.

## 📊 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│                    (HTML/CSS/JavaScript)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Django Application                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐ │
│  │   Views      │◄─┤   URLs       │  │   Authentication     │ │
│  │  (Logic)     │  │  (Routing)   │  │   (Django Auth)      │ │
│  └──────┬───────┘  └──────────────┘  └──────────────────────┘ │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐ │
│  │   Models     │  │   Forms      │  │   Templates          │ │
│  │  (Database)  │  │  (Input)     │  │   (UI Rendering)     │ │
│  └──────┬───────┘  └──────────────┘  └──────────────────────┘ │
│         │                                                        │
└─────────┼────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Database (SQLite)                             │
│                  (User Data, Sessions)                           │
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Tatum API Integration                         │
│              (Blockchain Abstraction Layer)                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Algorand Blockchain                           │
│              (Wallets, Transactions, NFTs)                       │
└─────────────────────────────────────────────────────────────────┘
```

## 🔧 Component Details

### 1. Frontend Layer

**Technology**: HTML5, CSS3, JavaScript, Bootstrap 5

**Components**:
- `templates/algorand/index.html` - Landing page
- `templates/algorand/explores.html` - NFT marketplace browsing
- `templates/algorand/wallet.html` - Wallet management
- `templates/algorand/signin.html` - User authentication
- `templates/algorand/signup.html` - User registration
- `templates/algorand/item-details.html` - NFT detail view
- `templates/algorand/live.html` - Live auctions (planned)

**Static Assets**:
- CSS: Bootstrap, custom styles, animations
- JavaScript: Owl Carousel, custom interactions
- Images: Logos, placeholders, UI elements

### 2. Backend Layer

**Technology**: Django 4.0, Python 3.8+

#### Views (`views.py`)

Handles HTTP requests and business logic:

```python
index(request)           # Landing page
explore(request)         # NFT browsing (auth required)
wallet(request)          # Wallet generation & display (auth required)
signin(request)          # User login
signup(request)          # User registration
itemdetails(request)     # NFT details
live(request)            # Live auctions
```

**Authentication Flow**:
1. User submits credentials via form
2. Django validates against database
3. Session created on success
4. User redirected to authenticated pages

#### Models (`models.py`)

**Current Status**: Minimal implementation (empty file)

**Planned Models**:
```python
class NFT(models.Model):
    """Represents an NFT on the marketplace"""
    token_id = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=6)
    image_url = models.URLField()
    metadata_url = models.URLField()  # IPFS link
    created_at = models.DateTimeField(auto_now_add=True)

class Wallet(models.Model):
    """User's Algorand wallet"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, unique=True)
    # Note: Never store private keys in database!
    balance = models.DecimalField(max_digits=20, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    """Blockchain transaction record"""
    transaction_id = models.CharField(max_length=255, unique=True)
    from_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    nft = models.ForeignKey(NFT, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### Forms (`forms.py`)

**NewUserForm**: Custom user registration form
- Extends Django's `UserCreationForm`
- Adds email validation
- Creates user accounts

#### URL Routing (`urls.py`)

Maps URLs to views:
```
/                    → index
/signin.html         → signin
/signup.html         → signup
/wallet.html         → wallet
/explores.html       → explore
/item-details.html   → itemdetails
/live.html           → live
```

### 3. Blockchain Integration Layer

**Technology**: Tatum API, HTTP Client

**File**: `tatum.py`

#### Current Functions

1. **generatewallet()**
   - Endpoint: `/v3/algorand/wallet`
   - Returns: `{'address': '...', 'secret': '...'}`
   - Purpose: Create new Algorand wallet

2. **createaccount()**
   - Endpoint: `/v3/ledger/account`
   - Purpose: Create ledger account for tracking
   - Status: Partially implemented

3. **getipfs()**
   - Endpoint: `/v3/ipfs/{id}`
   - Purpose: Retrieve NFT metadata from IPFS
   - Status: Skeleton only

#### Planned Functions

```python
def mint_nft(name, description, image_url, owner_address):
    """Mint a new NFT on Algorand blockchain"""
    pass

def transfer_nft(nft_id, from_address, to_address, private_key):
    """Transfer NFT ownership"""
    pass

def get_nft_details(nft_id):
    """Get NFT metadata and ownership info"""
    pass

def get_wallet_balance(address):
    """Check Algorand wallet balance"""
    pass

def deploy_smart_contract(contract_code):
    """Deploy NFT marketplace smart contract"""
    pass
```

### 4. Database Layer

**Technology**: SQLite (development), PostgreSQL (recommended for production)

**Current Schema**:
- Django's built-in User model
- Session management tables
- Migration history

**Planned Schema**:
- NFT records
- Wallet associations
- Transaction history
- User profiles with wallet info

### 5. External Services

#### Tatum API

**Purpose**: Blockchain abstraction layer

**Endpoints Used**:
- Wallet generation
- Account management
- IPFS storage (planned)
- Transaction signing (planned)

**Configuration**:
- API Key: Stored in `.env` file
- Region: EU (api-eu1.tatum.io)
- Protocol: HTTPS

#### Algorand Blockchain

**Purpose**: Decentralized ledger for NFTs

**Features Used**:
- Wallet creation
- Asset (NFT) management
- Transaction processing
- Smart contracts (planned)

## 🔐 Security Architecture

### Current Implementation

1. **Django Security Features**:
   - CSRF protection on forms
   - Password hashing (PBKDF2)
   - Session management
   - SQL injection prevention (ORM)

2. **API Key Management**:
   - Stored in environment variables
   - Not committed to version control

### Security Concerns (To Address)

1. **Private Key Storage**:
   - Currently displayed to user in wallet view
   - **Risk**: Keys could be logged or stored insecurely
   - **Solution**: Implement Tatum KMS or client-side key management

2. **Secret Key Exposure**:
   - Django SECRET_KEY hardcoded in settings.py
   - **Solution**: Move to environment variables

3. **HTTPS**:
   - Not configured for development
   - **Required for production**

4. **Input Validation**:
   - Minimal validation on forms
   - **Solution**: Add comprehensive validators

## 🔄 Data Flow Examples

### User Registration Flow

```
1. User fills signup form
   └─► POST /signup.html
       └─► NewUserForm.is_valid()
           ├─► Valid: Create user in database
           │   └─► login(request, user)
           │       └─► Redirect to index
           └─► Invalid: Show errors
```

### Wallet Generation Flow

```
1. User navigates to /wallet.html
   └─► Check authentication
       ├─► Not authenticated: Redirect to signin
       └─► Authenticated:
           └─► generatewallet() [Tatum API call]
               ├─► API Request: GET /v3/algorand/wallet
               │   └─► Headers: x-api-key
               └─► API Response: {address, secret}
                   └─► Render wallet.html with data
                       └─► Display address & private key
```

### NFT Purchase Flow (Planned)

```
1. User clicks "Buy" on NFT
   └─► POST /buy/{nft_id}
       └─► Verify user has wallet
           └─► Check balance (Tatum API)
               ├─► Insufficient: Show error
               └─► Sufficient:
                   └─► Create transaction (Tatum API)
                       └─► Sign with user's key
                           └─► Submit to Algorand
                               ├─► Success: Update ownership
                               │   └─► Record in database
                               └─► Failure: Rollback
```

## 📈 Scalability Considerations

### Current Limitations

1. **Database**: SQLite not suitable for production
2. **Static Files**: Served by Django (inefficient)
3. **No Caching**: Every request hits database
4. **Synchronous**: No async processing
5. **Single Server**: No load balancing

### Recommended Improvements

1. **Database**:
   - Migrate to PostgreSQL
   - Add database indexing
   - Implement connection pooling

2. **Caching**:
   - Redis for session storage
   - Cache NFT listings
   - Cache user wallets

3. **Static Files**:
   - Use CDN (CloudFront, Cloudflare)
   - Implement asset compression
   - Add cache headers

4. **Background Tasks**:
   - Celery for async operations
   - Queue blockchain transactions
   - Process IPFS uploads

5. **Infrastructure**:
   - Container orchestration (Docker, Kubernetes)
   - Load balancing (Nginx)
   - Auto-scaling

## 🧪 Testing Strategy

### Current State
- No automated tests implemented

### Recommended Testing Approach

1. **Unit Tests**:
   - Test Tatum API integration
   - Test form validation
   - Test model methods

2. **Integration Tests**:
   - Test user registration flow
   - Test wallet generation
   - Test authentication

3. **E2E Tests**:
   - Selenium for UI testing
   - Test complete user journeys

## 🔮 Future Architecture Enhancements

### Phase 1: Core Functionality
- Complete NFT minting
- Implement buy/sell transactions
- Add IPFS integration
- Deploy smart contracts

### Phase 2: User Experience
- Real-time updates (WebSockets)
- Notification system
- Search and filtering
- User profiles and collections

### Phase 3: Advanced Features
- Auction system
- Royalty management
- Multi-chain support
- Analytics dashboard

### Phase 4: Enterprise
- API for third-party integrations
- Microservices architecture
- Enhanced security (multi-sig wallets)
- Compliance and KYC

## 📚 Technology Decisions

### Why Django?
- Rapid development
- Built-in admin panel
- Strong ORM
- Excellent documentation
- Security features out of the box

### Why Tatum API?
- Simplifies blockchain complexity
- Multi-chain support
- Good documentation
- Handles infrastructure
- Fast time-to-market

### Why Algorand?
- Fast transactions (4.5s finality)
- Low fees
- Carbon negative
- Native NFT support (ASA)
- Growing ecosystem

### Why SQLite (Dev)?
- Zero configuration
- File-based (easy backup)
- Perfect for development
- Fast for small datasets

## 🔗 Related Documentation

- [README.md](README.md) - Project overview and setup
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [Algorand Docs](https://developer.algorand.org/)
- [Tatum Docs](https://docs.tatum.io/)
- [Django Docs](https://docs.djangoproject.com/)

---

**Last Updated**: November 2025
**Maintainer**: Jakob Richert
