#!/usr/bin/env bash
set -euo pipefail

# create-github-release.sh
# Create a GitHub release with all template zip files
# Usage: create-github-release.sh <version>

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <version>" >&2
  exit 1
fi

VERSION="$1"

# Remove 'v' prefix from version for release title
VERSION_NO_V=${VERSION#v}

gh release create "$VERSION" \
  .genreleases/nuaa-template-copilot-sh-"$VERSION".zip \
  .genreleases/nuaa-template-copilot-ps-"$VERSION".zip \
  .genreleases/nuaa-template-claude-sh-"$VERSION".zip \
  .genreleases/nuaa-template-claude-ps-"$VERSION".zip \
  .genreleases/nuaa-template-gemini-sh-"$VERSION".zip \
  .genreleases/nuaa-template-gemini-ps-"$VERSION".zip \
  .genreleases/nuaa-template-cursor-agent-sh-"$VERSION".zip \
  .genreleases/nuaa-template-cursor-agent-ps-"$VERSION".zip \
  .genreleases/nuaa-template-opencode-sh-"$VERSION".zip \
  .genreleases/nuaa-template-opencode-ps-"$VERSION".zip \
  .genreleases/nuaa-template-qwen-sh-"$VERSION".zip \
  .genreleases/nuaa-template-qwen-ps-"$VERSION".zip \
  .genreleases/nuaa-template-windsurf-sh-"$VERSION".zip \
  .genreleases/nuaa-template-windsurf-ps-"$VERSION".zip \
  .genreleases/nuaa-template-codex-sh-"$VERSION".zip \
  .genreleases/nuaa-template-codex-ps-"$VERSION".zip \
  .genreleases/nuaa-template-kilocode-sh-"$VERSION".zip \
  .genreleases/nuaa-template-kilocode-ps-"$VERSION".zip \
  .genreleases/nuaa-template-auggie-sh-"$VERSION".zip \
  .genreleases/nuaa-template-auggie-ps-"$VERSION".zip \
  .genreleases/nuaa-template-roo-sh-"$VERSION".zip \
  .genreleases/nuaa-template-roo-ps-"$VERSION".zip \
  .genreleases/nuaa-template-codebuddy-sh-"$VERSION".zip \
  .genreleases/nuaa-template-codebuddy-ps-"$VERSION".zip \
  .genreleases/nuaa-template-amp-sh-"$VERSION".zip \
  .genreleases/nuaa-template-amp-ps-"$VERSION".zip \
  .genreleases/nuaa-template-q-sh-"$VERSION".zip \
  .genreleases/nuaa-template-q-ps-"$VERSION".zip \
  --title "NUAA Project Templates - $VERSION_NO_V" \
  --notes-file release_notes.md
