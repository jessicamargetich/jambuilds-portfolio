from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import yaml
import os
from pathlib import Path

# Get the current directory
CURRENT_DIR = Path(__file__).parent
BASE_DIR = CURRENT_DIR.parent

app = FastAPI(
    title="jambuilds.com - Professional Portfolio",
    description="Personal portfolio website showcasing leadership and technical expertise",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Set up templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Data loading functions
def load_data(filename: str) -> dict:
    """Load YAML data file"""
    try:
        with open(BASE_DIR / "data" / filename, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}

def get_site_config() -> dict:
    """Get site configuration"""
    return load_data("config.yaml")

def get_projects() -> list:
    """Get portfolio projects"""
    data = load_data("projects.yaml")
    return data.get("projects", [])

def get_leadership() -> list:
    """Get leadership experiences"""
    data = load_data("leadership.yaml")
    return data.get("experiences", [])

def get_blog_posts() -> dict:
    """Get blog posts with filtering data"""
    return load_data("blog.yaml")

# SEO helper function
def get_page_meta(page: str, config: dict) -> dict:
    """Generate page-specific meta tags"""
    base_meta = {
        "title": config.get("site_name", "jambuilds.com"),
        "description": config.get("site_description", "Professional portfolio"),
        "keywords": config.get("keywords", ""),
        "author": config.get("author", ""),
        "url": config.get("base_url", "https://jambuilds.com")
    }

    page_meta = config.get("pages", {}).get(page, {})
    return {**base_meta, **page_meta}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    config = get_site_config()
    meta = get_page_meta("home", config)
    return templates.TemplateResponse("home.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    config = get_site_config()
    meta = get_page_meta("about", config)
    return templates.TemplateResponse("about.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/leadership", response_class=HTMLResponse)
async def leadership(request: Request):
    config = get_site_config()
    meta = get_page_meta("leadership", config)
    leadership_data = get_leadership()
    return templates.TemplateResponse("leadership.html", {
        "request": request,
        "meta": meta,
        "config": config,
        "experiences": leadership_data if isinstance(leadership_data, list) else leadership_data.get("experiences", []),
        "philosophy": leadership_data.get("philosophy", {}) if isinstance(leadership_data, dict) else {},
        "metrics": leadership_data.get("metrics", []) if isinstance(leadership_data, dict) else []
    })

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    config = get_site_config()
    meta = get_page_meta("projects", config)
    return templates.TemplateResponse("portfolio.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/portfolio/growth-engine", response_class=HTMLResponse)
async def growth_engine(request: Request):
    config = get_site_config()
    meta = get_page_meta("projects", config)
    meta["title"] = "Building the Next Growth Engine - Jessica Margetich"
    meta["description"] = "Creating a new business line and scaling it into a $700M+ growth engine at Walmart through GoLocal Delivery-as-a-Service"
    return templates.TemplateResponse("case-study-growth-engine.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/portfolio/trust-experience", response_class=HTMLResponse)
async def trust_experience(request: Request):
    config = get_site_config()
    meta = get_page_meta("projects", config)
    meta["title"] = "Earning Trust & Elevating Experience - Jessica Margetich"
    meta["description"] = "Transforming payment experiences through AI-powered optimization and customer-centric design"
    return templates.TemplateResponse("case-study-trust-experience.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/portfolio/failing-fast", response_class=HTMLResponse)
async def failing_fast(request: Request):
    config = get_site_config()
    meta = get_page_meta("projects", config)
    meta["title"] = "Failing Fast & Learning Faster - Jessica Margetich"
    meta["description"] = "Building an experimentation culture that turns failures into $650M revenue opportunities"
    return templates.TemplateResponse("case-study-failing-fast.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/portfolio/north-star", response_class=HTMLResponse)
async def north_star(request: Request):
    config = get_site_config()
    meta = get_page_meta("projects", config)
    meta["title"] = "Designing the North Star - Jessica Margetich"
    meta["description"] = "Creating shared vision and strategic alignment across global teams and stakeholders"
    return templates.TemplateResponse("case-study-north-star.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/portfolio/people-potential", response_class=HTMLResponse)
async def people_potential(request: Request):
    config = get_site_config()
    meta = get_page_meta("projects", config)
    meta["title"] = "Unlocking People Potential - Jessica Margetich"
    meta["description"] = "Scaling inclusive leadership and building talent pipelines that transform organizations"
    return templates.TemplateResponse("case-study-people-potential.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    config = get_site_config()
    meta = get_page_meta("blog", config)
    blog_data = get_blog_posts()
    return templates.TemplateResponse("blog.html", {
        "request": request,
        "meta": meta,
        "config": config,
        "posts": blog_data.get("posts", []),
        "filter_options": blog_data.get("filter_options", {})
    })

@app.get("/interests", response_class=HTMLResponse)
async def interests(request: Request):
    config = get_site_config()
    meta = get_page_meta("interests", config)
    interests_data = load_data("interests.yaml")
    return templates.TemplateResponse("interests.html", {
        "request": request,
        "meta": meta,
        "config": config,
        "interests": interests_data.get("interests", []),
        "motivations": interests_data.get("motivations", {}),
        "values": interests_data.get("values", []),
        "goals": interests_data.get("goals", [])
    })

@app.get("/knowledge", response_class=HTMLResponse)
async def knowledge(request: Request):
    config = get_site_config()
    meta = get_page_meta("knowledge", config)
    knowledge_data = load_data("knowledge.yaml")
    return templates.TemplateResponse("knowledge.html", {
        "request": request,
        "meta": meta,
        "config": config,
        "knowledge_data": knowledge_data,
        "education": knowledge_data.get("education", []),
        "certifications": knowledge_data.get("certifications", []),
        "technical_skills": knowledge_data.get("technical_skills", {}),
        "learning_philosophy": knowledge_data.get("learning_philosophy", {}),
        "current_learning": knowledge_data.get("current_learning", [])
    })

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    config = get_site_config()
    meta = get_page_meta("contact", config)
    return templates.TemplateResponse("contact.html", {
        "request": request,
        "meta": meta,
        "config": config
    })

@app.get("/sitemap.xml")
async def sitemap():
    """Generate XML sitemap for SEO"""
    config = get_site_config()
    base_url = config.get("base_url", "https://jambuilds.com")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{base_url}/</loc>
        <changefreq>monthly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{base_url}/about</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{base_url}/leadership</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{base_url}/projects</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{base_url}/blog</loc>
        <changefreq>weekly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{base_url}/interests</loc>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
    <url>
        <loc>{base_url}/knowledge</loc>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{base_url}/contact</loc>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
</urlset>"""

    return HTMLResponse(content=sitemap_xml, media_type="application/xml")

@app.get("/robots.txt")
async def robots():
    """Generate robots.txt for SEO"""
    config = get_site_config()
    base_url = config.get("base_url", "https://jambuilds.com")

    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml"""

    return HTMLResponse(content=robots_txt, media_type="text/plain")

# Vercel serverless function handler
from mangum import Mangum
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)