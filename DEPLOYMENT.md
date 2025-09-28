# jambuilds.com Deployment Guide

## Pre-Deployment Checklist
- [x] FastAPI application built
- [x] All templates and content finalized
- [x] jambuilds.com domain owned
- [ ] Local testing completed
- [ ] Git repository initialized

## Vercel Deployment Steps

### 1. GitHub Setup
```bash
# Initialize Git repository
git init
git add .
git commit -m "Initial portfolio site"

# Create GitHub repository (via GitHub CLI or web interface)
gh repo create jambuilds-portfolio --public
git remote add origin https://github.com/[username]/jambuilds-portfolio.git
git push -u origin main
```

### 2. Vercel Account Setup
1. Sign up at vercel.com (use GitHub login)
2. Connect GitHub account
3. Import jambuilds-portfolio repository

### 3. Vercel Configuration
```
Build Command: pip install -r requirements.txt
Output Directory: (default)
Install Command: pip install -r requirements.txt
Development Command: uvicorn app:app --host 0.0.0.0 --port 3000
```

### 4. Domain Configuration
1. Vercel Dashboard → Project Settings → Domains
2. Add Domain: jambuilds.com
3. Follow DNS configuration instructions
4. Add www.jambuilds.com → redirect to jambuilds.com

### 5. Required Files to Create
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel configuration
- Runtime configuration for FastAPI

## DNS Settings (for jambuilds.com)
Update your domain registrar with Vercel's nameservers:
- ns1.vercel-dns.com
- ns2.vercel-dns.com

## Post-Deployment
- [ ] SSL certificate active
- [ ] All pages loading correctly
- [ ] Contact form functional
- [ ] Performance testing
- [ ] SEO validation

## Phase 7: Scaling Features
- Google Analytics integration
- Search Console setup
- Performance monitoring
- A/B testing implementation