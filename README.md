# docktrader

<!--- See https://shields.io for others or to customize this set of shields.  --->

![GitHub repo size](https://img.shields.io/github/repo-size/dennislwm/docktrader?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/dennislwm/docktrader?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/dennislwm/docktrader?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/dennislwm/docktrader?color=red&style=plastic)
![GitHub stars](https://img.shields.io/github/stars/dennislwm/docktrader?style=social)
![GitHub forks](https://img.shields.io/github/forks/dennislwm/docktrader?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/dennislwm/docktrader?style=social)
![GitHub followers](https://img.shields.io/github/followers/dennislwm?style=social)
<span class="badge-buymeacoffee"><a href="https://ko-fi.com/dennislwm" title="Donate to this project using Buy Me A Coffee"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg" alt="Buy Me A Coffee donate button" /></a></span>
<span class="badge-patreon"><a href="https://patreon.com/dennislwm" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>

## Table of Contents
- [docktrader](#docktrader)
  - [Table of Contents](#table-of-contents)
    - [About docktrader](#about-docktrader)
      - [Known Issues](#known-issues)
    - [Prerequisites](#prerequisites)
    - [Project Structure](#project-structure)
  - [WinPython (deprecated)](#winpython-deprecated)
    - [Usage](#usage)
  - [Docker as a Virtual Environment for Python](#docker-as-a-virtual-environment-for-python)
    - [Initialize Docker Container from Image](#initialize-docker-container-from-image)
    - [Running terminal in Docker Container](#running-terminal-in-docker-container)
    - [Run a stopped Docker Container](#run-a-stopped-docker-container)
    - [Stop Docker Container](#stop-docker-container)
    - [Remove Docker Container](#remove-docker-container)
    - [Reach Out!](#reach-out)

Python trading scripts running on Jupyter notebook.

---

### About docktrader

This docktrader project is used by me to create trading scripts because:

- Visual environment used to create reproducible backtesting results
- Python dependencies containerized to run on MacOS, Windows, Ubuntu

This repository can be used as a starting point for adding further scripts, such as Deep Learning, Machine Learning, etc.

---

#### Known Issues

Python packages pyfolio and quantstats does not install on WinPython.

Alternatively, we can run notebooks with the above packages on Google Colab.

---

### Prerequisites

This project is now running on a custom Docker image ([dennislwm/pynotebook](https://github.com/dennislwm/pynotebook)) and it has the following dependencies:

- [Anaconda 3](https://hub.docker.com/r/continuumio/anaconda3)
- [Python 3](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/)

These additional Python libraries are installed in the Jupyter notebook:
- [Backtrader](https://www.backtrader.com/)
- [scikit-learn](https://scikit-learn.org/)
- [seaborn](https://seaborn.pydata.org/)
- [statsmodels](https://www.statsmodels.org/)
- [TA-Lib](https://github.com/mrjbq7/ta-lib)

This project is NO longer running on WinPython (deprecated):

- [WinPython](https://winpython.github.io/)

---

### Project Structure

     docktrader/                                                           <-- Root of your project
       |- Dockerfile                                                       <-- Dockerfile of image (deprecated)
       |- README.md                                                        <-- This README markdown file
       +- config/                                                          <-- System configuration files go here
          |- iex.conf                                                      <-- Token file (.gitignore)
       +- data/                                                            <-- Data files go here
          +- 01raw/                                                        <-- Raw data files go here
             +- stockrow/                                                  <-- Downloaded files from StockRow.com go here
          +- 02interim/                                                    <-- Cleaned version of raw files go here
          +- 03model/                                                      <-- Data files to develop model go here
          +- 04trained/                                                    <-- Trained models go here
          +- 05output/                                                     <-- Model output files go here
          +- 06report/                                                     <-- Reports and input to frontend
       +- notebooks/                                                       <-- Jupyter notebooks go here
          |- 001import.ipynb                                               <-- Sample notebook to import Python libraries
          |- 002basic.ipynb                                                <-- Sample notebook for Python script 001basic.py
          |- 003sma.ipynb                                                  <-- Sample notebook for Python script 002sma.py
          |- 004iexfinance.ipynb                                           <-- iexfinance is an IEX Cloud Python SDK
          |- 005iexnews.ipynb                                              <-- Jupyter notebook to showcase IEX news
          |- 006iexpiece.ipynb                                             <-- Jupyter notebook to showcase IEX financial statments
          |- 006mathplot.ipynb                                             <-- Jupyter notebook to showcase IEX price charts
          |- 007pyex.ipynb                                                 <-- pyex is an alternative IEX Cloud Python SDK
          |- 008stockrow.ipynb                                             <-- StockRow is an alternative to IEX Cloud
          |- 009stockrow-excel.ipynb                                       <-- Download financial statements as Excel spreadsheets from StockRow
          |- 011deepspeech.ipynb                                           <-- Mozilla Deep Speech Transcriber in Python
          |- 012portfolio.ipynb                                            <-- Mean Variance Optimizer in Python
          |- 013summarize.ipynb                                            <-- Simple Summarizer with NLP in Python
          |- 014piece.ipynb                                                <-- PIECE analysis in Python
          |- 015hmm_market_behaviour.ipynb                                 <-- Clone of https://github.com/lamres/hmm_market_behavior
          |- 016pairs_trading_cryptocurrencies_strategy_catalyst.ipynb     <-- Clone of https://github.com/lamres/pairs_trading_cryptocurrencies_strategy_catalyst/blob/master/cointegration_analysis_cryptocurrencies.ipynb
          |- 017trendet.ipynb                                              <-- Clone of https://github.com/alvarobartt/trendet
          |- 018ErrorCls.ipynb                                             <-- Define custom Class exception in Python
          |- 019whatsapp_analysis.ipynb                                    <-- Whatsapp chat analysis (non-API) from text file
       +- src/                                                             <-- Python scripts that correspond to notebooks
          |- 001import.py                                                  <-- Sample notebook to import Python libraries
          |- 002basic.py                                                   <-- Sample script to show account balance
          |- 003sma.py                                                     <-- Sample script to backtest SMA strategy

---

## WinPython (deprecated)

### Usage

After installing [WinPython](https://winpython.github.io/) on your PC, go the installation folder and run the following file:

     > Jupyter Notebook.exe

This command opens a Jupyter Notebook web application in your browser.

---

## Docker as a Virtual Environment for Python

### Initialize Docker Container from Image

Type the following command in your terminal, e.g. Windows command prompt:

     > docker run --rm -v (notedir):/home:rw --name objDocktrader -p 8888:8888 -it dennislwm/pynotebook

Note: Substitute "(notedir)" with the path to your notebooks folder on your host computer, e.g. C:\DOCUMENT\NOTEBOOK

---

### Running terminal in Docker Container

If you require root access to the Docker container, add a suffix "bash" to the above docker run command as follows:

     > docker run -v (notedir):/home --name objDocktrader -p 8888:8888 -it dennislwm/pynotebook bash

---

### Run a stopped Docker Container

Type the following command in your terminal, e.g. Windows command prompt:

     > docker start -ia objDocktrader

---

### Stop Docker Container

Type the following command in your terminal, e.g. Windows command prompt:

     > docker container stop objDocktrader

---

### Remove Docker Container

Type the following command in your terminal, e.g. Windows command prompt:

     > docker container rm objDocktrader

---

### Reach Out!

Please consider giving this repository a star on GitHub.
