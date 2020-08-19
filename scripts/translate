#!/usr/bin/env bash
set -euo pipefail

ESCAPE_CHAR="$(printf "\034")"

extract_variables() {
    grep -Eo '{{[^}]+}}' \
        | sed -E 's/^{{//' \
        | sed -E 's/}}$//g' \
        | sort -u
}

sanitize_variables() {
    local txt="$(cat)"
    local -r vars="$(echo "$txt" | extract_variables)"
    local sanitized_v

    for v in $vars; do
        sanitized_v="$(echo "$v" | sed 's/[^a-zA-Z0-9_]/_/g')"
        txt="$(echo "$txt" | sed "s${ESCAPE_CHAR}{{${v}}}${ESCAPE_CHAR}<${sanitized_v}>${ESCAPE_CHAR}g")"        
    done
    
    echo "$txt"
}

format_markdown() {
    grep -E '^[-`]' \
        | sed -E 's/:$//' \
        | sed 's/^\-/#/' \
        | sed -E 's/^`(.*)` *$/\1\'$'\n/g' \
        | sanitize_variables
}

tags_from_filename() {
    sed -E 's|[^t]*tldr/pages/||' \
        | sed 's/\.md//' \
        | tr '/' ' ' \
        | awk '{ for (i=NF; i>1; i--) printf("%s ",$i); print $1; }' \
        | sed 's/ /, /g'
}

comments_from_filename() {
    echo "; This has been extracted from"
    printf "; "
    sed -E 's|[^t]*tldr|https://github.com/tldr-pages/tldr/blob/master|'
}

format_markdown_file() {
    local -r filename="$1"
    echo "$filename" | comments_from_filename
    echo
    printf "%s" "% "
    echo "$filename" | tags_from_filename
    echo
    cat "$filename" | format_markdown
}

find_markdowns() {
    find './tldr/pages' -iname '*.md'
}

output_filename() {
    sed "s|^./tldr/|./|" \
        | sed 's/\.md/.cheat/' 
}

export_markdown() {
    local -r filename="$1"
    local -r out="$(echo "$filename" | output_filename)"
    mkdir -p "$(dirname "$out")" 2>/dev/null || true
    format_markdown_file "$filename" > "$out"
}

rm -rf "./pages"

for f in $(find_markdowns); do
    printf "Exporting $f: "
    export_markdown "$f" && echo "success" || echo "failed"
done