==========
Extensions
==========

Layout rendering can be fully customized as the program was built to be nearly completely modular. Some of the common layouts already have built-in extensions which you can load or unload based on your preference.

Interface
=========

.. code-block:: typescript
  :caption: squared.accessibility

  interface ExtensionAccessibilityOptions {
      displayLabel: boolean;
  }

.. code-block:: typescript
  :caption: squared.grid

  interface ResourceGridOptions {
      floatPrecision: number;
  }

.. code-block:: typescript
  :caption: squared.css-grid

  interface ResourceCssGridOptions {
      floatPrecision: number;
  }

.. code-block:: typescript
  :caption: squared.list

  interface ExtensionListOptions {
      ordinalFontSizeAdjust: number;
      ordinalPaddingLeft: number;
      imagePaddingRight: number;
  }

.. code-block:: typescript
  :caption: android.substitute

  interface ExtensionSubstituteOptions {
      element: Record<string, ExtensionAttributeElement>;
      resource: Record<string, unknown>;
      viewAttributes: string[];
      attributeMapping: Record<string, string>;
  }

.. code-block:: typescript
  :caption: android.delegate.multiline

  interface DelegateMultilineOptions {
      mergeSingleLine: boolean;
  }

.. code-block:: typescript
  :caption: android.delegate.scrollbar

  interface DelegateScrollbarOptions {
      alwaysDrawTrack: boolean;
  }

.. code-block:: typescript
  :caption: android.resource.background

  interface ResourceBackgroundOptions {
      outlineAsInsetBorder: boolean;
      enableImageRepeat: boolean;
  }

.. code-block:: typescript
  :caption: android.resource.dimens

  interface ResourceDimensOptions {
      percentAsResource: boolean;
      floatPrecision: number;
  }

.. code-block:: typescript
  :caption: android.resource.fonts

  interface ResourceFontsOptions {
      defaultFontFamily: string;
      systemFonts: string[];
      disableFontAlias: boolean;
      installGoogleFonts: boolean;
      fontSizeAdjust: number;
      floatPrecision: number;
  }

.. code-block:: typescript
  :caption: android.resource.fragment

  interface ExtensionFragmentOptions {
      viewAttributes: string[];
      viewAttributesApp: string[];
      retainAttributes: string[];
      retainAttributesApp: string[];
      dynamicNestedFragments: boolean;
  }

.. code-block:: typescript
  :caption: android.resource.includes

  interface ExtensionIncludesOptions {
      viewAttributes: string[];
      viewAttributesApp: string[];
      viewAttributesOuterView: string[];
  }

.. code-block:: typescript
  :caption: android.resource.strings

  interface ResourceStringsOptions {
      numberAsResource: boolean;
  }

.. code-block:: typescript
  :caption: android.resource.svg

  interface ResourceSvgOptions {
      textAsImage: boolean;
      transformExclude: SvgTransformExclude;
      animateInterpolator: string;
      floatPrecision: number;
      floatPrecisionKeyTime: number;
  }

.. code-block:: typescript
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
  ext.project.set(element, await fetch(url), "project-1"); // Map interface with optional "projectId" argument