============
Installation
============

- NodeJS 16 :alt:`(Minimum)`

NPX
===

.. highlight:: bash

.. code-block::
  :caption: node_modules

  npm init
  npm i sqd-cli sqd-serve

  npx sqd init  # --serve-only
  npx sqd serve

.. code-block::
  :caption: local (dev)

  npm init
  npm i sqd-cli sqd-serve

  npx sqd init --public --local-serve
  node serve.js

.. code-block::
  :caption: without sqd-cli

  npm init
  npm i squared sqd-serve

  mkdir dist html
  cp -r ./node_modules/squared/dist/* ./dist
  cp ./node_modules/squared/html/* ./html     # optional
  cp ./node_modules/sqd-serve/config/json/* . # yaml

  npx serve

GitHub
======

.. code-block::
  :caption: prod - master

  git clone https://github.com/anpham6/squared
  cd squared
  git checkout master

  npm install
  npm run build:all

  cd ..

  git clone https://github.com/anpham6/squared-express
  cd squared-express
  git checkout master

  npm install
  npm run prod
  npm run deploy # deploy:yaml

  cd ../squared

  # squared.json
  node serve.js

.. code-block::
  :caption: dev - 5.4.0

  git clone https://github.com/anpham6/squared
  cd squared
  git checkout 5.4.0

  npm install
  npm run build:dev

  cd ..

  git clone https://github.com/anpham6/squared-express
  cd squared-express
  git checkout 3.4.0

  npm install
  npm run dev
  npm run deploy:config # deploy:config:yaml

  cd ../squared

  # squared.json
  node serve.js

Repo
====

.. code-block::
  :caption: Install [#]_

  export REPO=$(mktemp /tmp/repo.XXXXXXXXX)
  curl -o ${REPO} https://storage.googleapis.com/git-repo-downloads/repo
  gpg --recv-keys 8BB9AD793E8E6153AF0F9A4416530D5E920F5C65
  curl -s https://storage.googleapis.com/git-repo-downloads/repo.asc | gpg --verify - ${REPO} && install -m 755 ${REPO} ~/bin/repo

.. code-block::
  :caption: Usage [#]_

  mkdir workspaces
  cd workspaces

  repo init -u https://github.com/anpham6/squared-repo -m latest.xml
  repo sync

.. code-block::
  :caption: Ruby (alternate) [#]_

  mkdir workspaces
  cd workspaces            # REPO_ROOT

  curl -o Rakefile https://raw.githubusercontent.com/anpham6/squared/5.4.0/Rakefile

  # REPO_DOCS=1 (venv)
  rake -T                  # List tasks

  # REPO_BUILD={dev,prod}
  # FAIL_BUILD=1
  rake repo:init           # nightly
  # OR
  rake repo:init[latest]
  # OR
  REPO_MANIFEST=latest rake repo:init

.. rst-class:: installation-workspace

.. code-block::
  :caption: ~/workspaces

  android-docs  chrome-docs  e-mc  pi-r  squared  squared-express

Docker
------

.. code-block::

  curl -o Dockerfile https://raw.githubusercontent.com/anpham6/squared/5.4.0/Dockerfile

  # NODE_TAG=latest
  # RUBY_VERSION=2.4.0-3.3.0
  # PIPE_FAIL=0
  # DOCS=1
  docker build -t squared --build-arg MANIFEST=prod --build-arg BUILD=prod .

  # Express
  docker run -it --name express --rm -p 80:80 \
    --mount type=bind,src=${PWD},dst=/workspaces/squared/.config \
    --mount type=bind,src=${PWD}/html,dst=/workspaces/squared/www \
    squared

  # Terminal
  docker run -it --name debian squared /bin/bash # irb

GitHub Codespaces
-----------------

- `Create <https://github.com/codespaces/new?hide_repo_select=true&ref=5.4.0&repo=162848626&skip_quickstart=true>`_

.. code-block::

  sudo ./scripts/repo-install.sh

  # NODE_INSTALL=pnpm
  REPO_ROOT=/workspaces rake repo:init[0.11.x]

  rake repo:sync
  # OR
  rake emc:checkout:force[0.11.0]    # once
  rake pir:checkout:force[0.9.0]
  rake express:checkout:force[3.4.0]
  rake pull

.. [#] https://source.android.com/docs/setup/download#installing-repo
.. [#] https://source.android.com/docs/setup/reference/repo
.. [#] https://www.ruby-lang.org/en/documentation/installation (2.4/3.0)