"""
Setup window's WSL zsh default option

Author:
    Name: Donghyun Kim
    Email: rkdqus2006@naver.com
"""

import os
import re

HOME = os.path.expanduser("~")
ZSH_RC_PATH = os.path.join(HOME, ".zshrc")


def set_default_plugins(zshrc: str):
    """
    Set default plugins to zsh string
    - git
    - autocompletion
    - syntax highlighting

    Args:
        zshrc (str): zsh string

    """
    zshrc = re.sub(
        "plugins=\(.*\)",
        "plugins=( git zsh-autosuggestions zsh-syntax-highlighting )",
        zshrc,
    )
    return zshrc


def set_default_theme(zshrc: str):
    """
    Set default theme(p10k) to zsh string

    P10K theme ref:
        https://github.com/romkatv/powerlevel10k

    Args:
        zshrc (str): zsh string

    """
    zshrc = re.sub('ZSH_THEME=".*"', 'ZSH_THEME="powerlevel10k/powerlevel10k"', zshrc)
    return zshrc


if __name__ == "__main__":
    """
    Load zshrc file and update features
    """
    with open(ZSH_RC_PATH, "r+", encoding="utf-8") as zshrc:
        contents = zshrc.read()
        contents = set_default_theme(contents)
        contents = set_default_plugins(contents)
        zshrc.write(contents)
