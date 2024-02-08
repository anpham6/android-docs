=============
Build Options
=============

:squared:
    - |FileActionOptions|

:squared-express:
    - |DocumentOutput|
    - |RequestData|

Interface
=========

.. highlight:: typescript

::

  interface FileActionOptions {
      pid?: number;
      fetchMode?: RequestMode;
      timeout?: number;
      config?: boolean | string | FileActionConfig;
      incrementalMap?: {
          pathname?: IncrementalData;
          extension?: IncrementalData;
          mime?: IncrementalData;
          overwrite?: boolean;
      };
      outgoing?: OutgoingHeaders;
      exclusions?: Exclusions | (string | RegExp)[];
      broadcast?: BroadcastSocket | BroadcastMessageCallback;
      throwErrors?: boolean;
      filter?: (item: FileAsset, index: number, array: FileAsset[]) => unknown;
  }

  interface RequestData {
      projectId?: string;
      assets?: FileAsset[];
      dataSource?: DataSource[];
      document?: string[];
      task?: string[];
      modules?: string[];
      update?: WatchInterval;
      incremental?: boolean | IncrementalMatch;
      checksum?: string | boolean | 1 | ChecksumOutput;
      imports?: StringMap;
      headers?: OutgoingHeaders;
      watch?: boolean;
      cache?: boolean | PlainObject;
      log?: boolean | string | string[] | LogOptions;
      baseUrl?: string;
      priority?: number;
      broadcastId?: string | string[];
      error?: { abort?: boolean | string | string[]; fatal?: boolean };
      ignoreExtensions?: boolean | string | string[];
  }

::

  interface FileCopyingOptions extends FileActionOptions {
      pathname?: string;
      emptyDir?: boolean;
      modified?: boolean;
  }

  interface FileArchivingOptions extends FileActionOptions {
      filename?: string;
      format?: string;
      copyTo?: string;
  }

Android
=======

Interface
---------

::

  interface DocumentOutput {
      targetAPI?: number | string;
      manifest?: ManifestData;
      namespace?: string;
      profileable?: boolean | string | string[];
      dependencies?: string[];
      dependencyScopes?: boolean | DependencyScopes | "snapshot" | (DependencyScopes | "snapshot")[];
      directories?: ControllerSettingsDirectoryUI;
      projectName?: string;
      mainParentDir?: string;
      mainSrcDir?: string;
      mainActivityFile?: string;
      javaVersion?: number | string;
      versionName?: string;
      versionCode?: number;
      dataBinding?: boolean;
      commands?: string | string[] | (string | string[])[];
      extensionData?: Record<string, PlainObject>;
  }

Example usage
-------------

.. code-block:: javascript

  squared.saveAs("android.zip", {
    projectId: "project-1",
    priority: 10,
    profileable: true,
    dependencyScopes: "snapshot",
    manifest: {
      package: "example",
      application: {
        label: "app_name",
        supportsRtl: true,
        theme: "AppTheme"
      }
    },
    commands: ["clean", ["build", "--parallel"]],
    assets: [
      {
        pathname: "app/src/main/res/drawable",
        filename: "ic_launcher_background.xml",
        uri: "http://localhost:3000/common/images/ic_launcher_background.xml"
      },
      {
        pathname: "app/src/main/res/drawable-v24",
        filename: "ic_launcher_foreground.xml",
        uri: "http://localhost:3000/common/images/ic_launcher_foreground.xml"
      }
    ]
  });

Chrome
======

Interface
---------

::

  interface FileActionOptions {
      baseHref?: URL;
      saveAs?: {
          html?: SaveAsOptions;
          script?: SaveAsOptions;
          link?: SaveAsOptions;
          image?: SaveAsOptions;
          font?: SaveAsOptions;
      };
      downloadOnly?: boolean;
      excluding?: HTMLElement[];
      observe?: true | MutationCallback;
      preserveCrossOrigin?: boolean | URLData;
      addResourceHints?: boolean | ResourceHintType | ResourceHintType[];
      retainUsedStyles?: (string | RegExp)[] | UsedStylesData;
      removeInlineStyles?: boolean;
      removeUnusedClasses?: boolean;
      removeUnusedPseudoClasses?: boolean;
      removeUnusedVariables?: boolean;
      removeUnusedFontFace?: boolean;
      removeUnusedKeyframes?: boolean;
      removeUnusedMedia?: boolean;
      removeUnusedContainer?: boolean;
      removeUnusedSupports?: boolean;
  }

  interface DocumentOutput {
      productionRelease?: boolean | string;
      useOriginalHtmlPage?: boolean | string;
      useUnsafeHtmlReplace?: boolean;
      useSessionCache?: boolean;
      stripCommentsAndCDATA?: boolean | string;
      normalizeHtmlOutput?: boolean | string;
      escapeReservedCharacters?: boolean;
      webBundle?: {
          rootDirAlias?: string;
          baseUrl?: string;
          primaryUrl?: string;
          copyTo?: string;
          rewriteHtmlPage?: boolean | string;
          excludeHtmlPage?: boolean;
          includeScopes?: string[];
          excludeScopes?: string[];
      };
      templateMap?: TemplateMap;
      userAgentData?: UserAgentData;
      /* Auto-generated from "removeUnused" */
      usedVariables?: string[]; // User supplied prepended
      usedFontFace?: string[];
      usedKeyframes?: string[];
      unusedStyles?: string[];
      unusedMedia?: string[];
      unusedContainer?: string[];
      unusedSupports?: string[];
      unusedAtRules?: UnusedAtRule[];
  }

.. seealso:: For any non-standard named definitions check :doc:`References </references>`.

Example usage
-------------

.. code-block:: javascript

  squared.copyTo("/path/project", {
    projectId: "project-1",
    useOriginalHtmlPage: true,
    preserveCrossOrigin: true,
    useSessionCache: true,
    removeUnusedClasses: true,
    retainUsedStyles: [/^a:[a-z]/i, "--property-name"],
    excluding: Array.from(document.querySelectorAll("video, audio"))
  });

.. |FileActionOptions| replace:: :ref:`FileActionOptions <references-squared-main>`
.. |DocumentOutput| replace:: :ref:`DocumentOutput <references-android-file>`
.. |RequestData| replace:: :ref:`RequestData <references-squared-base-file>`