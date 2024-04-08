=============
Miscellaneous
=============

Redirecting Output
------------------

Sometimes it is necessary to extract elements and append them into other containers for it to look identical on the Android device. Redirection will fail if the :target:`target location` is not a block/container element.

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

.. note:: Using **target** into a ConstraintLayout or RelativeLayout container will not include automatic positioning.