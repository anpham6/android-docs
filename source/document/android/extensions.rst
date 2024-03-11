==========
Extensions
==========

Layout rendering can be fully customized as the program was built to be nearly completely modular. Some of the common layouts already have built-in extensions which you can load or unload based on your preference.

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: squared.accessibility

  interface ExtensionAccessibilityOptions {
      displayLabel: boolean;
  }

.. code-block::
  :caption: squared.grid

  interface ResourceGridOptions {
      floatPrecision: number;
  }

.. code-block::
  :caption: squared.css-grid

  interface ResourceCssGridOptions {
      floatPrecision: number;
  }

.. code-block::
  :caption: squared.list

  interface ExtensionListOptions {
      ordinalFontSizeAdjust: number;
      ordinalPaddingLeft: number;
      imagePaddingRight: number;
      /* base */
      symbolDisc: string;
      symbolSquare: string;
      symbolCircle: string;
      symbolDisclosureOpen: string;
      symbolDisclosureClosed: string | [string, string /* rtl */];
      symbolFallback: string;
      markerStyle: CssStyleMap;
  }

.. code-block::
  :caption: android.substitute

  interface ExtensionSubstituteOptions {
      element: Record<string, ExtensionAttributeElement>;
      resource: PlainObject;
      viewAttributes: string[];
      attributeMapping: StringMap;
  }

.. code-block::
  :caption: android.delegate.multiline

  interface DelegateMultilineOptions {
      mergeSingleLine: boolean;
  }

.. code-block::
  :caption: android.delegate.scrollbar

  interface DelegateScrollbarOptions {
      alwaysDrawTrack: boolean;
      alwaysDrawHorizontalTrack: boolean;
      alwaysDrawVerticalTrack: boolean;
      style: "none" | "outsideInset" | "insideInset" | "insideOverlay" | "outsideOverlay";
      size: string; // px
      thinSize: string;
      fadeDuration: number;
      delayBeforeFade: number;
  }

.. code-block::
  :caption: android.resource.background

  interface ResourceBackgroundOptions {
      outlineAsInsetBorder: boolean;
      enableImageRepeat: boolean;
  }

.. code-block::
  :caption: android.resource.dimens

  interface ResourceDimensOptions {
      percentAsResource: boolean;
      floatPrecision: number;
  }

.. code-block::
  :caption: android.resource.fonts

  interface ResourceFontsOptions {
      defaultFontFamily: string;
      systemFonts: string[];
      disableFontAlias: boolean;
      installGoogleFonts: boolean;
      fontSizeAdjust: number;
      floatPrecision: number;
  }

.. code-block::
  :caption: android.resource.fragment

  interface ExtensionFragmentOptions {
      viewAttributes: string[];
      viewAttributesApp: string[];
      retainAttributes: string[];
      retainAttributesApp: string[];
      dynamicNestedFragments: boolean;
  }

.. code-block::
  :caption: android.resource.includes

  interface ExtensionIncludesOptions {
      viewAttributes: string[];
      viewAttributesApp: string[];
      viewAttributesOuterView: string[];
  }

.. code-block::
  :caption: android.resource.strings

  interface ResourceStringsOptions {
      numberAsResource: boolean;
  }

.. code-block::
  :caption: android.resource.svg

  interface ResourceSvgOptions {
      textAsImage: boolean;
      transformExclude: SvgTransformExclude;
      animateInterpolator: string;
      floatPrecision: number;
      floatPrecisionKeyTime: number;
  }

.. code-block::
  :caption: jetpack.compose.view

  interface JetpackComposeViewOptions {
      viewAttributes: string[];
      renderChildren: boolean;
  }

.. note:: These are only the built-in extensions with configurable settings.

Example usage
=============

Some extensions have a few settings which can be configured. The default settings usually achieve the best overall rendering accuracy without noticeably affecting performance.

.. code-block::
  :caption: Create

  class Sample extends squared.base.ExtensionUI {
      options = {
          attributeName: [],
          floatPrecision: 3
      };

      constructor(name, framework = 0, options = {}) {
          super(name, framework, options);
      }

      processNode(node) {
          const data = this.project.get(node.element, node.localSettings.projectId);
          if (data) {
              node.each((child, index) => child.element.title = data[index]);
          }
      }
  }

.. highlight:: javascript

.. code-block::
  :caption: Install

  const sample = new Sample("widget.example.com", 2 /* APP_FRAMEWORK.ANDROID */, { tagNames: ["span", "li"], dependencies: ["android.substitute"] });
  squared.add(sample);
  // OR
  squared.add([sample, { attributeName: ["width", "height"] }]);

.. code-block::
  :caption: Configure

  squared.attr("widget.example.com", "floatPrecision", 2); // typeof is enforced and will only set existing attributes

.. code-block::
  :caption: Add project data

  const ext = squared.get("widget.example.com");

  ext.project.set(element, await fetch(url?id=1)); // Map interface with optional "projectId" argument
  ext.project.set(element, await fetch(url?id=2), "project-1");

  const data = ext.project.get(element, "project-2"); // Returns data from default project (id=1)

.. versionadded:: 5.2.0

  - *ExtensionListOptions* properties were created:

    .. hlist::
      :columns: 3

      - symbolDisc
      - symbolSquare
      - symbolCircle
      - symbolDisclosureOpen
      - symbolDisclosureClosed
      - symbolFallback
      - markerStyle

  - *DelegateScrollbarOptions* properties were created:

    .. hlist::
      :columns: 3

      - alwaysDrawHorizontalTrack
      - alwaysDrawVerticalTrack
      - style
      - size
      - thinSize
      - fadeDuration
      - delayBeforeFade

  - *ProjectMap* methods **get** | **has** will also check default project "_" for key. 