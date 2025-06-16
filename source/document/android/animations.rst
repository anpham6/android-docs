==============
SVG Animations
==============

Initialize
==========

Animations are usually started before *DOMContentLoaded* has been fired and :func:`parseDocument` may be unable to read the initial **attribute** values. Inline hints can be used to recreate the non-*CSS* initial values when they are altered by the native *SVG*.

.. code-block:: html
  :caption: JSON
  :emphasize-lines: 2

  <svg viewBox="0 0 200 200">
    <rect id="animate" x="10" y="10" width="30" height="20" fill="purple" data-base-value='{ "x": 10, "y": 10, "width": 30, "height": 20, "fill": "purple" }'>
      <animate attributeName="y" values="150; 75; 0; 50; 100" keyTimes="0; 0.2; 0.5; 0.7; 1" begin="0s" dur="9s" repeatCount="indefinite" />
    </rect>
  </svg>

.. code-block:: html
  :caption: Delimited
  :emphasize-lines: 1-2

  <svg width="120" height="120" viewBox="0 0 240 240" data-base-value="width: 120; height: 120; opacity: 1;">
    <rect x="10" y="0" width="100" height="50" stroke="black" stroke-width="2" fill="purple" data-base-value="x: 10; y: 0; width: 100; fill: purple; opacity: 1; stroke-opacity: 1; fill-opacity: 1;">
      <animate attributeName="x" values="0; 100" keyTimes="0; 1" begin="0s" dur="10s" repeatCount="indefinite" />
      <animate attributeName="y" values="0; 100" keyTimes="0; 1" begin="0s; 5s; 10s" dur="10s" repeatCount="1" />
    </rect>
  </svg>

Interpolator
============

::

  squared.attr("android.resource.svg", "customInterpolator", true); // One template per element
  /* OR */
  squared.attr("android.resource.svg", "customInterpolator", 1); // One shared template per type/config

.. code-block:: html
  :caption: data-timing-function

  <svg width="120" height="120" viewBox="0 0 240 240">
    <rect x="10" y="0" width="100" height="50" data-timing-function="decelerate"> <!-- does not inherit -->
      <animate attributeName="x" values="0; 100" keyTimes="0; 1" begin="0s" dur="10s" /> <!-- inherits from shape -->
      <animate attributeName="x" values="0; 100" keyTimes="0; 1" begin="0s" dur="10s" data-timing-function="none" /> <!-- no timing function -->
      <animate attributeName="y" values="0; 100" keyTimes="0; 1" begin="0s" dur="10s" data-timing-function='anticipate_overshoot={ "tension": 3, "extraTension": 2 }' /> <!-- strict JSON -->
    </rect>
  </svg>

These built-in interpolators are usable without any additional configuration:

.. hlist::
  :columns: 2

  - accelerate

    * factor

  - anticipate

    * tension

  - anticipate_overshoot

    * tension
    * extraTension

  - cycle

    * cycles

  - decelerate

    * factor

  - overshoot

    * tension

.. note:: The extension will always generate an interpolator with custom attributes.

Play
====

Only the XML based layout and resource files can be viewed on the Android device/emulator without any Java/Kotlin backend code. To play animations in the emulator you also have to :target:`start` the animation in *MainActivity.java*.

.. code-block:: java
  :emphasize-lines: 6

  import android.graphics.drawable.Animatable;

  android.widget.ImageView svg = findViewById(R.id.imageview_1);
  if (svg != null) {
      Animatable animatable = (Animatable)svg.getDrawable();
      animatable.start();
  }