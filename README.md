# Open-Science-Practices
[![DOI](https://zenodo.org/badge/599046489.svg)](https://zenodo.org/badge/latestdoi/599046489)

Open Science elective subject practices at UPM Gonzalo Romeral Álvarez -- 2023


-Connect to the host

-Use the client to retrieve the XML files of our 10 papers

-Generate output: Draw a word cloud of keywords based on the abstract information. Create a visualization that shows the number of figures per article. Create a list of links found in each document.

#Pre-installation
- Python: https://www.python.org/downloads/
- Docker: https://www.docker.com/products/docker-desktop/
- Pip: To install libraries in Python, here's a tutorial on how to download it: https://python-poetry.org/docs/#installing-with-the-official-installer
- Python dependencies:
    -grobid_Client
    -Beautiful Soup
    -lxml
    -bs4
    -wordcloud  
    -matplotlib
    -poetry
    -unittest
    
- Grobid Docker server, once Docker is installed, run the following commands:
   * docker pull lfoppiano/grobid:0.7.2
   * docker run --rm -p 8070:8070 -p 8081:8071 lfoppiano/grobid:0.7.2   
- Additional dependencies of the above libraries
   Preferred operating system: Windows 7+

#Execution
- Generate your own environment through these steps:
   * Open the command prompt and run previously installed poetry
   * Create a new project with poetry new <name>
   * Add all dependencies explained in the Python dependencies section with the command poetry add <library_name>
   * Activate the poetry shell and all libraries
   * Run our script with poetry run python myscript.py
   * Once the process of the script is completed, deactivate the shell with deactivate or exit
- Execute the Dockerfile, and inside there are instructions on how to run the script
- To check that everything has been installed properly, enter http://localhost:8070/ and if everything is working properly, our client should be running 
- Run the grobid_2.1.py script in our environment using Python 
- It will ask for a directory, and we must select the directory where we have the PDFs. If the directory doesn't have PDFs, an error will occur, and the script must be run again.
- In this version, the XML files will be saved in the same directory. For another version, the output directory can be chosen.
- Finally output values will be host in the actual working directory

If there are any issues, I can solve them if informed in advance - Tested with XMLs in the environment and it works, it remains to be tested directly with PDFs. Generate our environment or run the script thanks to the Docker image (not fully tested).
