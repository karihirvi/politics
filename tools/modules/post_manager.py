"""
Postausten hallintamoduuli

Tämä moduuli sisältää funktiot postausten luomiseen, listaamiseen ja iteraatioiden hallintaan.
"""

from pathlib import Path
import shutil
import re
from typing import Dict, List, Optional, Any


# Project root (politics/)
PROJECT_ROOT = Path(__file__).parent.parent.parent
POSTAUKSET_DIR = PROJECT_ROOT / "postaukset"
TEMPLATE_PATH = PROJECT_ROOT / "resurssit" / "tyokalut" / "pyyntopohja-malli.md"


def _normalize_post_id(post_id: str) -> str:
    """
    Normalisoi postauksen ID muotoon p###
    
    Args:
        post_id: Postauksen ID (esim. "p001", "001", "1")
    
    Returns:
        Normalisoitu ID (esim. "p001")
    """
    # Remove p-prefix if present
    if post_id.lower().startswith('p'):
        post_id = post_id[1:]
    
    # Convert to number and format
    try:
        num = int(post_id)
        return f"p{num:03d}"
    except ValueError:
        raise ValueError(f"Virheellinen postaus ID: {post_id}")


def create_new_post(aihe: str) -> Dict[str, str]:
    """
    Luo uusi postaus annetulla aiheella
    
    Args:
        aihe: Postauksen aihe (käytetään kansion nimessä)
    
    Returns:
        Dict sisältäen:
            - folder: Luodun kansion nimi
            - file: Luodun tiedoston nimi
            - path: Täysi polku tiedostoon
    
    Raises:
        FileNotFoundError: Jos template-tiedostoa ei löydy
        PermissionError: Jos ei oikeuksia luoda kansiota
    """
    # Check that template exists
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Pyyntöpohjaa ei löydy: {TEMPLATE_PATH}")
    
    # Ensure posts directory exists
    POSTAUKSET_DIR.mkdir(parents=True, exist_ok=True)
    
    # Find next available number
    existing_posts = sorted(POSTAUKSET_DIR.glob("p[0-9][0-9][0-9]-*"))
    
    if existing_posts:
        # Get the last post number
        last_folder = existing_posts[-1].name
        match = re.match(r'p(\d{3})', last_folder)
        if match:
            last_num = int(match.group(1))
            next_num = last_num + 1
        else:
            next_num = 1
    else:
        next_num = 1
    
    # Format folder name
    # Remove special characters from topic
    clean_topic = re.sub(r'[^\w\s-]', '', aihe.lower())
    clean_topic = re.sub(r'[-\s]+', '-', clean_topic)
    clean_topic = clean_topic.strip('-')
    
    folder_name = f"p{next_num:03d}-{clean_topic}"
    new_dir = POSTAUKSET_DIR / folder_name
    
    # Create directory
    try:
        new_dir.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        raise FileExistsError(f"Kansio on jo olemassa: {folder_name}")
    
    # Copy request template
    file_name = f"p{next_num:03d}-01-a-pyyntö.md"
    target_file = new_dir / file_name
    
    try:
        shutil.copy2(TEMPLATE_PATH, target_file)
    except Exception as e:
        # If copying fails, remove created directory
        shutil.rmtree(new_dir)
        raise e
    
    return {
        'folder': folder_name,
        'file': file_name,
        'path': str(target_file)
    }


def list_all_posts() -> List[Dict[str, Any]]:
    """
    Listaa kaikki postaukset ja niiden tilat
    
    Returns:
        Lista dictionary-objekteja, jokainen sisältää:
            - id: Postauksen ID (esim. "p001")
            - topic: Postauksen aihe
            - iterations: Iteraatioiden määrä
            - latest_file: Viimeisin tiedosto
            - waiting_response: Odottaako Clauden vastausta (viimeisin on a-tiedosto)
            - path: Polku kansioon
    """
    posts = []
    
    # Find all p### folders
    post_folders = sorted(POSTAUKSET_DIR.glob("p[0-9][0-9][0-9]-*"))
    
    for folder in post_folders:
        # Parse ID and topic
        match = re.match(r'(p\d{3})-(.+)', folder.name)
        if not match:
            continue
            
        post_id = match.group(1)
        topic = match.group(2).replace('-', ' ').title()
        
        # Find all a- and b-files
        a_files = sorted(folder.glob(f"{post_id}-*-a-*.md"))
        b_files = sorted(folder.glob(f"{post_id}-*-b-*.md"))
        
        # Count iterations (a-b pairs)
        iterations = max(len(a_files), len(b_files))
        
        # Find latest file
        all_files = sorted(folder.glob(f"{post_id}-*.md"))
        latest_file = all_files[-1].name if all_files else "Ei tiedostoja"
        
        # Check if latest is b-file (waiting for response if a-file)
        latest_is_b = all_files and all_files[-1].name.split('-')[2] == 'b' if all_files else False
        
        posts.append({
            'id': post_id,
            'topic': topic,
            'iterations': iterations,
            'latest_file': latest_file,
            'waiting_response': not latest_is_b and bool(all_files),
            'path': str(folder)
        })
    
    return posts


