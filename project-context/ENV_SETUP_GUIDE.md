# Environment Setup Guide: BigBounce Research Paper

## Overview

This guide provides step-by-step instructions for setting up the BigBounce research paper project in your local development environment. The project is a static web application with minimal dependencies, making it easy to get started.

## Prerequisites

### Required Software
- **Node.js**: Version 16.0 or higher
- **Git**: Version 2.0 or higher
- **Web Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Text Editor**: VS Code, Sublime Text, or any code editor

### Optional Software
- **Image Editor**: For modifying scientific figures (GIMP, Photoshop, etc.)
- **Spreadsheet Software**: For editing data files (Excel, Google Sheets, etc.)
- **LaTeX Editor**: For mathematical content (if contributing to research)

## Installation Steps

### 1. Clone the Repository

```bash
# Clone the repository
git clone <repository-url>
cd bigbounce

# Verify the repository structure
ls -la
```

Expected output:
```
bigbounce/
├── index.html
├── bigbounce.md
├── paper/
├── public/
├── server.js
├── package.json
├── netlify.toml
└── CLAUDE.md
```

### 2. Install Dependencies

```bash
# Install Node.js dependencies
npm install

# Verify installation
npm list
```

Expected output:
```
bigbounce@1.0.0
└── express@5.1.0
```

### 3. Start Development Server

```bash
# Start the local development server
node server.js
```

Expected output:
```
Server running at http://localhost:3000
```

### 4. Access the Application

Open your web browser and navigate to:
```
http://localhost:3000
```

You should see the password protection screen. Enter the password: **houston**

## Environment Variables

### Development Environment

The project uses minimal environment variables. No `.env` file is required for basic development.

#### Optional Environment Variables

If you need to customize the development environment:

```bash
# Create a .env file (optional)
touch .env

# Add custom port (optional)
echo "PORT=3001" >> .env
```

#### Environment Variable Reference

| Variable | Default | Description | Required |
|----------|---------|-------------|----------|
| `PORT` | 3000 | Development server port | No |
| `NODE_ENV` | development | Node.js environment | No |

### Production Environment

No environment variables are required for production deployment on Netlify.

## Platform-Specific Setup

### macOS Setup

#### Install Prerequisites
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js
brew install node

# Install Git
brew install git

# Verify installations
node --version
npm --version
git --version
```

#### Development Workflow
```bash
# Clone repository
git clone <repository-url>
cd bigbounce

# Install dependencies
npm install

# Start development server
node server.js

# Open in browser
open http://localhost:3000
```

### Linux Setup

#### Ubuntu/Debian
```bash
# Update package manager
sudo apt update

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Git
sudo apt install git

# Verify installations
node --version
npm --version
git --version
```

#### CentOS/RHEL
```bash
# Install Node.js
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo yum install -y nodejs

# Install Git
sudo yum install git

# Verify installations
node --version
npm --version
git --version
```

### Windows Setup

#### Using Chocolatey
```bash
# Install Chocolatey (run as Administrator)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Node.js
choco install nodejs

# Install Git
choco install git

# Verify installations
node --version
npm --version
git --version
```

#### Using WSL (Windows Subsystem for Linux)
```bash
# Install WSL (run in PowerShell as Administrator)
wsl --install

# Follow Ubuntu setup instructions above
```

## Development Workflow

### 1. Content Development

#### Editing Research Paper
```bash
# Edit individual sections
code paper/01-introduction.md
code paper/02-theoretical-framework.md

# Edit complete paper
code bigbounce.md
```

#### Adding Images
```bash
# Add new scientific figures
cp /path/to/new/figure.png public/images/

# Update HTML to reference new image
code index.html
```

#### Updating Data
```bash
# Edit spreadsheet data
open public/spreadsheets/figure_1_lqg_holst_complete_data.xlsx

# Update references in paper
code paper/02-theoretical-framework.md
```

### 2. Web Interface Development

#### HTML/CSS/JavaScript
```bash
# Edit main interface
code index.html

