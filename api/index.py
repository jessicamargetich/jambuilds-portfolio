from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import yaml
from pathlib import Path

# Get the current directory
CURRENT_DIR = Path(__file__).parent
BASE_DIR = CURRENT_DIR.parent

app = FastAPI()

# Set up templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Data loading functions
def load_data(filename: str) -> dict:
    """Load YAML data file"""
    try:
        data_path = BASE_DIR / "data" / filename
        with open(data_path, "r") as file:
            data = yaml.safe_load(file)
            return data or {}
    except Exception as e:
        return {}

def get_site_config() -> dict:
    return load_data("config.yaml")

def get_page_meta(page: str, config: dict) -> dict:
    base_meta = {
        "title": config.get("site_name", "jambuilds.com"),
        "description": config.get("site_description", "Professional portfolio"),
        "keywords": config.get("keywords", ""),
        "author": config.get("author", ""),
        "url": config.get("base_url", "https://jambuilds.com")
    }
    page_meta = config.get("pages", {}).get(page, {})
    return {**base_meta, **page_meta}

@app.get("/")
async def home(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("home", config)
        return templates.TemplateResponse("home.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Portfolio Loading...</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/about")
async def about(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("about", config)
        return templates.TemplateResponse("about.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>About Page</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/career-journey")
async def career_journey(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("about", config)
        meta["title"] = "Career Journey - Jessica Margetich"
        return templates.TemplateResponse("career-journey.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Career Journey</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/credentials")
async def credentials(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("knowledge", config)
        meta["title"] = "Credentials - Jessica Margetich"
        knowledge_data = load_data("knowledge.yaml")
        return templates.TemplateResponse("credentials.html", {
            "request": request,
            "meta": meta,
            "config": config,
            "education": knowledge_data.get("education", []),
            "certifications": knowledge_data.get("certifications", {}),
            "technical_skills": knowledge_data.get("technical_skills", {})
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Credentials</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/projects")
async def projects(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("projects", config)
        return templates.TemplateResponse("portfolio.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Portfolio</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/portfolio/growth-engine")
async def growth_engine(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("projects", config)
        meta["title"] = "Building the Next Growth Engine - Jessica Margetich"
        return templates.TemplateResponse("case-study-growth-engine.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Growth Engine Case Study</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/leadership")
async def leadership(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("leadership", config)
        leadership_data = load_data("leadership.yaml")
        return templates.TemplateResponse("leadership.html", {
            "request": request,
            "meta": meta,
            "config": config,
            "experiences": leadership_data.get("experiences", []),
            "philosophy": leadership_data.get("philosophy", {}),
            "metrics": leadership_data.get("metrics", [])
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Leadership Page</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/portfolio/trust-experience")
async def trust_experience(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("projects", config)
        return templates.TemplateResponse("case-study-trust-experience.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Trust Experience Case Study</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/portfolio/failing-fast")
async def failing_fast(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("projects", config)
        return templates.TemplateResponse("case-study-failing-fast.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Failing Fast Case Study</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/portfolio/north-star")
async def north_star(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("projects", config)
        return templates.TemplateResponse("case-study-north-star.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>North Star Case Study</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/portfolio/people-potential")
async def people_potential(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("projects", config)
        return templates.TemplateResponse("case-study-people-potential.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>People Potential Case Study</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/blog")
async def blog(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("blog", config)
        blog_data = load_data("blog.yaml")
        return templates.TemplateResponse("blog.html", {
            "request": request,
            "meta": meta,
            "config": config,
            "posts": blog_data.get("posts", []),
            "filter_options": blog_data.get("filter_options", {})
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Blog Page</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/interests")
async def interests(request: Request):
    try:
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
    except Exception as e:
        return HTMLResponse(f"<h1>Interests Page</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/knowledge")
async def knowledge(request: Request):
    try:
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
    except Exception as e:
        return HTMLResponse(f"<h1>Knowledge Page</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/contact")
async def contact(request: Request):
    try:
        config = get_site_config()
        meta = get_page_meta("contact", config)
        return templates.TemplateResponse("contact.html", {
            "request": request,
            "meta": meta,
            "config": config
        })
    except Exception as e:
        return HTMLResponse(f"<h1>Contact Page</h1><p>Debug: {str(e)}</p>", status_code=200)

@app.get("/sitemap.xml")
async def sitemap():
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://jambuilds.com/</loc>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://jambuilds.com/about</loc>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://jambuilds.com/projects</loc>
        <priority>0.9</priority>
    </url>
</urlset>"""
    return HTMLResponse(content=sitemap_xml, media_type="application/xml")

@app.get("/robots.txt")
async def robots():
    robots_txt = """User-agent: *
Allow: /

Sitemap: https://jambuilds.com/sitemap.xml"""
    return HTMLResponse(content=robots_txt, media_type="text/plain")

# Export app for Vercel
# Vercel will automatically handle the ASGI interface