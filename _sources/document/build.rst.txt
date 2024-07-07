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
      incremental?: boolean | "none" | "staging" | "etag" | "exists";
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

.. code-block::
  :emphasize-lines: 15

  interface DocumentOutput {
      targetAPI?: number | string;
      manifest?: ManifestData;
      namespace?: string;
      applicationId?: string;
      profileable?: boolean | string | string[];
      dependencies?: string[];
      dependencyScopes?: boolean | 1 | DependencyScopes | "snapshot" | (DependencyScopes | "snapshot")[];
      directories?: ControllerSettingsDirectoryUI;
      projectName?: string;
      mainParentDir?: string;
      mainSrcDir?: string;
      mainActivityFile?: string;
      javaVersion?: number | string;
      jvmToolchain?: number | string;
      versionName?: string;
      versionCode?: number;
      dataBinding?: boolean;
      commands?: string | string[] | (string | string[])[];
      extensionData?: Record<string, PlainObject>;
      updateXmlOnly?: boolean;
  }

.. versionadded:: 5.3.0

  - *DocumentOutput* property **jvmToolchain** for :alt:`build.gradle` upgrades was created.

.. versionadded:: 5.2.0

  - *DocumentOutput* property **dependencyScopes** with the :target:`snapshot` number value **1** for all scopes was amended.

Example usage
-------------

.. code-block:: javascript

  squared.saveAs("android.zip", {
    targetAPI: 32, // Override settings.targetAPI
    targetAPI: "Tiramisu",
    manifest: {
      package: "com.example.demo", // <manifest package="com.example.demo">
      application: {
        label: "app_name",
        supportsRtl: true,
        theme: "AppTheme"
      }
    },
    namespace: "com.example.demo", // android.defaultConfig.applicationId (app/build.gradle)
    profileable: true, // <profileable android:enabled="[false|true]" />
    profileable: "debug", // android.buildTypes.release.signingConfig = signingConfigs.debug
    profileable: "--warn-manifest-validation", // aaptOptions.additionalParameters (--prefix)
    profileable: ["release", "--warn-manifest-validation", "--no-version-vectors"], // signingConfig + additionalParameters (multiple --args)
    dependencies: ["androidx.appcompat:appcompat:1.6.0"],
    dependencyScopes: true, // All first-level dependencies
    dependencyScopes: "compile", // implementation="compile" | compileOnly="provided" | runtimeOnly="runtime" | testImplementation="test"
    dependencyScopes: ["compile", "runtime"],
    dependencyScopes: "snapshot", // Use latest published release
    dependencyScopes: 1, // true + "snapshot"
    dependencyScopes: ["snapshot", "compile"],
    directories: {
      layout: "/path/to/res/layout",
      string: "/path/to/res/values"
    },
    projectName: "Example Project", // rootProject.name (settings.gradle)
    mainParentDir: "app", // Override settings.outputDirectory
    mainSrcDir: "src/main",
    mainActivityFile: "MainActivity.java", // "MainActivity.*" | "/path/user/project/MainActivity.java" | "app/path/MainActivity.java"
    javaVersion: 1.8, // JavaVersion.VERSION_1_8
    javaVersion: 11, // JavaVersion.VERSION_11
    jvmToolchain: 17,
    versionName: "1.0",
    versionCode: 1,
    dataBinding: true, // android.buildFeatures.dataBinding
    commands: "build", // gradlew build
    commands: ["test", "deploy"], // gradlew test deploy
    commands: ["lint", ["test", "--rerun-tasks"]], // gradlew lint && gradlew test --rerun-tasks
    updateXmlOnly: true // Copy only auto-generated content
  });

