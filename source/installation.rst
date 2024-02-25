============
Installation
============

- NodeJS 14 :alt:`(Minimum)`

NPX
===

.. highlight:: bash

.. code-block::
  :caption: node_modules

  npm init
  npm i sqd-cli sqd-serve

  npx sqd init
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
  :caption: prod - 5.1.2

  git clone https://github.com/anpham6/squared
  cd squared
  git checkout 5.1.2

  npm install
  npm run build:all

  cd ..

  git clone https://github.com/anpham6/squared-express
  cd squared-express
  git checkout 3.1.1

  npm install
  npm run prod
  npm run deploy # deploy:yaml

  cd ../squared

  # squared.json
  node serve.js

.. code-block::
  :caption: dev - 5.2.0

  git clone https://github.com/anpham6/squared
  cd squared
  git checkout 5.2.0

  npm install
  npm run build:dev

  cd ..

  git clone https://github.com/anpham6/squared-express
  cd squared-express
  git checkout 3.2.0

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

  mkdir workspace
  cd workspace

  repo init -u https://github.com/anpham6/squared-repo -m 5.1.5.xml
  repo sync

.. rst-class:: installation-workspace

.. code-block::
  :caption: ~/workspace

  android-docs  chrome-docs  e-mc  pi-r  squared  squared-express

.. [#] https://source.android.com/docs/setup/download#installing-repo
.. [#] https://source.android.com/docs/setup/reference/repo