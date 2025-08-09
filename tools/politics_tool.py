#!/usr/bin/env python3
"""
Poliittisen viestintäjärjestelmän hallintatyökalu

Käyttö:
    python tools/politics_tool.py [komento] [argumentit]

Komennot:
    uusi [aihe]         - Luo uusi postaus
    listaa              - Listaa kaikki postaukset
    seuraava [p###]     - Luo seuraava iteraatio
    viimeisin [p###]    - Näytä viimeisin versio
"""

import click
from pathlib import Path
import sys

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from tools.modules import post_manager


@click.group()
def cli():
    """Poliittisen viestintäjärjestelmän CLI-työkalu"""
    pass


@cli.command()
@click.argument('aihe')
def uusi(aihe):
    """Luo uusi postaus annetulla aiheella
    
    Args:
        aihe: Postauksen aihe (käytetään kansion nimessä)
    """
    try:
        result = post_manager.create_new_post(aihe)
        click.echo(f"✅ Luotu: {result['folder']}")
        click.echo(f"📝 Täytä pyyntö: {result['file']}")
        click.echo(f"📍 Polku: {result['path']}")
    except Exception as e:
        click.echo(f"❌ Virhe: {e}", err=True)
        sys.exit(1)


@cli.command()
def listaa():
    """Listaa kaikki postaukset ja niiden tilat"""
    try:
        posts = post_manager.list_all_posts()
        
        if not posts:
            click.echo("Ei postauksia.")
            return
            
        click.echo("\n📚 POSTAUKSET:\n")
        click.echo("-" * 70)
        
        for post in posts:
            status_icon = "🔄" if post['waiting_response'] else "✅"
            click.echo(f"{status_icon} {post['id']} - {post['topic']}")
            click.echo(f"   Iteraatioita: {post['iterations']}")
            click.echo(f"   Viimeisin: {post['latest_file']}")
            if post['waiting_response']:
                click.echo(f"   ⚠️  Odottaa Clauden vastausta")
            click.echo("-" * 70)
            
    except Exception as e:
        click.echo(f"❌ Virhe: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('postaus_id')
def seuraava(postaus_id):
    """Luo seuraava iteraatiotiedosto palautteelle
    
    Args:
        postaus_id: Postauksen tunniste (esim. p001 tai 001)
    """
    try:
        result = post_manager.create_next_iteration(postaus_id)
        click.echo(f"✅ Luotu: {result['file']}")
        click.echo(f"📝 Kirjoita palaute tiedostoon")
        click.echo(f"📍 Polku: {result['path']}")
    except Exception as e:
        click.echo(f"❌ Virhe: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('postaus_id')
def viimeisin(postaus_id):
    """Näytä postauksen viimeisin versio
    
    Args:
        postaus_id: Postauksen tunniste (esim. p001 tai 001)
    """
    try:
        result = post_manager.get_latest_version(postaus_id)
        
        if result['type'] == 'b':
            click.echo(f"📄 Viimeisin versio: {result['file']}")
            click.echo(f"   Iteraatio: {result['iteration']}")
            click.echo(f"📍 Polku: {result['path']}")
        else:
            click.echo(f"⚠️  Viimeisin on palaute: {result['file']}")
            click.echo("   Odottaa Clauden vastausta (b-tiedosto)")
            
    except Exception as e:
        click.echo(f"❌ Virhe: {e}", err=True)
        sys.exit(1)


@cli.command()
def ohje():
    """Näytä käyttöohjeet"""
    click.echo(__doc__)
    click.echo("\n📚 ESIMERKKEJÄ:\n")
    click.echo("  python tools/politics_tool.py uusi 'feminismi-ja-tasa-arvo'")
    click.echo("  python tools/politics_tool.py listaa")
    click.echo("  python tools/politics_tool.py seuraava p001")
    click.echo("  python tools/politics_tool.py viimeisin p001")
    

if __name__ == '__main__':
    cli()