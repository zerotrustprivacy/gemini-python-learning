## Gemini Python Learning Space - AI Assistant Instructions

### Project Overview
This repository is a structured, hands-on learning environment for Python, assisted by Gemini. The goal is to guide users from beginner to advanced levels through a series of self-contained lessons. The project emphasizes learning by doing within a pre-configured, secure development container.

### Project Structure & Patterns
*   **Lesson-based directories**: All content is organized within the `lessons/` directory.
*   **Numbered and Descriptive Naming**: Each lesson resides in its own folder, named with a numeric prefix and a descriptive, kebab-case title (e.g., `01-variables-and-data-types`, `02-working-with-strings`). This ensures chronological order and clarity.
*   **Consistent File Structure**: Every lesson directory **must** contain three files:
    *   `lesson.md`: A detailed explanation of the concept with code examples.
    *   `challenge.py`: A set of exercises for the user to complete. It should include a self-checking mechanism where appropriate.
    *   `solution.py`: The official, well-commented solution to the challenge.

### Development Environment
*   **VS Code Dev Container**: The project uses a Dev Container for a consistent, isolated, and zero-setup environment.
*   **Docker Image**: The environment is built from the `mcr.microsoft.com/devcontainers/python:3.11-bullseye` image.
*   **Dependencies**: Python packages are managed via `requirements.txt`.
*   **Extensions**: The container automatically installs `ms-python.python`, `ms-python.vscode-pylance`, and `Google.gemini`.

### Key Workflows
*   **Creating a New Lesson**:
    1.  Create a new directory inside `lessons/` (e.g., `mkdir lessons/02-working-with-strings`).
    2.  Create the three required files: `lesson.md`, `challenge.py`, and `solution.py`.
    3.  Populate the files with high-quality, educational content.
    4.  Update the lesson table in the main `README.md` to include the new lesson.

### AI Assistant Guidelines
When helping with this codebase:

*   **Tone**: Maintain a friendly, encouraging, and professional tone.
*   **Clarity**: Ensure all explanations and code comments are clear, concise, and aimed at a learner.
*   **Best Practices**: Use modern Python 3.11+ features and adhere to PEP 8 styling guidelines.
*   **Maintain Structure**: Strictly follow the established file and directory structure for all new lessons.
*   **Update README**: When adding a new lesson, always update the lesson plan table in the root `README.md`.
*   **Security**: Do not include any sensitive information. Ensure all code is safe to run in the sandboxed container environment.