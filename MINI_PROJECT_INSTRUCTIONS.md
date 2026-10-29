# Mini Project Instructions

This repository contains independent mini projects. Each project must live in its own folder at the repository root.

## Repository Layout

```text
LS_Mini_Projects/
├── .env                          # Local only — never committed
├── .env.example
├── .gitignore
├── MINI_PROJECT_INSTRUCTIONS.md
├── README.md
├── 1-project-name/
│   ├── PROJECT_INSTRUCTIONS.md
│   └── ...project files...
└── 2-another-project/
    ├── PROJECT_INSTRUCTIONS.md
    └── ...project files...
```

Do not place project source files directly in the repository root.

This root file is the global instruction for the entire repository. Keep repository-wide rules, security requirements, and shared conventions here. Do not move this file into an individual project or replace it with project-specific instructions.

## Root Environment File

All projects may read API keys from the root `.env` file. The root `.env` is local-only and must never be committed, copied into a project folder, or exposed in source code, logs, screenshots, or client-side bundles. It is listed in `.gitignore`.

Use these variable names when applicable:

```env
SERPER_API_KEY=
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

`ANTHROPIC_API_KEY` is the key for Claude. Project code should load environment variables through the project language's standard dotenv or environment configuration library. Never hard-code keys. Keep `.env.example` updated with variable names only and no real values.

When loading variables, resolve `.env` from the repository root rather than assuming the current working directory is the project folder. If a project is intentionally standalone, document that exception in its project instructions.

## Creating a New Project

1. Read this file completely before starting.
2. Create a folder at the repository root named `<n>-<descriptive-kebab-case-name>`, where `<n>` is the next unused project number (for example, `1-lead-list-builder`).
3. Create `<project-folder>/PROJECT_INSTRUCTIONS.md` inside the new project folder. Do not copy or move the global instruction file.
4. Add the project-specific goal, requirements, commands, dependencies, environment variables, and acceptance criteria to that file.
5. Keep all source code, tests, assets, and documentation inside the project folder.
6. Add the new project to the **Projects** table in the root `README.md` with a short description and current status.
7. Update the root `.env.example` if the project introduces a new shared variable. Do not modify `.env` with fake or placeholder secrets.
8. Run the project's available tests, linting, or build checks before considering the project complete.

## Project Instructions File

Every project must contain its own `PROJECT_INSTRUCTIONS.md` inside the project folder. It is the source of truth for that project and should include:

- Purpose and current status
- Functional requirements and constraints
- Project structure
- Setup and run commands
- Required environment variables and which services use them
- Test, lint, and build commands
- Known limitations and follow-up work
- A dated change log for project-specific updates

The project file inherits this root file's global rules and may add project-specific details, but it must not weaken the security or folder rules above. Update the root file only for repository-wide changes; update the project's file for project-specific changes.

## Updating a Project

For every project update:

1. Read both the root instructions and that project's `PROJECT_INSTRUCTIONS.md` before editing.
2. Change only the project files needed for the requested work.
3. Update that project's `PROJECT_INSTRUCTIONS.md` in the same change with the new behavior, commands, requirements, or limitations.
4. Add a concise dated entry to the project's change log.
5. Update the root `README.md` if the project's description or status changes.
6. Update this root instruction file only when the repository-wide workflow, security rules, or shared conventions change.
7. Keep unrelated project instruction files unchanged.
8. Re-run the project's focused validation checks and record any new required command or limitation.

## API Usage

Use only the services needed by a project. Validate missing API keys with a clear configuration error. Handle provider failures, rate limits, and timeouts without printing secret values. Keep API calls server-side whenever the project has a browser interface.

## Completion Checklist

- [ ] The project is in its own root-level folder.
- [ ] The project has an up-to-date `PROJECT_INSTRUCTIONS.md`.
- [ ] The project is listed with its description and status in the root `README.md`.
- [ ] Secrets are loaded from the root `.env` and are not committed or exposed.
- [ ] `.env.example` lists any required variable names without real values.
- [ ] Tests, linting, or build checks have been run.
- [ ] The project instruction change log describes the update.
