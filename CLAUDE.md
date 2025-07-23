# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a scientific research paper titled "Geometric Dark Energy from Spin-Torsion Cosmology: A Comprehensive Framework with Observational Validation" by Houston Golden. The project is a theoretical physics paper exploring dark energy through quantum gravitational effects in spin-torsion cosmology.

## Repository Structure

- `bigbounce.md` - Complete research paper content in Markdown format (~35,000 words)
- `index.html` - Interactive web presentation of the research paper with password protection
- `paper/` - Individual sections of the paper organized as separate Markdown files:
  - `00-abstract.md` through `11-acknowledgments.md`
  - `metadata.md` - Paper metadata
- `public/images/` - Scientific figures and illustrations (PNG format)
- `public/spreadsheets/` - Supporting data tables

## Development Environment

This is a static website project with no build system or package management. The main deliverable is `index.html` which presents the research paper in an interactive web format.

### Key Features of the Web Interface

- **Password Protection**: Uses session storage with password "houston"
- **Interactive Table of Contents**: Sidebar navigation with smooth scrolling
- **MathJax Integration**: Renders LaTeX mathematical expressions
- **Lightbox Image Viewer**: Click images to view in full screen
- **Responsive Design**: Mobile-friendly layout
- **Scientific Styling**: Academic paper formatting

### No Build Commands Required

This project does not use:
- Package managers (npm, yarn, etc.)
- Build tools (webpack, rollup, etc.)
- CSS preprocessors
- JavaScript frameworks

Simply open `index.html` in a web browser to view the paper.

## Content Organization

The paper is structured as a comprehensive theoretical physics research paper with:
- Mathematical derivations using LaTeX notation
- Scientific figures with detailed captions
- Extensive references to academic literature
- Systematic analysis and observational predictions
- Timeline for experimental validation

## Working with the Content

When editing the paper content:
- Mathematical expressions use LaTeX syntax within `$$` or `$` delimiters
- Figures are referenced as `public/images/figure_name.png`
- The HTML version in `index.html` should be kept in sync with `bigbounce.md`
- Maintain academic writing style and scientific rigor

## Contact Information

Author: Houston Golden
Email: houston@bamf.ai
LinkedIn: houstongolden