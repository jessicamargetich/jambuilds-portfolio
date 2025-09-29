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

# Export app for Vercel
# Vercel will automatically handle the ASGI interface