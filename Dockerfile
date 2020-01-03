#
# Example:
#   CMD> docker run -v <hostdir>:<dockerdir> --name <customname> -e DISPLAY=$DISPLAY -it <imagename>:<tag>
#

# Assert Anaconda 64-bit
FROM continuumio/anaconda3

# Assert Pip install
CMD [ "pip", "install", "notebook" ]
CMD [ "opt/conda/bin/pip", "install", "backtrader[plotting]" ]
CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root" ]

# Assert Open port
EXPOSE 8888