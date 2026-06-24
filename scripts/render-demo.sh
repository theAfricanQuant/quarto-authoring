#!/usr/bin/env bash
# colorful-pdf skill — quick test runner
# Usage: bash render-demo.sh
set -euo pipefail

OUTDIR="$HOME/Documents/pdf-outputs"
SKILL_DIR="$HOME/.config/opencode/skills/colorful-pdf/examples"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

echo "==> Copying demo files to $WORKDIR"
cp "$SKILL_DIR/demo.qmd" "$SKILL_DIR/demo.css" "$WORKDIR/"
cd "$WORKDIR"

mkdir -p "$OUTDIR"

# --- WeasyPrint route ---
echo ""
echo "=== Route 1: qmd + WeasyPrint ==="
if command -v weasyprint &>/dev/null; then
  quarto render demo.qmd --to html --quiet
  weasyprint demo.html "$OUTDIR/demo-weasy.pdf"
  echo "-> $OUTDIR/demo-weasy.pdf"
else
  echo "[SKIP] weasyprint not found. Install with: uv tool install weasyprint"
fi

# --- Typst route ---
echo ""
echo "=== Route 2: qmd + Typst ==="
quarto render demo.qmd --to typst --quiet
cp demo.pdf "$OUTDIR/demo-typst.pdf"
echo "-> $OUTDIR/demo-typst.pdf"

echo ""
echo "Done. Open the PDFs:"
ls -lh "$OUTDIR"/demo-*.pdf 2>/dev/null || echo "(some files missing)"
