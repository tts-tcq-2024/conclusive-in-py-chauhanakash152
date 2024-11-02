# Refactoring legacy code

Legacy code can be complex. It often starts simple, but collects complexity as the product and its customers evolve.

This repository has legacy code in it. Let's refactor to enable evolution without adding complexity.

## About this repository

The objective of the code is to monitor battery temperature and prevent damage:

- Classify the temperature measurement as being too high or too low. This classification depends on the type of cooling. With active cooling, the battery can reach higher temperatures before taking action.
- Transmit the classification to take action: When the system has a controller, send the classification to it. In the absence of a controller, send the classification via email. In this project, the transmission is 'simulated' by printing on the console.

The [GitHub Actions](https://docs.github.com/en/actions) in this project implement several workflows:

- No Duplications: Fails on finding duplication of 3 lines or more. There are no duplications, so this passes.
- Limit complexity: The limit per function is set at 3 and it's currently failing
- Build and Run: Runs the tests. It's passing currently, but there are hardly any tests. You need to add more.
- Enter Reflections: Replace the `_enter` in the **Reflections** section below, within this file. This workflow fails till you replace it with your impressions.

As with any legacy, have a look at the code to understand it better.

The 'Build and Run' workflow stores coverage-data as an artifact in the workflow run. You can download it from GitHub Actions.

## The refactoring task

Cyclomatic complexity is high in a few places. This indicates potential to steadily increase, as customers ask for changes and new features. Reduce the cyclomatic complexity. In future, it must be possible to add new features with less code-changes and re-testing.

Code coverage is low, because the test code is incomplete. Write more tests to take care of the variations. Track and improve the coverage.

Uncovered lines indicate an opportunity to write tests. Complex and repetitive tests indicate opportunity to simplify the code.

> Caution: High coverage doesn't indicate absence of bugs!

## Reflections

This section is about your regular work / project, not about the code in this repository.

Think about guiding refactoring-work in your regular/project teams. Think of the day-to-day work done in your team, and improving the quality of code.

You have seen a few workflows in this repository. They are quality-gates to prevent duplication, control complexity and prove functionality. Do you think some of them have potential to guide code-improvements in your team?
yes

During the next four weeks, what improvement do you plan in your code-quality practice? (in your regular work, not in this repository!)
# Code Quality Improvement Plan

During the next four weeks, I plan to focus on several key improvements in my code-quality practices:

1. **Enhanced Unit Testing**  
   I will adopt a more rigorous approach to unit testing, ensuring that all new features and bug fixes are accompanied by comprehensive tests. This includes writing tests that cover edge cases and using Test-Driven Development (TDD) for new features to catch potential issues early.

2. **Code Reviews**  
   I intend to participate more actively in code reviews, both as a reviewer and as a submitter. I will seek feedback on my code from peers and provide constructive feedback on theirs. This will help identify potential issues and promote best practices within the team.

3. **Static Code Analysis**  
   I will implement static code analysis tools (like Pylint or Flake8 for Python) in my workflow to automatically catch common issues, enforce coding standards, and improve overall code readability.

4. **Documentation Improvements**  
   I plan to enhance my code documentation by writing clearer docstrings and comments. This will not only help others understand my code but also serve as a useful reference for future development.

5. **Refactoring**  
   I will prioritize refactoring areas of the codebase that are overly complex or hard to maintain. This will include breaking down large functions into smaller, more manageable ones, aiming for a cyclomatic complexity below 3 when possible.

6. **Learning and Sharing**  
   I will dedicate time to learn about new tools and methodologies related to code quality and share my findings with my team. This could involve introducing them to new testing frameworks or code quality tools that could benefit our workflows.

By focusing on these areas, I aim to improve the maintainability, reliability, and overall quality of my code, which will ultimately lead to better software products.
