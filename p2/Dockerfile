FROM ubuntu:bionic
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade setuptools
RUN apt-get -y install git
RUN git clone https://github.com/irbalao/repositorio
EXPOSE 9080
CMD ["/usr/bin/python3", "/home/ignargb/repositorio/bookinfo/src/productpage/productpage_monolith.py"]
