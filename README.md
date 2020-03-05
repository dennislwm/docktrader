# docktrader

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

This project is now running on WinPython (the previous Docker image has been deprecated):

- [WinPython](https://winpython.github.io/)

This project is built using Docker for Windows and it has the following dependencies (deprecated):

- [Anaconda 3](https://hub.docker.com/r/continuumio/anaconda3)
- [Python 3](https://www.python.org/)
- [Backtrader](https://www.backtrader.com/)
- [Jupyter Notebook](https://jupyter.org/)

---

### Project Structure

     docktrader/                             <-- Root of your project
       |- Dockerfile                         <-- Dockerfile of image
       |- README.md                          <-- This README markdown file
       +- config/                            <-- System configuration files go here
          |- iex.conf                        <-- IEX Finance conf file
       +- data/                              <-- Data files go here
          +- 01raw/                          <-- Raw data files go here
             +- stockrow/                    <-- Downloaded files from StockRow.com go here
          +- 02interim/                      <-- Cleaned version of raw files go here
          +- 03model/                        <-- Data files to develop model go here
          +- 04trained/                      <-- Trained models go here
          +- 05output/                       <-- Model output files go here
          +- 06report/                       <-- Reports and input to frontend
       +- notebooks/                         <-- Jupyter notebooks go here
          |- 001import.ipynb                 <-- Sample notebook to import Python libraries
          |- 002basic.ipynb                  <-- Sample notebook for Python script 001basic.py
          |- 003sma.ipynb                    <-- Sample notebook for Python script 002sma.py
          |- 004iexfinance.ipynb             <-- iexfinance is an IEX Cloud Python SDK
          |- 005iexnews.ipynb                <-- Jupyter notebook to showcase IEX news
          |- 006iexpiece.ipynb               <-- Jupyter notebook to showcase IEX financial statments
          |- 006mathplot.ipynb               <-- Jupyter notebook to showcase IEX price charts
          |- 007pyex.ipynb                   <-- pyex is an alternative IEX Cloud Python SDK
          |- 008stockrow.ipynb               <-- StockRow is an alternative to IEX Cloud
          |- 009stockrow-excel.ipynb         <-- Download financial statements as Excel spreadsheets from StockRow
          |- 011deepspeech.ipynb             <-- Mozilla Deep Speech Transcriber in Python
          |- 012portfolio.ipynb              <-- Mean Variance Optimizer in Python
          |- 013summarize.ipynb              <-- Simple Summarizer with NLP in Python
          |- 014piece.ipynb                  <--PIECE analysis in Python
       +- src/                               <-- Python scripts go here
          |- 001basic.py                     <-- Sample script to show account balance
          |- 002sma.py                       <-- Sample script to backtest SMA strategy

---

## WinPython

### Usage

After installing [WinPython](https://winpython.github.io/) on your PC, go the installation folder and run the following file:

     > Jupyter Notebook.exe

This command opens a Jupyter Notebook web application in your browser.

---

## Docker as a Virtual Environment for Python (deprecated)

### Build a new Docker Image

In the root folder, type the following command in your terminal, e.g. Windows command prompt:

     > docker image build -t (imagename) .

Substitute "(imagename)" with a custom name for your image, e.g. docktrader

---

### Initialize Docker Container from Image

Type the following command in your terminal, e.g. Windows command prompt:

     > docker run -v (notedir):/home --name objDocktrader -p 8888:8888 -it (imagename)

Substitute "(notedir)" with the path to your notebooks folder on your host computer, e.g. C:\DOCUMENT\NOTEBOOK

Note: If you require root access to the Docker container, add a suffix "bash" to the above docker run command as follows:

     > docker run -v (notedir):/home --name objDocktrader -p 8888:8888 -it (imagename) bash

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
