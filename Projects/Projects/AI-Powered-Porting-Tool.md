---
title: "AI-Powered Package Porting Tool for the Arm Architectures"
subjects:
    - "CI-CD"
    - "ML"
    - "Migration to Arm"
requires-team:
    - "No"
platform:
    - "Servers and Cloud Computing"
    - "Laptops and Desktops"
    - "Mobile, Graphics, and Gaming"
    - "AI"
sw-hw:
    - "Software"
support-level: 
    - "Self-Service"
    - "Arm Ambassador Support"
publication-date: 30-05-2025
license: 
---

![research_on_arm](../../images/Research_on_arm_banner.png)

## Description

This project challenges students to build an intelligent automation tool for porting software packages — for use in domains such as [bioinformatic pipelines with Nextflow](https://github.com/arm-university/Arm-Projects-Labs/blob/main/PhD-Level/Bioinformatic-Pipeline-Analysis-INTERMEDIATE.md) or [statistics with R](https://github.com/arm-university/Arm-Projects-Labs/blob/main/PhD-Level/R-Arm-Community-Support-INTERMEDIATE.md).

Although most top Bioconda packages now support Linux/Arm, there's still a significant gap for native macOS on Apple Silicon, where many packages default to emulated x86 environments. Similarly, for the R community, Windows-on-Arm support for community created packages is lacking with many packages unable to build due to issues such as x86-specific code. 
Given the large number of community packages, applying manual patches is not only time-consuming but also inefficient, as many involve similar, repetitive adjustments—highlighting the need for a scalable, automated solution.
The goal is to build a sophisticated system (beyond simple shell scripts) that uses dependency graph analysis, machine learning, to:

- Identify unported packages
- Trace recursive dependency issues
- Recommend or auto-generate build recipes and steps
- Evaluate build success and reattempt intelligently
- Generate pull requests when confident of a fix. 
- For complex packages, offer guidance to developers on how to port them—for example, by suggesting tools like SSE2NEON for translating x86 SSE intrinsics.
- Be extensible to work with various  packaging systems and languages

🔬 Students will gain practical experience with CI/CD systems, Python packaging with bioconda, 

This project is an ideal blend of automation, machine learning, and systems programming — built with real-world impact in mind. The outcome could directly contribute to open source ecosystems and help bring cutting-edge bioinformatics tools to wider hardware audiences.

## Prerequisites

- Access to Apple Silicon either through the cloud or with Physical hardware
- Familiarity with Python, Bash and Nextflow
- Familiar with genomics or interest in computational biology. 
- Experience or willing to learn nf-core pipelines, Conda, BioConda and Docker/Singularity.


## Resources from Arm and our partners

- External Resource: [Example Porting Script for Bioconda](https://github.com/dslarm/bioconda-contrib-notes/tree/main), [Arm64 nf-core pipelines](https://github.com/ewels/nf-core-arm-discovery/tree/main) and [Bioconda package repository](https://bioconda.github.io/)

- Documentation: [nf-core documentation](https://nf-co.re/docs/)

- External Documentation: [Bioconductor Build Reports](https://bioconductor.org/checkResults/), Package installation results for [CRAN](https://www.r-project.org/nosvn/winutf8/ucrt3/CRAN_aarch64/install_out/) and [Bioconductor](https://www.r-project.org/nosvn/winutf8/ucrt3/BIOC_aarch64/install_out/) packages

- Dataset: [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions will result in preferential internal referrals to Arm Talent Acquisition (with digital badges for CV building).  And we are currently discussing with national agencies the potential for funding streams for Arm Developer Labs projects, which would flow to you, not us.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.