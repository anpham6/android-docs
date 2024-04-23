=======
Android
=======

Interface
=========

.. code-block:: typescript
  :emphasize-lines: 16,27,39

  interface UserResourceSettingsUI {
      targetAPI: number;
      supportRTL: boolean;
      compressImages: boolean;
      enabledMultiline: boolean;
      enabledViewModel: boolean;
      enabledIncludes: boolean;
      enabledFragment: boolean;
      enabledSubstitute: boolean;
      enabledCompose: boolean;
      dataBindableElements: ExtensionViewModelElement[];
      includableElements: ExtensionIncludeElement[];
      substitutableElements: ExtensionSubtituteElement[];
      fragmentableElements: (string | ExtensionFragmentElement)[];
      composableElements: string[];
      baseLayoutAsFragment: boolean | string | string[] | ExtensionFragmentElement;
      convertPixels: ResolutionUnit;
      lineHeightAdjust: number;
      fontMeasureAdjust: number;
      lockElementSettings: boolean;
      customizationsBaseAPI: number | number[];
      customizationsOverwritePrivilege: boolean;
      removeDeprecatedAttributes: boolean | string[];
      removeUnusedResourceViewId: boolean;
      preferMaterialDesign: boolean | "MaterialComponents" | "Material3";
      idNamingStyle: NamingStyles;
      showAttributes: boolean | Record<string, (string | null)[] | string | null>;
      createDownloadableFonts: boolean;
      manifestActivityName: string;
      manifestLabelAppName: string;
      manifestThemeName: string;
      manifestParentThemeName: string;
      createManifest: boolean;
      createBuildDependencies: boolean | ("ktx" | "baseline-profile")[];
      outputMainFileName: string;
      outputFragmentFileName: string;
      resolutionDPI?: number;
      resourceQualifier?: string | ResourceQualifierMap;
      resourceSystemColors?: Record<string, string | [string, number] | ColorRGB>;
      convertImages?: string;
      convertLineHeight?: ResolutionUnit;
      baseLayoutToolsIgnore?: string;
      manifestPackage?: string;
  }

.. versionadded:: 5.2.0

  - *UserResourceSettingsUI* property **showAttributes** accepts a map to globally replace layout attributes.
  - *UserResourceSettingsUI* property **resourceSystemColors** device color translation map was created.
  - *ExtensionFragmentElement* extends the *ViewAttribute* interface.

Example usage
=============

.. code-block::
  :caption: Customizable (project/all)
  :emphasize-lines: 7,44

  squared.settings = {
    targetAPI: 34,
    resolutionDPI: 160, // 320dpi = 2560x1600
    resolutionScreenWidth: 1280,
    resolutionScreenHeight: 800,
    framesPerSecond: 60, // SVG animation only
    useShapeGeometryBox: true, // Dimensions use native SVG method getBbox
    supportRTL: true,
    supportNegativeLeftTop: true,
    preloadImages: true,
    preloadFonts: true,
    preloadLocalFonts: true, // Chromium
    preloadCustomElements: true, // pierceShadowRoot = true
    enabledSVG: true, // android.resource.svg
    enabledMultiline: true, // android.delegate.multiline
    enabledViewModel: true, // android.resource.data
    enabledIncludes: false, // android.resource.includes
    enabledSubstitute: false, // android.resource.fragment
    enabledFragment: false, // android.substitute
    enabledCompose: false, // android.compose.view
    dataBindableElements: [/* ExtensionViewModelElement */],
    includableElements: [/* ExtensionIncludeElement */],
    substitutableElements: [/* ExtensionSubtituteElement */],
    fragmentableElements: [/* "selector" | ExtensionFragmentElement */],
    composableElements: [/* "selector" | "--property" */],
    baseLayoutAsFragment: "fragment-name",
    baseLayoutAsFragment: ["fragment-name", "fragment-tag", "document_id" /* Optional */],
    baseLayoutAsFragment: { // ExtensionFragmentElement
      name: "androidx.navigation.fragment.NavHostFragment",
      documentId: "main_content",
      app: {
        navGraph: "@navigation/product_list_graph",
        defaultNavHost: "true"
      }
    },
    baseLayoutToolsIgnore: "TooManyViews, HardcodedText", // Android Studio Editor
    fontMeasureAdjust: 0.75, // thicker < 0 | thinner > 0
    lineHeightAdjust: 1.1, // shorter < 1 | taller > 1
    preferMaterialDesign: true, // "Material3"
    preferMaterialDesign: "MaterialComponents",
    createDownloadableFonts: true,
    createElementMap: false, // Cache not used with NodeUI
    pierceShadowRoot: true,
    adaptStyleMap: true, // Use rendered values for output
    lockElementSettings: false, // Modify Node before rendering (LocalSettingsUI)
    customizationsBaseAPI: -1, // None
    customizationsBaseAPI: 0, // All (14 - 34)
    customizationsBaseAPI: [0, 33, 34], // Multiple with ordering
    customizationsOverwritePrivilege: true, // Existing auto-generated attributes (e.g. layout_width)
    removeDeprecatedAttributes: true, // Remove all
    removeDeprecatedAttributes: ["enabled", "singleLine"], // Remove all except the listed values
    removeUnusedResourceViewId: false,
    idNamingStyle: "android", // Use layout name
    idNamingStyle: "html", // Use tagName
    idNamingStyle: {
      "__default__": "html", // Optional
      "DIV": "comments", // HTML is uppercase (comments_1 then comments_2)
      "svg": ["vector", 0], // SVG is lowercase (vector_0 then vector_1)
      "#text": "text", // Plain text
      "::first-letter": "dropcap", // Pseudo element
      "main > section": ["content", 1, 2], // content_1 then content_3
      "form input[type=submit]": function(node) {
        return "submit_" + node.id;
      }
    },
    outputMainFileName: "activity_main.xml",
    outputFragmentFileName: "fragment_main.xml"
  };

