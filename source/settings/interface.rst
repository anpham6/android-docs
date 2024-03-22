=========
Interface
=========

These settings are available in the global variable ``squared`` to customize your desired output structure. Each framework shares a common set of settings and also a subset of their own settings.

.. highlight:: typescript

.. code-block::
  :emphasize-lines: 5

  interface UserSettings {
      builtInExtensions: string[];
      showErrorMessages: boolean;
      pierceShadowRoot: boolean;
      adaptStyleMap: boolean;
      createElementMap: boolean;
  }

::

  interface UserResourceSettings extends UserSettings {
      preloadImages: boolean;
      preloadFonts: boolean;
      preloadLocalFonts: boolean;
      preloadCustomElements: boolean;
      outputEmptyCopyDirectory: boolean;
      outputDocumentHandler: string | string[];
      outputArchiveFormat: string;
      outputArchiveName: string;
      outputArchiveCache: boolean;
      outputSummaryModal: boolean | string;
      formatUUID?: string;
      formatDictionary?: string;
      outputTasks?: Record<string, TaskCommand[]>;
      outputWatch?: Record<string, boolean | WatchInterval>;
      outputConfigName?: string;
      observePort?: number;
      observeSecurePort?: number;
      observeExpires?: string;
      broadcastPort?: number;
      broadcastSecurePort?: number;
  }

.. code-block::
  :emphasize-lines: 4,11

  interface UserResourceSettingsUI extends UserResourceSettings {
      enabledSVG: boolean;
      supportNegativeLeftTop: boolean;
      showAttributes: boolean | Record<string, unknown>;
      showComments: boolean | CssStyleAttr[] | { include?: ShowCommentsInclude } & Record<string, CssStyleAttr[]>;
      insertSpaces: number;
      outputDirectory: string;
      outputDocumentEditing: boolean;
      outputDocumentCSS: CssStyleAttr[];
      framesPerSecond?: number;
      useShapeGeometryBox?: boolean;
      resolutionScreenWidth?: number;
      resolutionScreenHeight?: number;
  }

.. versionadded:: 5.2.0

  - *UserSettings* property **adaptStyleMap** for the rendered value was created.
  - *UserResourceSettingsUI* property **useShapeGeometryBox** for SVG native method getBbox was created.
  - *UserResourceSettingsUI* property **showAttributes** for global attribute modification is supported.

.. seealso:: For any non-standard named definitions check :doc:`References </references>`.

Example usage
=============

.. code-block:: javascript
  :caption: All

  squared.settings = {
    pierceShadowRoot: false,
    adaptStyleMap: false, // Merge all associated styles into rendered value
    showErrorMessages: false, // console.log
    showErrorMessages: true, // alert
    createElementMap: false // Cache queries for subsequent nested queries
  };

.. note:: The native ``document.querySelector`` does not enter :ref:`ShadowRoot <references-typescript-dom-generated>` elements.

.. code-block:: javascript
  :caption: Resource

  squared.settings = {
    formatUUID: "8-4-4-4-12", // UUID: 8-4-[12345]3-[89ab]3-12
    formatDictionary: "0123456789abcdef",
    outputConfigName: "sqd.config", // Per directory filename with URL globs of static pages
    outputTasks: {
      "*.xml": { handler: "gulp", task: "minify" }
    },
    outputWatch: {
      "**/images/*.png": true,
      "**/images/*.jpg": { interval: 1000, expires: "2h" }
    },
    observePort: 8080,
    observeSecurePort: 8443,
    observeExpires: "1h", // Server defaults will be used
    broadcastPort: 3080,
    broadcastSecurePort: 3443
  };

.. attention:: These settings are not available in the :doc:`vdom` framework.