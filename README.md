# Calculator Project

## Overview
This project implements an **advanced calculator** in Python, supporting basic arithmetic operations, square root, powers, modulus, factorial, trigonometric functions, and logarithms. It includes:

- **Logging** of all operations to a file  
- **Command-Line Interface (CLI)** for interactive use  
- **Unit tests** with `pytest`  
- **Continuous Integration (CI/CD)** using Jenkins  

This project is ideal for practicing **unit testing**, **exception handling**, and **automation testing** with CI/CD pipelines.

---

## Files
- **calculator.py** – Contains the implementation of calculator functions with logging.  
- **calculator_cli.py** – CLI interface for interactive use.  
- **test_calculator.py** – Contains unit tests for all calculator functions using pytest.

---

## Calculator Functions

### 1. `add(a, b)`
- **Purpose:** Returns the sum of two numbers  
- **Example:**  
```python
add(2, 3)  # returns 5
add(-1, 1) # returns 0
```

### 2. `subtract(a, b)`
- **Purpose:** Returns the difference between two numbers  
- **Example:**  
```python
subtract(5, 3)  # returns 2
subtract(0, 5)  # returns -5
```

### 3. `multiply(a, b)`
- **Purpose:** Returns the product of two numbers.  
- **Input:** Two numbers (`a` and `b`).  
- **Output:** Product of `a` and `b`.  
- **Example:**  
```python
multiply(3, 4)  # returns 12
multiply(-2, 5) # returns -10
```

### 4. `divide(a, b)`
- **Purpose:** Returns the result of dividing `a` by `b`.  
- **Input:** Two numbers (`a` and `b`).  
- **Output:** Result of `a / b`.  
- **Edge Case:** Raises a `ValueError` if `b` is 0.  
- **Example:**  
```python
divide(10, 2)  # returns 5
divide(5, 2)   # returns 2.5
divide(10, 0)  # raises ValueError: Cannot divide by zero
```

### 5. `sqrt(a)`
- **Purpose:** Returns the square root of a number.  
- **Input:** A number `a`.  
- **Output:** Square root of `a`.  
- **Example:**  
```python
sqrt(4)   # returns 2
sqrt(16)  # returns 4
```

### 6. `power(a, b)`
- **Purpose:** Returns `a` raised to the power of `b`  
- **Example:**  
```python
power(2, 3)   # returns 8
power(5, 0)   # returns 1
power(4, 0.5) # returns 2.0
```

### 7. `modulus(a, b)`
- **Purpose:** Returns the remainder of `a` divided by `b`  
- **Example:**  
```python
modulus(10, 3)  # returns 1
modulus(20, 7)  # returns 6
modulus(-10, 3) # returns 2
```

### 8. `factorial(a)`
- **Purpose:** Returns the factorial of a non-negative integer `a`  
- **Edge Case:** Raises a `ValueError` if `a` is negative  
- **Example:**  
```python
factorial(5)  # returns 120
factorial(0)  # returns 1
factorial(-3) # raises ValueError
```

### 9. `sin(a)`
- **Purpose:** Returns the sine of an angle in degrees  
- **Example:**  
```python
sin(0)    # returns 0.0
sin(90)   # returns 1.0
sin(180)  # returns 0.0
```

### 10. `cos(a)`
- **Purpose:** Returns the cosine of an angle in degrees  
- **Example:**  
```python
cos(0)    # returns 1.0
cos(90)   # returns 0.0
cos(180)  # returns -1.0
```

### 11. `log(a, base=10)`
- **Purpose:** Returns the logarithm of a number with a specified base (default is 10)  
- **Edge Case:** Raises a `ValueError` if `a <= 0`  
- **Example:**  
```python
log(100)        # returns 2
log(8, 2)       # returns 3
log(math.e, math.e)  # returns 1
```
## Running the Calculator CLI

You can interact with the advanced calculator using the command-line interface (CLI) provided in `calculator_cli.py`.

### Steps

1. **Open Terminal** and navigate to the project directory:

```bash
cd path/to/project
```
2. **Run the CLI**
```bash
python calculator_cli.py
```
3. **Follow the prompts:** 
- Enter the operation you want to perform: add, subtract, multiply, divide, sqrt, power, modulus, factorial, sin, cos, log. 
- Enter the required number(s) when prompted. 
- The result will be displayed in the terminal.

### Example CLI Session
```bash
Welcome to the Calculator CLI!
Operations: add, subtract, multiply, divide, sqrt, power, modulus, factorial, sin, cos, log
Enter operation: add
Enter first number: 5
Enter second number: 3
Result: 8
```
### Notes
- The CLI uses the same functions as `calculator.py`, so all **logging** and **error handling** are applied.  
- Invalid inputs or operations will display an **error message**.  
- For logarithms, if only one number is provided, the **default base 10** is used.


# Advanced Calculator Project Testing