.. code-block::
  :caption: Customizable (project/main)
  :emphasize-lines: 3-7

  squared.settings = {
    resourceQualifier: "land", // "res/layout-land"
    resourceSystemColors: {
        "system_accent1_100": "white", // Will be converted to ARGB
        "system_accent1_200": ["#ff0000", 0.75], // opacity
        "system_accent1_300": squared.lib.color.parseColor("#000", 1)
    },
    manifestPackage: "example", // <manifest package="example"> (OR: RequestData<{ namespace: "android.application.id" }>)
    manifestLabelAppName: "android", // <application android:label="@string/android">
    manifestThemeName: "AppTheme", // <application android:theme="@style/AppTheme"> (overrides manifestParentThemeName)
    manifestParentThemeName: "Theme.AppCompat.Light.NoActionBar", // <style parent="Theme.AppCompat.Light.NoActionBar"> [res/values/styles.xml]
    manifestActivityName: ".MainActivity", // <activity android:name=".MainActivity">
    outputDocumentEditing: true, // RequestData<{ targetAPI + dependencies + mainParentDir + mainSrcDir + directories + dataBinding + elements }> (append without overwrite)
    outputDocumentCSS: [], // CSS properties to be processed with a server extension (e.g. "boxShadow")
    outputDirectory: "app/src/main",
    createManifest: false, // Update AndroidManifest.xml
    createBuildDependencies: false, // build.gradle
    createBuildDependencies: ["ktx", "baseline-profile"]
  };

.. code-block::
  :caption: Global
  :emphasize-lines: 9

  squared.settings = {
    builtInExtensions: [
      "squared.accessibility",
      "android.delegate.background",
      "android.delegate.negative-x",
      "android.delegate.positive-x",
      "android.delegate.max-width-height",
      "android.delegate.percent",
      "android.delegate.content",
      "android.delegate.scrollbar",
      "android.delegate.radiogroup",
      "android.delegate.multiline",
      "squared.relative",
      "squared.css-grid",
      "squared.flexbox",
      "squared.table",
      "squared.column",
      "squared.list",
      "squared.grid",
      "squared.sprite",
      "squared.whitespace",
      "android.resource.background",
      "android.resource.svg",
      "android.resource.strings",
      "android.resource.fonts",
      "android.resource.dimens",
      "android.resource.styles",
      "android.resource.data"
    ],
    convertImages: "png", // jpeg | webp | gif | bmp
    compressImages: false, // TinyPNG (https://tinypng.com/developers)
    showAttributes: {
      "android:hyphenationFrequency": "full", // Replace all
      "android:fontFeatureSettings": null // Delete all
    },
    showComments: false, // <!-- TODO in layout.xml -->
    showComments: ["boxShadow"],
    showComments: {
      self: ["boxShadow"],
      nextSibling: ["marginBottom"],
      previousSibling: ["marginTop"],
      parent: ["position", "top", "left"]
    },
    showComments: {
      self: ["boxShadow", ".className"],
      include: {
        tagName: true, // ["button"]
        attributes: true, // ["id", "style"]
        dataset: false,
        bounds: true
      }
    },
    showErrorMessages: false,
    convertPixels: "dp", // ResolutionUnit
    convertLineHeight: "sp", // ResolutionUnit
    insertSpaces: 0, // tabs
    insertSpaces: 4, // per tab
    outputDocumentHandler: "android",
    outputEmptyCopyDirectory: false, // Sub directories within target directory (OR: RequestData<{ emptyDir: false }>)
    outputSummaryModal: true, // Affected files in base output directory
    outputSummaryModal: "path/summary.css", // Use custom style sheet
    outputSummaryModal: ".status-4 { color: purple; }", // Use inline style sheet
    outputTasks: {
      "**/drawable/*.xml": { handler: "gulp", task: "minify" }
    },
    outputWatch: {
      "**/drawable/*.png": true,
      "**/drawable/*.jpg": { interval: 1000, expires: "2h" }
    },
    outputArchiveName: "android-xml", // squared.saveAs
    outputArchiveFormat: "zip", // tar | 7z | gz
    outputArchiveCache: false // Downloadable URL in ResponseData<downloadUrl>
  };

.. code-block::
  :caption: Global (optional)

  squared.settings = {
    builtInExtensions: [
      "android.resource.includes", // enabledIncludes
      "android.substitute", // enabledSubstitute
      "android.resource.fragment", // enabledFragment
      "jetpack.compose.view" // enabledCompose
    ]
  };