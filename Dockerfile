FROM public.ecr.aws/lambda/python:3.9

RUN yum install make -y

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install app
WORKDIR ${LAMBDA_TASK_ROOT}
COPY app ./


CMD ["app.lambda_handler"]