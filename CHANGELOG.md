# Changelog

All notable changes to the Car-Bon project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.8] - 2025-11-09

### Added
- Comprehensive project documentation
  - Architecture documentation with system design details
  - Design patterns documentation covering 20+ patterns
  - Complete API schema with all endpoints
  - Database schema documentation for DynamoDB and SQL
  - Deployment guide for AWS Lambda
- Contributing guidelines
- Code documentation and docstrings for all service modules
- Type hints throughout the codebase
- Detailed comments explaining business logic

### Changed
- Improved README with complete setup instructions
- Enhanced error handling in service layers
- Better code organization and structure

### Fixed
- Documentation inconsistencies
- Code style improvements

## [1.6.7] - 2024-02-26

### Added
- Initial FastAPI implementation
- DynamoDB integration
- Twilio notification service
- User management system
- Graph generation with Pygal
- Dash dashboard for CO monitoring

### Changed
- Migrated from Flask to FastAPI
- Improved API response models with Pydantic

## [1.6.0] - 2024-02-22

### Added
- AWS Lambda deployment support
- Mangum adapter for serverless
- Docker containerization
- CloudFormation templates

### Changed
- Environment-based configuration
- AWS Secrets Manager integration

## [1.5.0] - 2023-12-17

### Added
- Real-time CO monitoring
- Alert threshold configuration
- Historical data visualization
- Time-series data queries

### Changed
- Database schema optimization
- Query performance improvements

## [1.0.0] - 2023-11-26

### Added
- Initial release
- Basic IoT data collection
- DynamoDB storage
- Simple REST API
- ESP32 integration

---

## Types of Changes

- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability fixes
