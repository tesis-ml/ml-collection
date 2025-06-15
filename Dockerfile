FROM jupyter/scipy-notebook

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]

RUN pip install seaborn matplotlib scikit-learn-extra
