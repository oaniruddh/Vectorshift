VectorShift HubSpot Integration
📋 Technical Assessment Submission
This repository contains my complete implementation of the VectorShift Integrations Technical Assessment, featuring a full-stack HubSpot OAuth integration with React frontend and FastAPI backend.

🎯 Assessment Overview
Completed Tasks:

✅ Part 1: HubSpot OAuth 2.0 integration (backend + frontend)

✅ Part 2: HubSpot CRM data loading with IntegrationItem mapping

✅ Bonus: Production-ready code with error handling and security features

Tech Stack:

Backend: Python, FastAPI, Redis

Frontend: JavaScript, React

Integration: HubSpot CRM API, OAuth 2.0

🚀 Features Implemented
Backend Implementation (/backend/integrations/hubspot.py)
OAuth Flow:

python
def authorize_hubspot():
    """Initiates HubSpot OAuth 2.0 authorization flow"""
    # Generates secure state parameter
    # Redirects to HubSpot with proper scopes
    
def oauth2callback_hubspot():
    """Handles OAuth callback and token exchange"""
    # Exchanges auth code for access/refresh tokens
    # Encrypts and stores credentials in Redis
    
def get_hubspot_credentials():
    """Retrieves and decrypts stored credentials"""
    # Handles token refresh automatically
    # Returns valid access tokens
Data Loading:

python
def get_items_hubspot():
    """Loads HubSpot CRM data as IntegrationItems"""
    # Fetches contacts, companies, deals
    # Maps to standardized IntegrationItem format
    # Handles pagination and rate limiting
Frontend Implementation (/frontend/src/integrations/hubspot.js)
Integration Module:

OAuth flow initiation and callback handling

Connection status management

Error handling with user-friendly messages

Seamless integration with existing VectorShift UI

🛠️ Setup & Running
Prerequisites
Python 3.8+

Node.js 16+

Redis server

HubSpot Developer Account

Quick Start
Backend:

bash
cd /backend
pip install -r requirements.txt
redis-server  # In separate terminal
uvicorn main:app --reload
Frontend:

bash
cd /frontend
npm install
npm run start
Environment Configuration
Required Environment Variables:

text
HUBSPOT_CLIENT_ID=your_hubspot_client_id
HUBSPOT_CLIENT_SECRET=your_hubspot_client_secret
HUBSPOT_REDIRECT_URI=http://localhost:8000/integrations/hubspot/oauth2callback
REDIS_URL=redis://localhost:6379
HubSpot App Setup:

Create app in HubSpot Developer Portal

Configure redirect URI: http://localhost:8000/integrations/hubspot/oauth2callback

Required scopes: crm.objects.contacts.read, crm.objects.companies.read, crm.objects.deals.read

🏗️ Architecture
Code Structure
text
/backend/integrations/hubspot.py
├── authorize_hubspot()          # OAuth initiation
├── oauth2callback_hubspot()     # Token exchange
├── get_hubspot_credentials()    # Credential management
└── get_items_hubspot()         # Data loading

/frontend/src/integrations/hubspot.js
├── OAuth flow handlers
├── UI components
└── API integration
Integration Patterns
Following established VectorShift conventions from airtable.py and notion.py:

Consistent API endpoint structure

Standardized error handling

Unified IntegrationItem data format

Shared React component patterns

🔐 Security Features
Token Encryption: All OAuth tokens encrypted before Redis storage

CSRF Protection: State parameter validation in OAuth flow

Input Validation: Pydantic models for request validation

Secure Headers: Proper security headers in API responses

📊 API Endpoints
Authentication
GET /integrations/hubspot/authorize - Start OAuth flow

GET /integrations/hubspot/oauth2callback - Handle callback

GET /integrations/hubspot/credentials - Get connection status

Data Access
GET /integrations/hubspot/items - Load HubSpot CRM data

🧪 Testing
Manual Testing Flow
Start both backend and frontend servers

Navigate to integrations page

Click "Connect HubSpot"

Complete OAuth authorization

Verify data loading functionality

API Testing
bash
# Test OAuth initiation
curl "http://localhost:8000/integrations/hubspot/authorize"

# Test data loading (after OAuth)
curl "http://localhost:8000/integrations/hubspot/items"
⚡ Performance & Error Handling
Rate Limiting:

Automatic retry with exponential backoff

Respects HubSpot API limits (100 requests/10 seconds)

Token Management:

Automatic access token refresh

Graceful handling of expired tokens

Error Recovery:

Network timeout handling

OAuth flow error management

User-friendly error messages

📈 Implementation Highlights
Key Technical Decisions
Security First: Implemented proper OAuth 2.0 flow with CSRF protection

Consistency: Followed existing integration patterns for maintainability

Scalability: Designed for easy extension to additional HubSpot objects

Reliability: Comprehensive error handling and recovery mechanisms

Code Quality Features
Clean Architecture: Separation of concerns between auth and data layers

Type Safety: Pydantic models for data validation

Documentation: Comprehensive inline documentation

Testing Ready: Structured for easy unit and integration testing

🔮 Future Enhancements
Potential Extensions:

Webhook integration for real-time updates

Support for HubSpot custom objects

Bulk data synchronization capabilities

Multi-portal support

Enhanced caching strategies

📝 Submission Notes
This implementation demonstrates:

Full-stack development with modern Python and JavaScript

API integration following OAuth 2.0 best practices

Code quality with security and error handling

Pattern consistency with existing VectorShift architecture

Production readiness with proper configuration management



🤝 Contact
Developer: Aniruddh Ojha, Email: aniruddhojha705@gmail.com


For questions about this implementation or VectorShift opportunities:

Technical questions: Feel free to reach out via GitHub issues

VectorShift recruiting: recruiting@vectorshift.ai

Implemented with attention to security, scalability, and maintainability. Ready for production deployment.

⭐ Acknowledgments
Thank you to the VectorShift team for the opportunity to work on this technical assessment. The existing codebase patterns made integration straightforward and enjoyable to implement.
