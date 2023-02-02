FROM ubuntu:bionic

ENV GROUP_NUMBER=44
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade setuptools
WORKDIR /productpage
COPY . .
EXPOSE 9080
RUN pip3 install -r ./requirements.txt

RUN sed -i "s/Simple\sBookstore\sApp/Simple Bookstore App Equipo ${GROUP_NUMBER}/g" ./templates/productpage.html

CMD ["python3", "productpage.py", "9080"]
