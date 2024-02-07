======
Chrome
======

The default settings were optimized for creating static web pages with `E-mc <https://e-mc.readthedocs.io>`_. Any customizations are usually the ``output`` properties.

Interface
=========

.. code-block:: typescript

  import type { UserResourceSettings } from "./interface";

  interface UserResourceSettings {
      excludePlainText?: boolean;
      webSocketPort?: number;
      webSocketSecurePort?: number;
  }

Example usage
=============

.. code-block:: typescript
  :caption: Global (bundle)

  squared.settings = {
    pierceShadowRoot: true,
    builtInExtensions: [], // Called for every local asset (ext.processFile)
    showErrorMessages: false,
    webSocketPort: 80, // Used with watch
    webSocketSecurePort: 443,
    outputDocumentHandler: "chrome",
    /* Same as android */
    outputEmptyCopyDirectory: false,
    outputSummaryModal: false,
    outputTasks: {
      "*.js": [{ handler: "gulp", task: "minify" }, { handler: "gulp", task: "beautify" }]
    },
    outputWatch: { "*": true },
    outputArchiveName: "chrome-data",
    outputArchiveFormat: "zip",
    outputArchiveCache: false
  };

.. code-block:: typescript
  :caption: Global (query)

  squared.settings = {
    excludePlainText: true, // HTMLElement + SVGElement
    createElementMap: true
  };

.. code-block:: typescript
  :caption: Global (unused)

  squared.settings = {
    preloadImages: false,
    preloadFonts: false,
    preloadLocalFonts: false,
    preloadCustomElements: false
  };