The project uses `pytest` to ensure that all calculator functions work correctly. Each function has a corresponding test in `test_calculator.py`.

## Test Functions

- **`test_add()`** – Checks addition for positive and negative numbers  
- **`test_subtract()`** – Checks subtraction, including negative results  
- **`test_multiply()`** – Checks multiplication with positive and negative numbers  
- **`test_divide()`** – Checks division for normal cases and ensures division by zero raises an error  
- **`test_sqrt()`** – Checks square root calculation  
- **`test_power()`** – Checks exponentiation including zero, negative, and fractional powers  
- **`test_modulus()`** – Checks modulus operations with positive and negative numbers  
- **`test_factorial()`** – Checks factorial including zero and negative error handling  
- **`test_sin()`** – Checks sine values for known angles  
- **`test_cos()`** – Checks cosine values for known angles  
- **`test_log()`** – Checks logarithms with default and custom bases


## How to Run tests Locally

1. **Install dependencies**  
   ```bash
   pip install pytest
   ```

2. **Run tests**
   ```bash
   pytest test.py
   ```
Pytest will execute all test functions and display results.
Passing tests indicate the calculator functions are working correctly.

## Running in Jenkins

You can automate testing of this calculator project using Jenkins.

### 1. Prerequisites

- Jenkins installed  
- Python 3 installed and accessible in Jenkins’ PATH  
- Git installed and project pushed to a GitHub repository  
- `pytest` installed in the environment Jenkins will use  

### 2. Create a Jenkins Job

1. Open Jenkins → **New Item** → Enter a job name → **Freestyle Project** → OK  
2. In **Source Code Management**, select Git and enter your repository URL  
3. Specify the branch to build (e.g., `main`)

### 3. Add Build Steps

In the **Build** section → **Execute shell**, add the following:

```bash
# Navigate to workspace folder
cd "$WORKSPACE"

# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

# Install pytest
pip install pytest

# Run tests and generate JUnit XML report
pytest test_calculator.py --junitxml=results.xml
```

> Tip: Ensure there are no spaces in the workspace folder path, or wrap paths in quotes.  

### 4. Optional: Publish Test Results

1. Go to **Post-build Actions** → **Publish JUnit test result report**  
2. Enter `results.xml` as the test report path  

Jenkins will display test results after each build.  

### 5. Build the Job

Click **Build Now**.  
Jenkins will fetch the code, set up the environment, run tests, and display results.  

### Purpose

- Demonstrates basic Python programming with functions  
- Provides practice with unit testing and exception handling  
- Can be integrated into CI/CD pipelines like Jenkins for automated testing  
- Prepares for future projects that require automated testing and continuous integration



### Jenkins Test Results

When the Jenkins job runs, it automatically sets up the Python environment, installs dependencies, and executes all tests with `pytest`.  
If all calculator functions work correctly, the build will pass and Jenkins will display the results.

Below is a screenshot of a successful Jenkins test run:
![Screenshot of Jenkins Setup](images/screenshot_2025-09-26.png)


## Continuous Integration: Automatic Builds on GitHub Push

This section shows how to configure **automatic Jenkins builds** whenever you push changes to the GitHub repository.

---

### 1. Jenkins Setup for GitHub Webhooks

1. Open your Jenkins dashboard → **New Item** → Freestyle Project → Enter a name → OK  
2. In **Source Code Management**, select **Git** and enter your repository URL  
3. Specify the branch to build (e.g., `main`)  

---

### 2. Build Triggers

1. Go to the **Build Triggers** section  
2. Check **GitHub hook trigger for GITScm polling**  

> This allows Jenkins to automatically trigger a build when a push event occurs in GitHub.

---

### 3. Using Ngrok for Local Jenkins Testing

- Ngrok exposes your local Jenkins server to the public internet via a temporary URL.  
- Start ngrok pointing to your local Jenkins port (default 8080):

```bash
ngrok http 8080
```
- Ngrok will provide a public HTTPS URL, e.g., https://alfredia-pentamerous-cecilia.ngrok-free.dev.
- Use this URL when creating a GitHub webhook to trigger builds on code pushes.
- Keep ngrok running during development to ensure GitHub can reach your Jenkins server.

---

### 4. Configure GitHub Webhook

1. Open your repository on GitHub → **Settings** → **Webhooks** → **Add webhook**  
2. **Payload URL:** `https://<your-jenkins-domain>/github-webhook/`  
   - If using ngrok for local testing, it would be like: `https://abcdef.ngrok-free.dev/github-webhook/`  
3. **Content type:** `application/json`  
4. **Which events would you like to trigger this webhook?** → Choose **Just the push event**  
5. Click **Add webhook**  

---

### 5. Jenkins Build Step

In your Jenkins project → **Build** → **Execute shell**, add:

```bash
# Navigate to workspace
cd "$WORKSPACE"

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pytest

# Run tests and generate report
pytest test_calculator.py --junitxml=results.xml

