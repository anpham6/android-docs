==============
SVG Animations
==============

Initialize
==========

Animations are usually started before :func:`parseDocument` can read the initial values once the *DOMContentLoaded* event has fired. Inline hints are required in order to recreate the non-CSS initial values which are lost once they are dynamically altered by the native SVG.

.. code-block:: html
  :caption: JSON
  :emphasize-lines: 2

  <svg viewBox="0 0 200 200">
    <rect id="animate" x="10" y="10" width="30" height="20" fill="purple" data-base-value='{ "x": 10, "y": 10, "width": 30, "height": 20, "fill": "purple" }'>
      <animate attributeName="y" values="150; 75; 0; 50; 100;" keyTimes="0; 0.2; 0.5; 0.7; 1" begin="0s" dur="9s" repeatCount="indefinite" />
    </rect>
  </svg>

.. code-block:: html
  :caption: Delimited
  :emphasize-lines: 1,2

  <svg width="120" height="120" viewBox="0 0 240 240" data-base-value="width: 120; height: 120; opacity: 1;">
    <rect x="10" y="0" width="100" height="50" stroke="black" stroke-width="2" fill="purple" data-base-value="x: 10; y: 0; width: 100; fill: purple; opacity: 1; stroke-opacity: 1; fill-opacity: 1;">
      <animate attributeName="x" values="0; 100;" keyTimes="0; 1" begin="0s" dur="10s" repeatCount="indefinite" />
      <animate attributeName="y" values="0; 100" keyTimes="0; 1" begin="0s; 5s; 10s" dur="10s" repeatCount="1" />
    </rect>
  </svg>

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