============
Installation
============

- NodeJS 14 (*Minimum*)

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
  :caption: local

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