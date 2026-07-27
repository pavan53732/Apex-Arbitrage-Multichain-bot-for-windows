#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_root"

status=0
tmp_file=$(mktemp)
trap 'rm -f "$tmp_file"' EXIT HUP INT TERM

find . \( -path './.git' -o -path './.git/*' \) -prune -o -type f -name '*.md' -print | sort | while IFS= read -r file; do
  dir=$(dirname "$file")

  perl -ne '
    while (/\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)/g) {
      print $. . "\t" . $1 . "\n";
    }
  ' "$file" | while IFS=$(printf '\t') read -r line ref; do
    [ -n "$ref" ] || continue

    clean_ref=${ref%%#*}
    case "$clean_ref" in
      http://*|https://*|mailto:*|tel:*)
        continue
        ;;
      /*)
        target=".$clean_ref"
        ;;
      *)
        target="$dir/$clean_ref"
        ;;
    esac

    if [ ! -f "$target" ]; then
      printf '%s:%s -> %s\n' "$file" "$line" "$ref" >> "$tmp_file"
      status=1
    fi
  done
done

if [ -s "$tmp_file" ]; then
  echo "Broken markdown links detected:" >&2
  cat "$tmp_file" >&2
  exit 1
fi

echo "Markdown link validation passed."
