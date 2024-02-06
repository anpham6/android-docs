Interface
=========

These settings are available in the global variable ``squared`` to customize your desired output structure. Each framework shares a common set of settings and also a subset of their own settings.

.. code-block:: typescript

  interface UserSettings {
      builtInExtensions: string[];
      showErrorMessages: boolean;
      pierceShadowRoot: boolean;
      createElementMap: boolean;
  }

.. code-block:: typescript

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

  interface TaskCommand {
      handler: string;
      task: unknown;
      preceding?: boolean;
  }

  interface WatchInterval {
      interval?: number | string;
      start?: number | string;
      expires?: number | string;
      id?: string;
      main?: boolean;
      reload?: WatchReload | boolean;
  }

  interface WatchReload {
      socketId?: string;
      port?: number;
      secure?: boolean;
      module?: boolean;
      always?: boolean;
      on?: {
          message: string;
          open?: string;
          error?: string;
          close?: string;
      };
  }

.. code-block:: typescript

  interface UserResourceSettingsUI extends UserResourceSettings {
      enabledSVG: boolean;
      supportNegativeLeftTop: boolean;
      showAttributes: boolean;
      showComments: boolean | CssStyleAttr[] | { include?: ShowCommentsInclude } & Record<string, CssStyleAttr[]>;
      insertSpaces: number;
      outputDirectory: string;
      outputDocumentEditing: boolean;
      outputDocumentCSS: CssStyleAttr[];
      framesPerSecond?: number;
      resolutionScreenWidth?: number;
      resolutionScreenHeight?: number;
  }

  interface ShowCommentsInclude {
      tagName?: boolean | string[];
      attributes?: boolean | string[];
      dataset?: boolean;
      bounds?: boolean;
  }

  type CssStyleAttr = keyof CSSStyleDeclaration;

Global
------

.. code-block:: typescript
  :caption: Required

  squared.settings = {
    pierceShadowRoot: false,
    showErrorMessages: false, // console.log
    showErrorMessages: true, // alert
    createElementMap: false // Cache querySelector results for subsequent queries
  };

.. note:: The native **document.querySelector** does not enter *shadowRoot* [#]_ elements.

.. code-block:: typescript
  :caption: Optional

  squared.settings = {
    formatUUID: "8-4-4-4-12", // UUID: 8-4-[12345]3-[89ab]3-12
    formatDictionary: "0123456789abcdef",
    outputConfigName: "sqd.config", // Per directory filename with URL globs of static pages
    outputTasks: {
      "*.xml": { handler: "gulp", task: "minify" } // https://e-mc.readthedocs.io/en/latest/task
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

.. note:: These optional settings are not available in the :doc:`vdom <vdom>` framework.

.. [#] https://developer.mozilla.org/docs/Web/API/ShadowRoot