# Branching Strategy: GitHub Flow

## Branches
- main: Production branch
- feature/*: Feature branches
- bugfix/*: Bug fixes

## Workflow
1. Create branch: git checkout -b feature/name
2. Make changes
3. Commit: git commit -m "feat: description"
4. Push: git push -u origin feature/name
5. Create Pull Request
6. Merge when CI passes
