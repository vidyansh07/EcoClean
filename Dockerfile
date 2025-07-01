FROM public.ecr.aws/lambda/python:3.10

COPY src/API ${LAMBDA_TASK_ROOT}

COPY src/API/requirements.txt .

RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" -U --no-cache-dir

# RUN pip install -r requirements.txt

# ENTRYPOINT ["poetry", "run", "python", "index.py"]
CMD ["app.index:handler"]