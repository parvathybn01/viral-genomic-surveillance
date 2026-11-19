:::writing{variant="document" id="84621"}
# 🧬 VIGESORA
### AI-Assisted Viral Genomic Surveillance and Outbreak Risk Assessment Platform

*Understanding Viral Genomes. Supporting Genomic Surveillance.*

VIGESORA is a prototype web application designed to simplify viral genomic sequence analysis, with a primary focus on viral variant classification from FASTA-formatted genome sequences.

The platform brings sequence upload, input validation, quality assessment, analysis-result presentation, and reporting into a unified interface. It also provides a public-health information section for users exploring viral genomic surveillance.

## ✨ Key Features

- **FASTA File Upload:** Upload viral genomic sequences in FASTA format.
- **Sequence Validation:** Check FASTA headers, sequence availability, nucleotide symbols, and minimum sequence length.
- **Sequence Quality Assessment:** Calculate sequence length, ambiguous-base count, ambiguous-base percentage, and GC content.
- **Variant Classification Workflow:** Provides a structured workflow for presenting variant classification results.
- **Mutation Analysis:** Included as a supplementary experimental component for examining differences against reference sequences.
- **Analysis History:** Maintain analysis history within the current session.
- **Report Generation:** Export supported analysis results in JSON format.
- **Public Health Watch:** Access curated public-health information and relevant resources.
- **Help and Researcher Interface:** Provides guidance and a dedicated sequence-analysis workflow.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Backend API | Flask (integration under verification) |
| Data Handling | Pandas |
| API Communication | Requests |
| Input Format | FASTA |
| Output Format | JSON |

## 🏗️ System Workflow

1. The user uploads a viral genome sequence in FASTA format.
2. The application validates the sequence and checks its basic structure.
3. Sequence-quality metrics are calculated and displayed.
4. The analysis workflow is designed to communicate with a Flask backend for variant classification.
5. Available results are presented through an interactive interface.
6. Users can export supported results as JSON reports.

## 🔬 Project Focus

VIGESORA prioritises viral variant classification, with reference-based mutation analysis as a supplementary component.

The project explores how machine-learning approaches and bioinformatics workflows can be brought together to make genomic analysis more accessible.

## 📌 Current Development Status

VIGESORA is a working frontend prototype with implemented FASTA validation, sequence-quality calculations, demo-result presentation, JSON report export, and session-level history.

The live backend/model integration and independent evaluation of variant classification remain under development and verification. Mutation analysis is experimental and requires further validation. The platform does not currently provide validated outbreak-risk predictions or live epidemiological surveillance.

## 🏆 Project Achievement

**Project Course Evaluation: 98/100**

## 👩‍💻 Project Team

- **Shivani S.**
- **Parvathy B. Nair**
- **Varsha S. Kumar**

**Project Guide:** Ms. Nimina George

**Institution:** Chinmaya Vishwa Vidyapeeth

**Department:** Computer Science and Engineering (Artificial Intelligence and Machine Learning)

---

*VIGESORA — Connecting Computer Science, Bioinformatics, and Public Health.*
:::