.. code-block:: javascript
  :caption: With assets

  squared.saveAs("android.zip", {
    projectId: "project-1",
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

.. code-block::
  :emphasize-lines: 9-11,19,35

  interface FileActionOptions {
      baseHref?: URL;
      saveAs?: {
          html?: SaveAsOptions;
          script?: SaveAsOptions;
          link?: SaveAsOptions;
          image?: SaveAsOptions;
          font?: SaveAsOptions;
          video?: SaveAsOptions;
          audio?: SaveAsOptions;
          raw?: SaveAsOptions;
      };
      downloadOnly?: boolean;
      excluding?: HTMLElement[];
      observe?: true | MutationCallback;
      preserveCrossOrigin?: boolean | URLData;
      addResourceHints?: boolean | ResourceHintType | ResourceHintType[];
      retainUsedStyles?: (string | RegExp)[] | UsedStylesData;
      removeBinaries?: boolean;
      removeInlineStyles?: boolean;
      removeUnusedClasses?: boolean;
      removeUnusedPseudoClasses?: boolean;
      removeUnusedVariables?: boolean;
      removeUnusedFontFace?: boolean;
      removeUnusedKeyframes?: boolean;
      removeUnusedMedia?: boolean;
      removeUnusedSupports?: boolean;
      removeUnusedContainer?: boolean;
      removeUnusedScope?: boolean;
  }

  interface DocumentOutput {
      productionRelease?: boolean | string;
      productionIncremental?: boolean;
      serverRootMapping?: StringMap;
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
      unusedSupports?: string[];
      unusedContainer?: string[];
      unusedScope?: string[];
      unusedAtRules?: UnusedAtRule[];
  }

.. versionadded:: 5.3.0

  - *FileActionOptions* property **removeBinaries** for :alt:`squared.js` <script> exclusion was created.
  - *DocumentOutput* property **serverRootMapping** for local path rewriting in :alt:`productionRelease` was created.
  - *DocumentOutput* property **saveAs** with sub-properties as :alt:`SaveAsOptions` was amended:

    .. hlist::
      :columns: 3

      - video
      - audio
      - raw

.. versionadded:: 5.2.0

  - *FileActionOptions* property **removeUnusedScope** for :alt:`@scope` removal was created.

Example usage
-------------

.. code-block:: javascript

  squared.copyTo("/path/project", {
    cache: {
      transform: false, // Not recommended when using watch
      transform: true, // "etag" (not bundled) + string comparison by URL (single page)
      transform: "etag", // request.cache OR request.buffer.expires (required)
      transform: "md5" | "sha1" | "sha224" | "sha256" | "sha384" | "sha512", // Multi-[user|page] + Inline content (includes "etag")
      transform: { expires: "2h" }, // Expires in 2 hrs since creation
      transform: { expires: "1h", renew: true }, // Expires from 1 hr of last time accessed
      transform: { algorithm: "md5" /* etag */, expires: "2h", limit: "5mb" }, // Set expiration and content size limit
      transform: { exclude: { html: "*", js: ["bundle-es6"] } }, // Format names per type
      transform: { include: { css: "*", js: ["bundle"] } }
    },
    checksum: true, // sha256 + recursive
    checksum: 1, // sha256 + recursive = 1
    checksum: "sha512", // checksum.sha512
    checksum: "filename.sha384", // sha384
    checksum: {
      algorithm: "md5", // Default is "sha256"
      digest: "base64", // Default is "hex"
      filename: "checksum.crc", // Default is "checksum" + algorithm
      recursive: true, // Default is "false"
      recursive: 1, // Ignore nested checksum files
      include: "**/*.png", // Has precedence
      exclude: ["**/*.js", "**/*.css"]
    },
    imports: {
      "http://localhost:3000/build/": "./build", // Starts with "http"
      "http://localhost:3000/dist/chrome.framework.js": "/path/project/build/framework/chrome/src/main.js" // Full file path
    },
    webBundle: { // Chromium
      baseUrl: "http://hostname/dir/", // Resolves to current host and directory
      rewriteHtmlPage: true | "index.html", // Hide or rename main page
      excludeHtmlPage: true, // Exclude HTML page from WBN archive
      excludeTransforms: true, // Exclude transformed files not used in HTML page
      includeScopes: ["**/*.css"], // http://localhost:3000/dir/**/*.css (hides "excludeTransforms" + "excludeScopes")
      excludeScopes: ["/**/*.js"], // http://localhost:3000/**/*.js
      copyTo: "/path/project", // Copy archive (absolute + permission)
      rootDirAlias: "__serverroot__" // Internal
    },
    baseHref: "http://hostname/prod/example.html", // Additional hostname to use for parsing local files
    retainUsedStyles: [/^a:[a-z]/i, "--property-name"],
    downloadOnly: true, // Do not transform HTML and CSS files
    excluding: Array.from(document.querySelectorAll("video, audio")) // Elements to remove from HTML
  });

.. seealso:: :external+chrome:doc:`E-mc <index>` / :external+chrome:doc:`Build Options <build>`

.. |FileActionOptions| replace:: :ref:`FileActionOptions <references-squared-main>`
.. |DocumentOutput| replace:: :ref:`DocumentOutput <references-android-file>`
.. |RequestData| replace:: :ref:`RequestData <references-squared-base-file>`