FROM ubuntu:bionic


RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade setuptools
RUN apt-get -y install git

RUN git clone https://github.com/irbalao/repositorio

WORKDIR repositorio/bookinfo/src/productpage
RUN pip3 install -r requirements.txt

EXPOSE 9080

CMD ["python3", "productpage_monolith.py", "9080"]
