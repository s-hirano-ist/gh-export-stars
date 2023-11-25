# Github Export Stars

## Install

Install rye

```bash
curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash
echo 'source "$HOME/.rye/env"' >> ~/.bashrc
source "$HOME/.rye/env"
```

Install packages

```bash
rye sync
```

Install pre-commit

```bash
rye run pre-commit install
```

## Run

Export github stars

```bash
rye run python src/main.py --user GITHUB_USERNAME
```

```bash
rye run python src/main.py --user GITHUB_USERNAME --output <output file name>
```

Run pre-commit manually

```bash
rye run pre-commit run --files src/main.py
```
