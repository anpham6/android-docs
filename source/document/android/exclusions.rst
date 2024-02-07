==========
Exclusions
==========

Most attributes can be excluded from the generated XML. One or more exclusions can be applied to any element using the OR "|" operator.

.. tip:: Defining an element ``id`` will prevent it from being removed during the optimization phase.

Interface
=========

.. code-block:: typescript
  :caption: squared.lib.base.constant

  enum APP_SECTION {
      DOM_TRAVERSE = 1,
      EXTENSION = 2,
      RENDER = 4,
      ALL = DOM_TRAVERSE | EXTENSION | RENDER
  }

  enum NODE_RESOURCE {
      BOX_STYLE = 1,
      BOX_SPACING = 2,
      FONT_STYLE = 4,
      VALUE_STRING = 8,
      IMAGE_SOURCE = 16,
      ASSET = FONT_STYLE | VALUE_STRING | IMAGE_SOURCE,
      ALL = BOX_STYLE | BOX_SPACING | ASSET
  }

  enum NODE_PROCEDURE {
      CONSTRAINT = 1,
      LAYOUT = 2,
      ALIGNMENT = 4,
      ACCESSIBILITY = 8,
      LOCALIZATION = 16,
      CUSTOMIZATION = 32,
      OPTIMIZATION = 64,
      DOCUMENT = CONSTRAINT | LAYOUT | ALIGNMENT,
      ENHANCEMENT = ACCESSIBILITY | CUSTOMIZATION | OPTIMIZATION,
      USABILITY = ENHANCEMENT | LOCALIZATION,
      ALL = DOCUMENT | USABILITY
  }

Method
======

.. code-block::

    const { NODE_RESOURCE, NODE_PROCEDURE, APP_SECTION } = squared.base.lib.constant;

    await squared.parseDocument({
      element: document.body,
      excludeQuery: [
        {
          selector: "h1",
          section: APP_SECTION.DOM_TRAVERSE | APP_SECTION.EXTENSION,
          resource: NODE_RESOURCE.BOX_SPACING | NODE_RESOURCE.FONT_STYLE,
          procedure: NODE_PROCEDURE.CONSTRAINT | NODE_PROCEDURE.LOCALIZATION | NODE_PROCEDURE.CUSTOMIZATION | NODE_PROCEDURE.OPTIMIZATION
        },
        {
          selector: "p > span",
          resource: NODE_RESOURCE.FONT_STYLE
        },
        {
          selector: "#cb1",
          procedure: NODE_PROCEDURE.ACCESSIBILITY
        }
      ]
    });

Inline
======

.. code-block:: html

  <h1>
    data-exclude-section="DOM_TRAVERSE | EXTENSION"
    data-exclude-resource="BOX_SPACING | FONT_STYLE"
    data-exclude-procedure="CONSTRAINT | LOCALIZATION | CUSTOMIZATION | OPTIMIZATION">
    title
  </h1>
  <p>
    <span data-exclude-resource="FONT_STYLE">content</span>
    <input id="cb1" type="checkbox" data-exclude-procedure="ACCESSIBILITY"><label for="cb1">checkbox text</label>
  </p>

.. warning:: These may cause warnings when you compile your project and should only be used when an extension has their custom attributes overwritten.