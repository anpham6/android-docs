=============
Local Storage
=============

Custom named user settings per framework can be saved to `local storage <https://developer.mozilla.org/docs/Web/API/Window/localStorage>`_ and reloaded across all pages in the same domain. Extensions are configured using the same procedure.

Framework
=========

.. code-block::
  :caption: Save

  squared.setFramework(android, { compressImages: true }, "android-example");

.. code-block::
  :caption: Load

  squared.setFramework(android, "android-example");

Output
======

.. code-block::
  :caption: Save

  await squared.copyTo("/path/project", {/* options saved with JSON.stringify */}, "copy-example", true); // Will overwrite and not merge with previously saved settings

.. code-block::
  :caption: Load

  // Local storage
  await squared.copyTo("/path/project", {/* options */}, "copy-example"); // Object.assign({ ...copy-example }, options)
  await squared.copyTo("/path/project", "copy-example"); // options = { ...copy_example }

  // External
  await squared.copyTo("/path/project", {/* options */}, "http://localhost:3000/copy-to/base-config.json"); // Object.assign({ ...base-config }, options)
  await squared.copyTo("/path/project", "http://localhost:3000/copy-to/base-config.json"); // options = { ...base-config }