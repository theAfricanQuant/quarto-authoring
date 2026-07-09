#!/usr/bin/env node
/**
 * Installer for the quarto-authoring skill.
 *
 * Copies SKILL.md, references/, examples/, and scripts/ into the skills
 * directory of one or more coding agents.
 *
 *   npx quarto-authoring-skill              # -> ~/.claude/skills/quarto-authoring
 *   npx quarto-authoring-skill --project    # -> ./.claude/skills/quarto-authoring
 *   npx quarto-authoring-skill --opencode   # -> ~/.config/opencode/skills/quarto-authoring
 *   npx quarto-authoring-skill --all        # claude + opencode
 *   npx quarto-authoring-skill --dir <path> # custom directory
 */

const fs = require("fs");
const path = require("path");
const os = require("os");

const SKILL_NAME = "quarto-authoring";
const PKG_ROOT = path.resolve(__dirname, "..");
const PAYLOAD = ["SKILL.md", "references", "examples", "scripts"];

const args = process.argv.slice(2);

if (args.includes("--help") || args.includes("-h")) {
  console.log(`
Install the ${SKILL_NAME} skill (Quarto + Typst: docs, websites, blogs,
books in PDF/EPUB, presentations, publishing).

Usage: npx quarto-authoring-skill [options]

Options:
  (none)       Install for Claude Code, user-wide (~/.claude/skills/)
  --project    Install into the current project (./.claude/skills/)
  --opencode   Install for OpenCode (~/.config/opencode/skills/)
  --all        Install for Claude Code and OpenCode
  --dir <path> Install into a custom directory
  --help       Show this message
`);
  process.exit(0);
}

const targets = [];
const home = os.homedir();

if (args.includes("--dir")) {
  const i = args.indexOf("--dir");
  const dir = args[i + 1];
  if (!dir) {
    console.error("error: --dir requires a path argument");
    process.exit(1);
  }
  targets.push({ label: "custom directory", dir: path.resolve(dir, SKILL_NAME) });
} else {
  const wantClaude =
    args.length === 0 || args.includes("--all") || args.includes("--claude");
  const wantProject = args.includes("--project");
  const wantOpencode = args.includes("--all") || args.includes("--opencode");

  if (wantProject)
    targets.push({
      label: "Claude Code (project)",
      dir: path.resolve(process.cwd(), ".claude", "skills", SKILL_NAME),
    });
  if (wantClaude && !wantProject)
    targets.push({
      label: "Claude Code (user)",
      dir: path.join(home, ".claude", "skills", SKILL_NAME),
    });
  if (wantOpencode)
    targets.push({
      label: "OpenCode",
      dir: path.join(home, ".config", "opencode", "skills", SKILL_NAME),
    });
}

if (targets.length === 0) {
  console.error("error: no install target selected (see --help)");
  process.exit(1);
}

for (const item of PAYLOAD) {
  if (!fs.existsSync(path.join(PKG_ROOT, item))) {
    console.error(`error: package is missing "${item}" — corrupt install?`);
    process.exit(1);
  }
}

for (const { label, dir } of targets) {
  const existed = fs.existsSync(dir);
  if (existed) fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
  for (const item of PAYLOAD) {
    fs.cpSync(path.join(PKG_ROOT, item), path.join(dir, item), {
      recursive: true,
    });
  }
  console.log(`${existed ? "updated" : "installed"}  ${label}  ->  ${dir}`);
}

console.log(
  `\nDone. The skill triggers on Quarto/Typst questions — websites, blogs,\nbooks (PDF/EPUB), CVs, presentations, and publishing.`
);
