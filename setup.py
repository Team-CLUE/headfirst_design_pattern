import re
from os import path

from setuptools import find_packages, setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def find_version(*file_path_parts):
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, *file_path_parts), "r") as fp:
        version_file_text = fp.read()

    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file_text,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


MEMBERS = [
    "Donghyun Kim",
    "Ganmin Kim",
    "Jonghyuk Lee",
    "Junhyeok Yang",
    "Kyunghyun Lim",
]
MEMBER_EMAILS = [
    "rkdqus2006@naver.com",
    "rlarkdals7@gmail.com",
    "",
    "surfing2003@naver.com",
    "lkh1075@yonsei.ac.kr",
]
setup(
    name="headfirst_design_pattern",
    version="latest",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    author=", ".join(MEMBERS).strip(),
    author_email=", ".join(MEMBER_EMAILS).strip(),
    description="A repository for implementations related to design pattern projects by CLUE team members",
    keywords="hdfs_python",
    url="https://github.com/Team-CLUE/headfirst_design_pattern",
    project_urls={
        "Documentation": "https://github.com/Team-CLUE/headfirst_design_pattern",
        "Source Code": "https://github.com/Team-CLUE/headfirst_design_pattern",
    },
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
