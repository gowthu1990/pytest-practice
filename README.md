# pytest-practice

# Mastering Pytest: A Practical Guide for Students

Welcome to the **Mastering Pytest** repository! This is a comprehensive, hands-on guide designed to help you understand and master the powerful `pytest` framework. Whether you're a student new to testing or a professional looking to write more robust and efficient tests, this repository provides a clear, step-by-step path to becoming proficient in `pytest`.

Each folder in this repository corresponds to a specific topic, with code examples and exercises to reinforce your learning.

---

### **Topics Covered**

#### **1. Core Concepts: The Foundation of Pytest**

* **Introduction to `pytest`:** What is `pytest` and why is it the go-to framework for Python testing?
* **Installation:** How to set up your environment and get started.
* **Test Discovery:** The magic of `pytest` – how it finds your tests automatically.
* **Writing Your First Tests:** Simple test functions and the use of the `assert` statement.
* **Basic Test Execution:** Running your tests from the command line with `pytest`.
* **Organizing Tests:** Using test classes and modules to structure your test suite.

#### **2. Fixtures: Powering Setup and Teardown**

* **Understanding Fixtures:** The "why" and "how" of using fixtures for repeatable setup.
* **Function-level Fixtures:** Setting up resources for a single test.
* **Module-level Fixtures:** Sharing setup code across multiple tests in a file.
* **Session-level Fixtures:** Creating resources that last for the entire test run.
* **Autouse Fixtures:** Automatically applying a fixture to all tests in its scope.
* **Fixture Scopes and Dependencies:** Managing the lifecycle and relationships of your fixtures.

#### **3. Parametrization: Running Tests with Different Data**

* **The Problem:** Why you need to avoid writing repetitive tests.
* **Using `@pytest.mark.parametrize`:** A clean and efficient way to test a function with multiple inputs and expected outputs.
* **Parametrizing with Tuples and Dictionaries:** Structuring your data for clear test cases.

#### **4. Marks: Controlling Test Execution**

* **The `@pytest.mark` Decorator:** How to apply special behaviors to your tests.
* **Skipping Tests:** Using `skip` and `skipif` to avoid running certain tests under specific conditions.
* **Expected Failures:** Using `xfail` for tests that are not yet passing but are expected to in the future.
* **Custom Marks:** Creating your own marks to organize and filter tests.

#### **5. Advanced Topics & Best Practices**

* **The `conftest.py` File:** Sharing fixtures and configuration across your entire project.
* **Mocking and Patching:** Using `pytest-mock` to test code that interacts with external services or dependencies.
* **Command-Line Options:** Advanced usage of the `pytest` command for powerful filtering and reporting.
    * `-k`: Selecting tests by name.
    * `-m`: Running tests by mark.
    * `--cov`: Measuring test coverage with `pytest-cov`.
* **Custom Hooks:** Extending `pytest`'s functionality with custom hooks.

---

### **Getting Started**

1.  **Enabling pytest in VS Code settings.json file**
    ```json
    {
        "python.testing.pytestEnabled": true,
        "python.testing.unittestEnabled": false,
        "python.testing.pytestArgs": [
            "tests"
        ]
    }
    ```

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/gowthu1990/pytest-practice.git
    cd pytest-practice
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Tests:**
    ```bash
    pytest
    ```

Start exploring the folders to dive into the code and examples. Good luck on your journey to becoming a `pytest` expert!

---