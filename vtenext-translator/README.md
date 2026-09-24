# vtenext-translator (`packageTranslator-reghack`)

A specialized Python utility and installable package developed to automate and streamline the generation of localized language packs for **vtenext CRM**.

Originally engineered while working at a wind park, this tool combines automated machine translation via the Google Translator API with manual dictionary overrides and chunked data management to efficiently translate large arrays of CRM strings.

---

## Architecture & Core Features

* 🌐 **Hybrid Translation Engine:**
    * Automatically processes string arrays using the Google Translator API.
    * Merges automated translations with curated manual dictionaries (`dict-vol*.json`) to ensure accurate domain-specific terminology for the CRM.


* 🗂️ **Dictionary & Chunk Management:**
    * Breaks down massive language datasets into manageable chunks (`bg.chunks.json`, `en.chunks.json`) and structured multi-volume dictionary sets (`dict-vol1.json` through `dict-vol7.json`).
    * Supports dictionary compilation and helper tools via `dictmaker.py`.


* 📦 **Packaged Python Library:**
    * Structured as a reusable package (`packageTranslator`) with build configurations, wheels (`.whl`), and source distributions (`.tar.gz`).
    * Includes environment configuration assets for network routing and proxies (`inc/proxyes.json`, `inc/service_urls.json`).



---

## Project Structure

```text
vtenext-translator/
├── build/                      # Compiled package build outputs
├── dist/                       # Python distribution archives (.whl and .tar.gz)
├── inc/                        # Configuration files (proxies and service URLs)
├── packageTranslator/          # Core package source code
│   ├── dictmaker.py            # Dictionary generation and dataset chunking
│   ├── translator.py           # Core translation pipeline and API logic
│   └── translator2.py          # Alternative translation workflow handler
├── packageTranslator_reghack.egg-info/ # Package metadata and dependencies
├── tests/                      # Test suites and translation datasets
│   ├── dictionary/             # Manual translation volumes (vol1 to vol7)
│   ├── dictionary-worked/      # Verified and processed dictionary archives
│   └── test_translator.py      # Unit and integration test suite
├── LICENSE                     # MIT License file
├── README.md                   # Project documentation
└── setup.py                    # Package installation and setup configuration

```

---

## Tech Stack & Libraries

* **Language:** Python 3 (>=3.8.2)
* **Packaging & Distribution:** Setuptools, wheel distribution formats
* **Data Processing:** JSON-based chunking and structured dictionary volumes
* **API Integration:** Google Translator API with configurable proxy and endpoint support (`inc/`)