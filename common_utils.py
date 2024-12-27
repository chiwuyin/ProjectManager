conda env export --no-builds > environment.yml
conda env export --name my_env > my_env.yml
conda env export > environment.yml
conda env create -f environment.yml


pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple some-package
python -m pip install --upgrade pip
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

shell:startup


