# Project Documentation

## Overview

This project is a web application built using React and TypeScript, featuring a responsive design and a theme-aware user interface. The application includes various components, including a footer, and utilizes React Router for client-side routing. The project is designed to provide users with an intuitive and visually appealing experience while navigating through different sections of the application.

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Components](#components)
5. [Routing](#routing)
6. [Theming](#theming)
7. [Styling](#styling)
8. [Usage](#usage)
9. [Contributing](#contributing)
10. [License](#license)

## Technologies Used

- **React**: A JavaScript library for building user interfaces.
- **TypeScript**: A superset of JavaScript that adds static typing.
- **React Router**: A library for routing in React applications.
- **Tailwind CSS**: A utility-first CSS framework for styling.
- **SVG**: Scalable Vector Graphics for the application logo.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the dependencies:

   ```bash
   npm install
   Start the development server:
   ```

   ```bash
   npm start
   Open your browser and navigate to http://localhost:3000 to view the application.
   ```

## Project Structure
The project is organized into the following structure:

   ```
   /your-repo-name
   │
   ├── /public                # Public assets
   │   └── index.html        # Main HTML file
   │
   ├── /src                   # Source files
   │   ├── /assets            # Static assets (e.g., images, logos)
   │   ├── /components        # Reusable components (e.g., Footer)
   │   ├── /hooks             # Custom hooks (e.g., useTheme)
   │   ├── /pages             # Page components for routing
   │   ├── /styles            # Global styles (if any)
   │   └── index.tsx         # Entry point of the application
   │
   ├── package.json           # Project metadata and dependencies
   └── tsconfig.json          # TypeScript configuration
   ```

## Components
The application consists of several reusable components, including:

**Footer**: Displays the application logo and navigation links.  
**Header**: (if applicable) Displays the application title and navigation.  
**Other Page Components**: Various components representing different pages in the application (e.g., Home, Dashboard, Account).  

## Routing
The application uses React Router for client-side routing. The main routes typically include:

*  `/`: The root route, which renders the Home page.
*   `/dashboard`: The dashboard route, which renders the Dashboard page.
* `/account`: The Account route, which renders the Account management page

Routes are defined in the main application file (e.g., index.tsx or App.tsx).

## Theming
The application supports light and dark themes. The theme can be toggled using a custom hook (useTheme), which provides the current theme context to components. The components adjust their styles based on the selected theme.

## Styling
The project uses Tailwind CSS for styling. This utility-first CSS framework allows for rapid styling directly within the JSX code. Custom styles can also be added as needed.

## Usage
for usage guidelines of the application, refer [user-manual](./user-manual.md)
