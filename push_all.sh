#!/bin/bash

# Pushes every source file individually to GitHub with a descriptive commit message.
# Output/artifact files (*.json, *.csv, *.xlsx, *.pdf, *.png) are skipped.

set -e

echo "Starting individual file push process..."
echo ""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Returns 0 (true) if the file should be skipped (output/artifact files)
should_skip() {
    local file=$1
    case "$file" in
        *.json|*.csv|*.xlsx|*.pdf|*.png)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# Generates a descriptive commit message based on the file's path and role
generate_commit_message() {
    local file=$1
    local filename
    filename=$(basename "$file")
    local project
    project=$(echo "$file" | cut -d'/' -f1)

    case "$file" in

        # ── Spider files ──────────────────────────────────────────────────

        *"spiders/ebook.py")
            echo "Add ebook spider: crawl travel books with title, price, and availability from books.toscrape.com"
            ;;
        *"spiders/login.py")
            echo "Add login spider: demonstrate form-based authentication using Scrapy FormRequest"
            ;;
        *"spiders/table.py")
            echo "Add table spider: extract and parse HTML table data from a product detail page"
            ;;
        *"spiders/oscar.py")
            echo "Add oscar spider: scrape Ajax-rendered Oscar film data via Playwright JS interaction"
            ;;
        *"spiders/pdfs.py")
            echo "Add pdf spider: render a live webpage and export it as PDF using Playwright"
            ;;
        *"spiders/quote.py")
            echo "Add quote spider: automate login form submission and extract page content using Playwright"
            ;;
        *"spiders/screenshots.py")
            echo "Add screenshot spider: capture a full-page screenshot using Playwright"
            ;;

        # ── Core Scrapy files ─────────────────────────────────────────────

        *"items.py")
            echo "Add items: define Item data models for the $project project"
            ;;
        *"pipelines.py")
            echo "Add pipeline: configure item processing and export pipeline for $project"
            ;;
        *"settings.py")
            echo "Add settings: configure Scrapy and Playwright settings for $project"
            ;;
        *"middlewares.py")
            echo "Add middleware: set up custom request/response middleware for $project"
            ;;

        # ── Package init files ────────────────────────────────────────────

        *"spiders/__init__.py")
            echo "Add init: initialize spiders package for $project"
            ;;
        *"__init__.py")
            echo "Add init: initialize $project module"
            ;;

        # ── Project config ────────────────────────────────────────────────

        *"scrapy.cfg")
            echo "Add config: Scrapy deployment settings for $project"
            ;;

        # ── Repo-level files ──────────────────────────────────────────────

        "README.md")
            echo "Add docs: project overview, setup instructions, and spider run commands"
            ;;
        ".gitignore")
            echo "Add gitignore: exclude venv, cache files, and scraped output artifacts"
            ;;

        # ── Fallback ──────────────────────────────────────────────────────

        *)
            echo "Add $project: include $filename"
            ;;
    esac
}

# ---------------------------------------------------------------------------
# Collect files
# ---------------------------------------------------------------------------

# Modified tracked files
modified_files=$(git status --porcelain | grep '^ M' | cut -c4-)

# Untracked files (uses ls-files to expand untracked directories into individual files)
untracked_files=$(git ls-files --others --exclude-standard)

committed=0

# ---------------------------------------------------------------------------
# Process modified tracked files
# ---------------------------------------------------------------------------
if [ -n "$modified_files" ]; then
    echo "── Modified files ──────────────────────────────────────"
    while IFS= read -r file; do
        [ -z "$file" ] && continue

        if should_skip "$file"; then
            echo "  SKIP  $file  (output artifact)"
            continue
        fi

        commit_msg=$(generate_commit_message "$file")
        echo "  COMMIT  $file"
        echo "          → $commit_msg"
        git add "$file"
        git commit -m "$commit_msg"
        committed=$((committed + 1))
        echo ""
    done <<< "$modified_files"
fi

# ---------------------------------------------------------------------------
# Process untracked files
# ---------------------------------------------------------------------------
if [ -n "$untracked_files" ]; then
    echo "── Untracked files ─────────────────────────────────────"
    while IFS= read -r file; do
        [ -z "$file" ] && continue

        if should_skip "$file"; then
            echo "  SKIP  $file  (output artifact)"
            continue
        fi

        commit_msg=$(generate_commit_message "$file")
        echo "  COMMIT  $file"
        echo "          → $commit_msg"
        git add "$file"
        git commit -m "$commit_msg"
        committed=$((committed + 1))
        echo ""
    done <<< "$untracked_files"
fi

# ---------------------------------------------------------------------------
# Push
# ---------------------------------------------------------------------------
echo "────────────────────────────────────────────────────────"

if [ "$committed" -eq 0 ]; then
    echo "No new commits — nothing to push."
    exit 0
fi

echo "Pushing $committed commit(s) to GitHub..."
git push origin main
echo ""
echo "All $committed files pushed to GitHub successfully."
