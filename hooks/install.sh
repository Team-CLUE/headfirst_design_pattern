REPO_ROOT=$(git rev-parse --show-toplevel)

# Install pre-commit
rm -f $REPO_ROOT/.git/hooks/pre-commit && rm -f $REPO_ROOT/.git/hooks/pre-commit.legacy
pip install pre-commit
cd $REPO_ROOT && pre-commit install

# ipynb diff
pip install nbdime
nbdime config-git --enable
git config diff.jupyternotebook.command "git-nbdiffdriver diff -s"

# track ipynb with lfs
git lfs install
git config diff.lfs.textconv cat
