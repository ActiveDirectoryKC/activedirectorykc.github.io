"""Keep the footer copyright end year current at build time."""
from datetime import date


def on_config(config):
    config["copyright"] = f"Copyright &copy; 2020 - {date.today().year} Tyler Jacobs"
    return config
