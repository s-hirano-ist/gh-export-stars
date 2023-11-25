import json
import sys
from argparse import ArgumentParser
from collections.abc import Iterator
from math import ceil

from github import Github, Repository


def __starred_repos(user: str) -> Iterator[Repository.Repository]:
    github_user = Github().get_user(user)
    starred = github_user.get_starred()
    total_pages = ceil(starred.totalCount / 30)

    for page_num in range(0, total_pages):
        for repo in starred.get_page(page_num):
            yield repo


def main() -> None:
    parser = ArgumentParser(
        prog="gh-export-stars",
        description="Export Github stars to a json file",
    )
    parser.add_argument("--user")
    parser.add_argument("--output", default="./output.json")
    args = parser.parse_args()

    if not args.user:
        print("Set `--user` option and a github user name", file=sys.stderr)
        sys.exit(1)

    data = [
        {"url": repo.html_url, "description": repo.description}
        for repo in __starred_repos(args.user)
    ]

    with open(args.output, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    main()
