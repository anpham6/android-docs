=========
Multiline
=========

.. highlight:: html

Intl Locales
============

Extension
---------

.. code-block:: javascript
  :caption: Global

  squared.settings.defaultIntlLocales = ["ja-JP"]; // All text elements
  /* OR */
  squared.attr("android.delegate.multiline", "intlLocales", ["ja-JP"]);

.. code-block:: javascript
  :caption: Root element

  squared.parseDocument("content-id", {
    options: {
      "android.delegate.multiline": {
        intlLocales: ["ja-JP"]
      }
    }
  });

.. note:: The first supported locale is applied to all text elements only when there is word wrapping.

Inline
------

Setting anything inline overrides all inherited global settings and can also prevent an element from being interpreted.

.. code-block::
  :caption: Source

  <p data-intl-locales-android="ja-JP-u-ca, ja-JP">
    吾輩は猫である。名前はたぬき。
    吾輩は猫である。名前はたぬき。
  </p>

  <p data-intl-locales-android="none">
    吾輩は猫である。名前はたぬき。
    吾輩は猫である。名前はたぬき。
  </p>

.. tip:: The ``-android`` suffix is optional when using only one framework.

Font Adjustment
===============

Browser to device measurements are not expected to be accurate due to issues with font availability and screen resolutions. Text wrapping can be adjusted at the global and element level.

Global
------

.. code-block:: javascript

  squared.settings.fontMeasureAdjust = 1; // 1px added per character to width

Inline
------

.. code-block::
  :caption: Source

  <p>
    content content content content
    content content content content
  </p>

.. code-block::
  :caption: Wrap late < 0

  <p data-android-font-measure-adjust="-0.5">
    content content content content content
    content content content
  </p>

.. code-block::
  :caption: Wrap early > 0

  <p data-android-font-measure-adjust="1">
    content content content
    content content content
    content content
  </p>

.. code-block::
  :caption: No adjustment = 0

  <p data-android-font-measure-adjust="0">
    content content content content
    content content content content
  </p>

.. code-block::
  :caption: Ignore

  <p data-android-font-measure-adjust="false">
    content content content content content content content content
  </p>

.. tip:: *CSS* ``initial-letter`` uses the :target:`multiline` extension for detection and rendering.

Column Spacing
==============

The amount of spacing between words cannot be accurately measured due to the font size differences on the output device. Inline properties can be used to modify when a block of text is to be segmented into another column when using *CSS* ``column-width`` or ``column-spacing``.

::

  <p data-android-column-word-spacing="0.25">
    content content content content
    content content content content
  </p>

.. code-block::
  :caption: text-align: justify

  <p data-android-column-justify-spacing="4">
    content content content content
    content content content content
  </p>

.. note:: *CSS* ``word-spacing`` is not implemented when using column layout.