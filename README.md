# Github Export Stars

## Initial setups

1. [Install Rye](https://rye-up.com/guide/installation/)

2. Install packages

```bash
rye sync
```

## How to use?

```bash
rye run python src/main.py --user <gitHub username>
```

```bash
rye run python src/main.py --user <gitHub username> --output <output file name>
```

For more information, run the following command

```bash
rye run python src/main.py --help
```

## For developers (formatters and linters)

Install pre-commit (if necessary)

```bash
rye run pre-commit install
```

Run pre-commit manually

```bash
rye run pre-commit run --files src/main.py
```
