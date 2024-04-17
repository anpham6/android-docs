=============
Miscellaneous
=============

System Colors
=============

Any `R.color <https://developer.android.com/reference/android/R.color>`_ that starts with the prefix "**system_**" can be used as substitute for a CSS color.

::

  squared.settings.resourceSystemColors = {
    "system_accent1_0": "white", // Converted to ARGB
    "system_accent1_50": "#FFFFFF", // Will override "system_accent1_0"
    "system_accent1_100": ["white", 0.75], // Different color with opacity
    "system_accent1_200": "hwb(12 50% 0%)", // rgb + hsl
    "system_accent1_300": squared.lib.color.parseColor("#000", 1)
  };

.. note:: Android 12 :alt:`API 31` is required when using accent colors. [#]_

.. code-block::
  :caption: `?attr/color* <https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/color/res/values/attrs.xml>`_

  squared.settings.preferMaterialDesign = 'MaterialComponents'; // Required
  squared.settings.resourceSystemColors = {
    "system_accent1_0": "white", // Invalid
    "colorPrimary": "white",
    "colorSecondary": "rgb(255 0 0)"
  };

When any element uses a CSS color it will be substituted with the same value in the global system color map. This behavior can be disabled locally using dataset attributes. 

.. code-block:: html
  :caption: Active (highlight)
  :emphasize-lines: 1,3,5,10-12

  <div data-android-system-color-children="false">
    <span>Item 1</span>
    <span data-android-system-color="true">Item 2</span>
    <div>
      <span>Item 3</span>
    </div>
    <div>
      <span data-android-system-color="false">Item 4</span>
    </div>
    <div data-android-system-color="true">
      <span data-android-system-color="inherit">Item 5</span>
    </div>
    <div>
      <span data-android-system-color="inherit">Item 6</span>
    </div>
  <div>

Redirecting Output
==================

Sometimes it is necessary to extract elements and append them into other containers for it to look identical on the Android device. Usually it is when you are using an `App widget <https://developer.android.com/develop/ui/views/appwidgets/overview>`_ and never with the standard layouts.

.. code-block:: html
  :emphasize-lines: 4

  <div>
    <span>Item 1</span>
    <span data-android-target="location">Item 2</span>
    <span data-android-target="location" data-android-target-index="1">Item 3</span>
  <div>
  <ul id="location">
    <li>Item 4</li>
    <li>Item 5</li>
    <!-- span -->
  </ul>

.. code-block:: xml
  :emphasize-lines: 6

  <LinearLayout>
    <TextView>Item 1</TextView>
  </LinearLayout>
  <LinearLayout>
    <TextView>Item 4</TextView>
    <TextView>Item 3</TextView>
    <TextView>Item 5</TextView>
    <TextView>Item 2</TextView>
  </LinearLayout>

.. note:: Using **target** into a *ConstraintLayout* or *RelativeLayout* container will not include automatic positioning. Redirection will fail if the :target:`target location` is not a block/container element.

.. [#] https://source.android.com/docs/core/display/dynamic-color