import argparse
import hashlib
from pathlib import Path

from hashling.hash import hash_file


def file_exists(filepath):
    return Path(filepath).exists()


def hash_algorithm_exists(hashalg):
    return hashalg.lower() in {
        alg.lower() for alg in hashlib.algorithms_available
    }


def list_hash_algorithms():
    for alg in sorted(
        hashlib.algorithms_available, key=lambda x: x.lower()
    ):
        print(f"- {alg.lower()}")
    print()  # Adds a blank line for clean exit


def setup_cli():
    parser = argparse.ArgumentParser(
        prog="Hashling",
        description="A Python CLI Tool to Hash Files",
    )

    parser.add_argument("filepath", help="The path to the file to hash")
    parser.add_argument("hashalg", help="The hashing algorithm to use")
    parser.add_argument(
        "-l",
        "--list-supported",
        action="store_true",
        help="List supported hash algorithms",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show resulting file and hash",
    )
    return parser.parse_args()


def main():
    args = setup_cli()

    filepath, hashalg, verbose, listalg = (
        args.filepath,
        args.hashalg,
        args.verbose,
        args.list_supported,
    )

    if listalg:
        return list_hash_algorithms()

    if not file_exists(filepath):
        raise FileNotFoundError(f"{filepath} does not exist")

    if not hash_algorithm_exists(hashalg):
        raise ValueError(
            f"{hashalg} is unsupported. Use --list-supported to see available algorithms."
        )

    result = hash_file(filepath, hashalg)

    if verbose:
        print(f"File: {filepath}")
        print(f"Hash: {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()
