=====
Types
=====

*ESM* compatible :target:`stand-alone` typings are available as of **squared 5.5**.

Installation
============

.. code-block:: bash

  npm i squared-types

.. note:: Dual installations with local typings are not supported such as within the **squared** repository.

tsconfig.json
=============

.. code-block::
  :caption: Required
  :emphasize-lines: 6

  {
    "compilerOptions": {
      "target": "es2022",
      "module": "es6",
      "lib": ["dom"],
      "typeRoots": ["node_modules/squared-types"]
    }
  }

You can do the same thing with **squared-express 4.0** using :target:`typeRoot` ``node_modules/squared-express`` and the :target:`UMD` global ``sqex``.