def create_next_iteration(postaus_id: str) -> Dict[str, str]:
    """
    Luo seuraava iteraatiotiedosto (a-tiedosto palautteelle)
    
    Args:
        postaus_id: Postauksen tunniste (esim. "p001" tai "001")
    
    Returns:
        Dict sisältäen:
            - file: Luodun tiedoston nimi
            - path: Täysi polku tiedostoon
            - iteration: Iteraation numero
    
    Raises:
        FileNotFoundError: Jos postausta ei löydy
        ValueError: Jos viimeisin on jo a-tiedosto (odottaa b-vastausta)
    """
    # Normalize ID
    post_id = _normalize_post_id(postaus_id)
    
    # Find post folder
    post_folders = list(POSTAUKSET_DIR.glob(f"{post_id}-*"))
    
    if not post_folders:
        raise FileNotFoundError(f"Postausta ei löydy: {post_id}")
    
    folder = post_folders[0]
    
    # Find all files
    all_files = sorted(folder.glob(f"{post_id}-*.md"))
    
    if not all_files:
        raise FileNotFoundError(f"Postauksessa ei ole tiedostoja: {post_id}")
    
    # Check latest file
    latest = all_files[-1]
    latest_parts = latest.stem.split('-')
    
    # If latest is a-file, cannot create new one
    if latest_parts[2] == 'a':
        raise ValueError(f"Viimeisin on palaute ({latest.name}). Odottaa Clauden vastausta (b-tiedosto).")
    
    # Calculate next iteration number
    # Find highest iteration number
    max_iteration = 0
    for file in all_files:
        parts = file.stem.split('-')
        if len(parts) >= 2:
            try:
                iteration = int(parts[1])
                max_iteration = max(max_iteration, iteration)
            except ValueError:
                continue
    
    next_iteration = max_iteration + 1
    
    # Create new a-file
    file_name = f"{post_id}-{next_iteration:02d}-a-palaute.md"
    new_file = folder / file_name
    
    # Create file with basic template
    content = f"""# Palaute iteraatioon {max_iteration:02d}

## Mikä toimi hyvin

[Kirjoita tähän mikä toimi]

## Mitä pitää muuttaa

[Kirjoita tähän mitä pitää muuttaa]

## Muut huomiot

[Vapaamuotoiset huomiot]
"""
    
    new_file.write_text(content, encoding='utf-8')
    
    return {
        'file': file_name,
        'path': str(new_file),
        'iteration': next_iteration
    }


def get_latest_version(postaus_id: str) -> Dict[str, Any]:
    """
    Hakee postauksen viimeisimmän version
    
    Args:
        postaus_id: Postauksen tunniste (esim. "p001" tai "001")
    
    Returns:
        Dict sisältäen:
            - file: Tiedoston nimi
            - path: Täysi polku
            - type: 'a' (palaute) tai 'b' (generoitu)
            - iteration: Iteraation numero
            - content_preview: Ensimmäiset 500 merkkiä sisällöstä
    
    Raises:
        FileNotFoundError: Jos postausta ei löydy
    """
    # Normalize ID
    post_id = _normalize_post_id(postaus_id)
    
    # Find post folder
    post_folders = list(POSTAUKSET_DIR.glob(f"{post_id}-*"))
    
    if not post_folders:
        raise FileNotFoundError(f"Postausta ei löydy: {post_id}")
    
    folder = post_folders[0]
    
    # Find all files
    all_files = sorted(folder.glob(f"{post_id}-*.md"))
    
    if not all_files:
        raise FileNotFoundError(f"Postauksessa ei ole tiedostoja: {post_id}")
    
    # Latest file
    latest = all_files[-1]
    latest_parts = latest.stem.split('-')
    
    # Read content preview
    try:
        content = latest.read_text(encoding='utf-8')
        preview = content[:500] + "..." if len(content) > 500 else content
    except Exception:
        preview = "[Sisältöä ei voitu lukea]"
    
    return {
        'file': latest.name,
        'path': str(latest),
        'type': latest_parts[2],  # 'a' tai 'b'
        'iteration': int(latest_parts[1]),
        'content_preview': preview
    }


# Helper functions for future extensions

def get_post_path(postaus_id: str) -> Optional[Path]:
    """
    Hakee postauksen kansion polun
    
    Args:
        postaus_id: Postauksen tunniste
    
    Returns:
        Path-objekti tai None jos ei löydy
    """
    post_id = _normalize_post_id(postaus_id)
    folders = list(POSTAUKSET_DIR.glob(f"{post_id}-*"))
    return folders[0] if folders else None


def get_iteration_count(postaus_id: str) -> int:
    """
    Laskee postauksen iteraatioiden määrän
    
    Args:
        postaus_id: Postauksen tunniste
    
    Returns:
        Iteraatioiden määrä
    """
    folder = get_post_path(postaus_id)
    if not folder:
        return 0
    
    # Calculate maximum iteration number
    max_iter = 0
    for file in folder.glob("*.md"):
        parts = file.stem.split('-')
        if len(parts) >= 2:
            try:
                iteration = int(parts[1])
                max_iter = max(max_iter, iteration)
            except ValueError:
                continue
    
    return max_iter