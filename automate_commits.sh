#!/bin/bash

REPO_DIR="$PWD"
DAY=$1
COMMITS_PER_DAY=50
COUNTER_FILE="$REPO_DIR/commit_counter.txt"
FILES=(
    "src/main.py"
    "src/wallet.py"
    "src/utils.py"
    "tests/test_wallet.py"
    "docs/README.md"
    "config/settings.json"
)

if [ ! -f "$COUNTER_FILE" ]; then
    echo 0 > "$COUNTER_FILE"
fi

cd "$REPO_DIR" || exit 1

make_micro_change() {
    FILE=${FILES[$((RANDOM % ${#FILES[@]}))]}
    COMMIT_NUM=$(cat "$COUNTER_FILE")
    case $((RANDOM % 3)) in
        0)
            echo "# Comment $COMMIT_NUM for day $DAY" >> "$FILE"
            echo "Add comment $COMMIT_NUM to $FILE for day $DAY"
            ;;
        1)
            if [[ "$FILE" == docs/* ]]; then
                echo "- Update $COMMIT_NUM for day $DAY" >> "$FILE"
                echo "Update $FILE with entry $COMMIT_NUM"
            else
                echo "# Doc comment $COMMIT_NUM" >> "$FILE"
                echo "Add doc comment $COMMIT_NUM to $FILE"
            fi
            ;;
        2)
            echo "" >> "$FILE"
            echo "Add spacing in $FILE for commit $COMMIT_NUM"
            ;;
    esac
}

for ((i=1; i<=COMMITS_PER_DAY; i++)); do
    COMMIT_NUM=$(cat "$COUNTER_FILE")
    ((COMMIT_NUM++))
    echo "$COMMIT_NUM" > "$COUNTER_FILE"

    COMMIT_MSG=$(make_micro_change)

    git add .
    git commit -m "$COMMIT_MSG"
    git push origin main || { echo "Push failed"; exit 1; }

    echo "Commit $COMMIT_NUM: $COMMIT_MSG"
    sleep 10
done