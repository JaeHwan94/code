FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y --no-install-recommends python3.6 python3.6-dev python3-pip
COPY ./requirement.txt /app/requirement.txt
WORKDIR /app
RUN python3.6 -m pip install pip --upgrade
RUN pip3 install -r requirement.txt
COPY . /app
CMD [ "python3", "Member_Check.py" ]