# Test changes in browser
# Refresh http://localhost:3000
```

#### MathJax Configuration
```bash
# MathJax settings are in index.html
# Look for the MathJax configuration section
code index.html
```

### 3. Testing and Validation

#### Cross-Browser Testing
```bash
# Test in different browsers
open -a "Google Chrome" http://localhost:3000
open -a "Firefox" http://localhost:3000
open -a "Safari" http://localhost:3000
```

#### Mobile Testing
```bash
# Use browser developer tools for mobile testing
# Chrome: F12 → Device toolbar
# Firefox: F12 → Responsive design mode
```

#### Performance Testing
```bash
# Use browser developer tools
# Chrome: F12 → Performance tab
# Lighthouse: Generate performance report
```

## Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Error: EADDRINUSE: address already in use :::3000

# Solution 1: Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Solution 2: Use different port
PORT=3001 node server.js
```

#### Node.js Version Issues
```bash
# Check Node.js version
node --version

# If version < 16, update Node.js
# macOS: brew upgrade node
# Linux: Use nvm or package manager
# Windows: Download from nodejs.org
```

#### MathJax Loading Issues
```bash
# Check browser console for errors
# Verify internet connection (MathJax loads from CDN)
# Check MathJax configuration in index.html
```

#### Image Loading Issues
```bash
# Verify image paths in HTML
# Check file permissions
# Ensure images are in public/images/ directory
```

### Debug Mode

#### Enable Debug Logging
```bash
# Add debug logging to server.js
DEBUG=* node server.js
```

#### Browser Developer Tools
```bash
# Open developer tools
# Chrome/Edge: F12
# Firefox: F12
# Safari: Cmd+Option+I
```

## Deployment Setup

### Netlify Deployment

#### Automatic Deployment
```bash
# Push to Git repository
git add .
git commit -m "Update content"
git push origin main

# Netlify automatically deploys from Git
```

#### Manual Deployment
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy manually
netlify deploy --prod
```

### Local Production Testing
```bash
# Test production build locally
# Serve static files without development server
python3 -m http.server 8000
# or
npx serve .

# Access at http://localhost:8000
```

## Provider Setup

### Netlify Configuration

#### Automatic Setup
1. Connect GitHub repository to Netlify
2. Configure build settings:
   - Build command: (leave empty)
   - Publish directory: `.`
3. Deploy automatically

#### Manual Configuration
```toml
# netlify.toml configuration
[build]
  command = ""
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

### Custom Domain Setup

#### DNS Configuration
1. Add custom domain in Netlify dashboard
2. Configure DNS records:
   - A record: 75.2.60.5
   - CNAME record: your-site.netlify.app
3. Wait for DNS propagation (up to 24 hours)

#### SSL Certificate
- Netlify automatically provides SSL certificates
- No additional configuration required

## Security Considerations

### Development Security
```bash
# Never commit sensitive data
echo ".env" >> .gitignore
echo "node_modules/" >> .gitignore

# Use environment variables for sensitive data
# (Not applicable for this static site)
```

### Production Security
- Security headers configured in `netlify.toml`
- No server-side processing (reduces attack surface)
- Static content only (no database or API endpoints)

## Performance Optimization

### Development Performance
```bash
# Monitor file sizes
du -sh public/images/
du -sh public/spreadsheets/

# Optimize images before adding
# Use tools like ImageOptim or TinyPNG
```

### Production Performance
- CDN distribution via Netlify
- Automatic asset optimization
- Caching policies configured

## Maintenance

### Regular Updates
```bash
# Update dependencies
npm update

# Check for security vulnerabilities
npm audit

# Update Node.js (when needed)
# Follow platform-specific instructions
```

### Backup Strategy
```bash
# Create backup of repository
git clone <repository-url> bigbounce-backup

# Backup data files
cp -r public/spreadsheets/ ~/backups/
cp -r public/images/ ~/backups/
```

## How to Keep This File Fresh

- **Monthly Reviews**: Update based on new dependencies or tools
- **Platform Updates**: Update when Node.js or other tools change
- **Security Updates**: Update security recommendations
- **User Feedback**: Incorporate setup issues and solutions
- **New Features**: Update when new development features are added

