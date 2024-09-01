<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="20%" alt="WALLHAVEN.PY-logo">
</p>
<p align="center">
    <h1 align="center">WALLHAVEN.PY</h1>
</p>
<p align="center">
    <em>Your wallpaper, your way, API-powered.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/git/license/vaproh/wallhaven.py?style=flat-square&logo=opensourceinitiative&logoColor=white&color=A931EC" alt="license">
	<img src="https://img.shields.io/git/last-commit/vaproh/wallhaven.py?style=flat-square&logo=git&logoColor=white&color=A931EC" alt="last-commit">
	<img src="https://img.shields.io/git/languages/top/vaproh/wallhaven.py?style=flat-square&color=A931EC" alt="repo-top-language">
	<img src="https://img.shields.io/git/languages/count/vaproh/wallhaven.py?style=flat-square&color=A931EC" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
</p>

<br>

<details><summary>Table of Contents</summary>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
    - [ Prerequisites](#-prerequisites)
    - [ Installation](#-installation)
    - [ Usage](#-usage)
    - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

</details>
<hr>

##  Overview

Wallhaven.py is a Python library designed to simplify interactions with the Wallhaven API. It provides a user-friendly interface for searching and retrieving high-resolution wallpapers, accessing user collections, and fetching random images. The library handles API requests, error handling, and JSON parsing, allowing developers to easily integrate Wallhavens vast library of wallpapers into their applications. Whether youre building a wallpaper management tool, a desktop background changer, or a creative project that requires high-quality imagery, Wallhaven.py offers a robust and efficient solution for accessing Wallhaven's extensive collection.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project utilizes a class-based architecture with a `WallhavenPY` class encapsulating API interactions. It leverages external libraries for HTTP requests and JSON parsing. |
| 🔩 | **Code Quality**  | The codebase demonstrates good readability and follows Python conventions. It includes clear variable names and comments, enhancing maintainability. |
| 📄 | **Documentation** | The repository includes basic documentation within the code itself, explaining the purpose of each file and key functions. However, more comprehensive documentation would be beneficial. |
| 🔌 | **Integrations**  | The project integrates with the Wallhaven API for retrieving wallpaper data. It utilizes external libraries like `requests` for HTTP requests and `urllib3` for secure communication. |
| 🧩 | **Modularity**    | The codebase is modular, with the `WallhavenPY` class encapsulating API interactions. This allows for easy reuse and extension of the functionality. |
| 🧪 | **Testing**       | The project includes a test suite (`test_wallhaven.py`) that utilizes mocking to validate API interactions and error handling. |
| ⚡️  | **Performance**   | The project's performance is likely dependent on the Wallhaven API's response time and network conditions. The codebase itself appears optimized for efficient API interactions. |
| 🛡️ | **Security**      | The project relies on the security measures provided by the `urllib3` library for secure communication. However, it's important to note that the API key should be handled securely to prevent unauthorized access. |
| 📦 | **Dependencies**  | Key dependencies include `requests`, `urllib3`, `certifi`, `idna`, and `charset-normalizer`. These libraries provide essential functionalities for HTTP requests, secure communication, and character encoding. |
| 🚀 | **Scalability**   | The project's scalability depends on the Wallhaven API's rate limits and the ability to handle increased traffic. The codebase itself appears well-structured for potential future scaling. |

---

##  Repository Structure

```sh
└── wallhaven.py/
    ├── errors.py
    ├── requirements.txt
    ├── test_wallhaven.py
    ├── usage.py
    └── wallhaven.py
```

---

##  Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| errors.py | The `errors.py` file defines a custom exception class named `WallhavenAPIError`. This exception is used to handle errors that occur when interacting with the Wallhaven API, providing a clear and specific way to manage API-related issues within the repositorys architecture. |
| requirements.txt | The `requirements.txt` file specifies the external Python libraries necessary for the Wallhaven API client to function correctly. These libraries provide essential functionalities like HTTP requests, URL parsing, and secure communication, enabling the client to interact with the Wallhaven API effectively. |
| test_wallhaven.py | This test suite thoroughly validates the functionality of the WallhavenPY class, ensuring its ability to handle successful API requests, various error scenarios, and specific search operations. It leverages mocking to simulate API responses and exceptions, guaranteeing robust and reliable interactions with the Wallhaven API. |
| usage.py | The `usage.py` file demonstrates the basic usage of the `WallhavenPY` class within the `wallhaven.py` repository. It showcases how to initialize the client, retrieve collections data, and perform searches with various parameters. |
| wallhaven.py | The `wallhaven.py` file provides a Python client for interacting with the Wallhaven API. It offers methods for searching wallpapers, retrieving wallpaper details, accessing user collections, and fetching random wallpapers. The client handles API requests, error handling, and JSON parsing, simplifying interactions with the Wallhaven API. |

</details>

---

##  Getting Started

###  Prerequisites

**Python**: `version 3.12.5`

###  Installation

Build the project from source:

1. Clone the wallhaven.py repository:
```sh
❯ git clone https://git.vaproh.xyz/vaproh/wallhaven.py
```

2. Navigate to the project directory:
```sh
❯ cd wallhaven.py
```

3. Create an virtual envirourment:
```sh
❯ python -m venv .venv 
```

4. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

###  Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

###  Tests

Execute the test suite using the following command:

```sh
❯ python -m unittest discover
```

---

##  Project Roadmap

- [ ] **`Task 1`**: <strike>Make it more secure?</strike>

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://git.vaproh.xyz/vaproh/wallhaven.py/issues)**: Submit bugs found or log feature requests for the `wallhaven.py` project.
- **[Submit Pull Requests](https://git.vaproh.xyz/vaproh/wallhaven.py/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://git.vaproh.xyz/vaproh/wallhaven.py/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your git account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://git.vaproh.xyz/vaproh/wallhaven.py
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to git**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

---

##  License

This project is protected under the [GNU GPL](https://www.gnu.org/licenses/gpl-3.0.en.html) License. For more details, refer to the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file.

---

##  Acknowledgments

- Thanks to this [Article](https://www.pretzellogix.net/2021/12/08/how-to-write-a-python3-sdk-library-module-for-a-json-rest-api/) for guiding me. 

---
