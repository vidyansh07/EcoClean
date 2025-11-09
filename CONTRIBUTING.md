# Contributing to Car-Bon

Thank you for considering contributing to Car-Bon! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Maintain professional communication

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported
2. Use the issue tracker with the "bug" label
3. Include:
   - Detailed description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Error logs if applicable

### Suggesting Enhancements

1. Use the issue tracker with the "enhancement" label
2. Clearly describe the feature and its benefits
3. Provide use cases and examples

### Code Contributions

#### Setup Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/vidyansh07/EcoClean.git
cd EcoClean

# Setup API environment
cd src/API
poetry install
poetry shell

# Setup UI environment
cd src/UI/old/car-bon-ui
npm install
```

#### Making Changes

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following the code style guidelines

3. Write/update tests if applicable

4. Update documentation as needed

5. Commit your changes:
```bash
git commit -m "type: brief description

Detailed explanation of changes"
```

#### Commit Message Convention

Follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

#### Pull Request Process

1. Update README.md if needed
2. Update documentation in `docs/`
3. Ensure all tests pass
4. Request review from maintainers

### Code Style Guidelines

#### Python

- Follow PEP 8
- Use type hints
- Write docstrings for all public functions/classes
- Maximum line length: 100 characters

Example:
```python
def function_name(param1: str, param2: int) -> Dict[str, Any]:
    """
    Brief description.
    
    Detailed description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
    pass
```

#### JavaScript/TypeScript

- Use Prettier for formatting
- Follow ESLint rules
- Use meaningful variable names
- Write JSDoc comments for functions

### Testing

- Write unit tests for new features
- Ensure existing tests pass
- Aim for high code coverage

```bash
# Run Python tests
pytest

# Run JavaScript tests
npm test
```

## Project Structure

```
EcoClean/
├── src/API/          # Backend API
├── src/UI/           # Frontend applications
├── infra/            # Infrastructure as Code
├── docs/             # Documentation
└── tests/            # Test files
```

## Getting Help

- Open an issue for questions
- Check existing documentation
- Contact maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
```

Thank you for your contributions! 🎉
