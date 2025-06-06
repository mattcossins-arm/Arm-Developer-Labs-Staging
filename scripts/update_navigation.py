import os
from pathlib import Path
import yaml
import frontmatter
from datetime import datetime

projects_dir = "../Projects/Projects"
extended_projects_dir = "../Projects/Extended-Team-Projects"

projects_pathlist = Path(projects_dir).rglob("*.md")
extended_project_pathlist = Path(extended_projects_dir).rglob("*.md")

navigation = "../docs/_data/navigation.yml"

def extract_date_components(path: Path) -> (str, str, str):
    """
    Look for a 'date' field in frontmatter. If present and valid ISO or datetime, use it.
    Otherwise, fall back to the file's last-modified timestamp. Return (YYYY, MM, DD).
    """
    post = frontmatter.load(path)
    date_meta = post.metadata.get("date")

    if isinstance(date_meta, datetime):
        dt = date_meta
    elif isinstance(date_meta, str):
        try:
            dt = datetime.fromisoformat(date_meta)
        except ValueError:
            try:
                dt = datetime.fromisoformat(date_meta[:10])
            except Exception:
                dt = None
    else:
        dt = None

    if dt is None:
        timestamp = path.stat().st_mtime
        dt = datetime.fromtimestamp(timestamp)

    return dt.strftime("%Y"), dt.strftime("%m"), dt.strftime("%d")

def make_url_from_path(path: Path) -> str:
    """
    Build URL = "/YYYY/MM/DD/<slug>.html", where slug = filename without ".md"
    """
    year, month, day = extract_date_components(path)
    slug = path.stem
    return f"/{year}/{month}/{day}/{slug}.html"

def process_yml(pathlist, level: str, tab: str):
    # Load the entire navigation.yml as a Python dict
    with open(navigation, "r") as f:
        yam_tab = yaml.safe_load(f)

    # --- Update the header URL for the "projects" tab ---
    if level == "projects":
        projects_index = Path("../Projects/projects.md")
        if projects_index.exists():
            header_url = make_url_from_path(projects_index)
            # Overwrite header[0].url
            if "header" in yam_tab and isinstance(yam_tab["header"], list):
                yam_tab["header"][0]["url"] = header_url

        # Clear existing children under yam_tab["projects"][0]["children"]
        yam_tab[tab][0]["children"].clear()

        for path in pathlist:
            filename = path.name
            slug = filename.removesuffix(".md")
            url = make_url_from_path(path)
            title = slug

            post = frontmatter.load(path)
            platform = post.metadata.get("platform")
            sw_hw = post.metadata.get("sw-hw")
            support_level = post.metadata.get("support-level")
            subjects = post.metadata.get("subjects")

            yam_tab[tab][0]["children"].append({
                "title": title,
                "url": url,
                "subjects": subjects,
                "platform": platform,
                "sw-hw": sw_hw,
                "support-level": support_level
            })

    elif level == "extended-team-project":
        # Clear existing children under yam_tab["projects"][1]["children"]
        yam_tab[tab][1]["children"].clear()

        for path in pathlist:
            filename = path.name
            slug = filename.removesuffix(".md")
            url = make_url_from_path(path)
            title = slug

            post = frontmatter.load(path)
            platform = post.metadata.get("platform")
            sw_hw = post.metadata.get("sw-hw")
            support_level = post.metadata.get("support-level")
            subjects = post.metadata.get("subjects")

            yam_tab[tab][1]["children"].append({
                "title": title,
                "url": url,
                "subjects": subjects,
                "platform": platform,
                "sw-hw": sw_hw,
                "support-level": support_level
            })

    # Write the entire YAML back out
    with open(navigation, "w") as f:
        yaml.safe_dump(yam_tab, f, sort_keys=False)

if __name__ == "__main__":
    process_yml(projects_pathlist, "projects", "projects")
    process_yml(extended_project_pathlist, "extended-team-project", "projects")
