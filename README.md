# Jessica Margetich - Professional Portfolio

A modern, SEO-optimized portfolio website built with FastAPI showcasing Jessica's expertise as a Technical Product Leader.

## About

This portfolio highlights Jessica's 10+ years of experience embedding data and technology into product strategy, leading global teams, and delivering innovative solutions at scale across D2C and B2B2C enterprises.

## Key Features

- **Static FastAPI Architecture**: Fast, SEO-friendly server-side rendering
- **Responsive Design**: Mobile-first design optimized for all devices
- **SEO Optimized**: Structured data, meta tags, and performance optimization
- **Professional Content**: Leadership experience, technical projects, and achievements
- **Contact Integration**: Professional contact forms and social media links

## Technology Stack

- **Backend**: FastAPI with Jinja2 templating
- **Frontend**: Semantic HTML5, CSS3, Vanilla JavaScript
- **Data**: YAML-based content management
- **Deployment**: Ready for Railway, Render, or Vercel
- **Domain**: Configured for jambuilds.com

## Quick Start

1. **Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run Development Server**:
   ```bash
   python app.py
   ```

3. **Visit**: http://localhost:8000

## Project Structure

```
jambuilds-portfolio/
├── app.py                 # FastAPI application
├── requirements.txt       # Python dependencies
├── data/
│   ├── config.yaml       # Site configuration
│   ├── leadership.yaml   # Leadership experience data
│   └── projects.yaml     # Technical projects data
├── templates/
│   ├── base.html         # Base template with SEO
│   ├── home.html         # Homepage
│   ├── about.html        # About page
│   ├── leadership.html   # Leadership experience
│   ├── projects.html     # Technical projects
│   ├── blog.html         # Blog/LinkedIn integration
│   ├── interests.html    # Interests & motivation
│   └── contact.html      # Contact page
└── static/
    ├── css/style.css     # Main stylesheet
    ├── js/script.js      # JavaScript functionality
    └── images/           # Images and assets
```

## Content Management

Content is managed through YAML files in the `/data` directory:

- `config.yaml`: Site settings, meta tags, and navigation
- `leadership.yaml`: Leadership experience and achievements
- `projects.yaml`: Technical projects and outcomes
- `interests.yaml`: Personal interests, motivations, and values

## SEO Features

- Structured data (JSON-LD) for professional profiles
- Dynamic meta tags per page
- XML sitemap generation (`/sitemap.xml`)
- Robots.txt (`/robots.txt`)
- Open Graph and Twitter Card support
- Performance optimized CSS and JavaScript

## Deployment

### Railway/Render
1. Connect repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`
4. Configure custom domain: jambuilds.com

### Environment Variables
- `PORT`: Server port (default: 8000)
- `ENV`: Environment (development/production)

## LinkedIn Integration

The blog section is prepared for LinkedIn post integration. To enable:

1. Set up LinkedIn API access
2. Update the blog template with API calls
3. Configure authentication credentials

## Analytics & SEO

Ready for:
- Google Analytics 4
- Google Search Console
- Core Web Vitals monitoring
- Performance tracking

## Professional Highlights

- **$44M P&L responsibility** at sticky.io
- **14% YoY revenue growth** through strategic initiatives
- **1.6M employees** reached through VR training innovation
- **Global team leadership** across US, Europe, Africa, and Asia
- **AI/ML product expertise** in payment optimization and delivery
- **Executive MBA** from INSEAD with AI specialization

## Contact Information

- **Email**: jessica.a.margetich@gmail.com
- **Phone**: +1 415 515 0844
- **LinkedIn**: [linkedin.com/in/jessica-margetich](https://linkedin.com/in/jessica-margetich)

---

Built with FastAPI, deployed on jambuilds.com