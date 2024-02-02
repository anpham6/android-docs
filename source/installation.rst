============
Installation
============

* NodeJS 14

NPX
===

.. code-block:: shell
  :caption: node_modules

  npm init
  npm i sqd-cli sqd-serve

  npx sqd init
  npx sqd serve

.. code-block:: shell
  :caption: local

  npm init
  npm i sqd-cli sqd-serve

  npx sqd init --public --local-serve
  node serve.js

.. code-block:: shell
  :caption: without sqd-cli

  npm init
  npm i squared sqd-serve

  mkdir dist html
  cp -r ./node_modules/squared/dist/* ./dist
  cp ./node_modules/squared/html/* ./html # optional
  cp ./node_modules/sqd-serve/config/json/* .

  npx serve

GitHub
======

.. code-block:: shell
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
  npm run deploy

  cd ../squared

  # squared.json
  node serve.js

.. code-block:: shell
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
  npm run deploy:config

  cd ../squared

  # squared.json
  node serve.js