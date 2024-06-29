=========
Multiline
=========

Browser to device measurements are not expected to be accurate due to issues with font availability and screen resolutions. Text wrapping can be adjusted at the global and element level.

Global
======

::

  squared.settings.fontMeasureAdjust = 1; // 1px added per character to width

Inline
======

.. highlight:: html

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

Column
======

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
