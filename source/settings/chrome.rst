======
Chrome
======

The default settings were optimized for creating static web pages with :external+chrome:doc:`E-mc <index>`. Any customizations are usually the ``output`` properties.

Interface
=========

.. code-block:: typescript

  interface UserResourceSettings {
      excludePlainText?: boolean;
      webSocketPort?: number;
      webSocketSecurePort?: number;
  }

Example usage
=============

.. code-block::
  :caption: Global (bundle)

  squared.settings = {
    pierceShadowRoot: true,
    adaptStyleMap: false,
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

.. code-block::
  :caption: Global (query)

  squared.settings = {
    excludePlainText: true, // HTMLElement + SVGElement
    createElementMap: true
  };

.. code-block::
  :caption: Global (unused)

  squared.settings = {
    preloadImages: false,
    preloadFonts: false,
    preloadLocalFonts: false,
    preloadCustomElements: false
  };