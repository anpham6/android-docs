=================
Modify Attributes
=================

System or extension generated attributes can be overridden preceding finalization. They will only be visible on the declared framework.

.. tip:: Default namespace is ``android``.

Settings
========

::

  squared.settings.showAttributes = {
    "hyphenationFrequency": "full", // Replace all
    "android:fontFeatureSettings": null, // Delete all
    "app:menu": [
      "@menu/menu_1", "@menu/menu_2", // Replace with "@menu/menu_2" when value is "@menu/menu_1"
      "@menu/menu_3", null // Delete attribute when value is "@menu/menu_3"
    ]
  };

Method
======

::

  squared.parseDocument().then(() => {
    const node = squared.findDocumentNode("customId");
    node.android("layout_width", "match_parent");
    node.android("layout_height", "match_parent");
    node.app("layout_scrollFlags", "scroll|exitUntilCollapsed");
  });

Inline
======

.. code-block:: none

  data-android-attr-{namespace}?

.. code-block:: html
  :emphasize-lines: 2

  <div id="customId"
    data-android-attr="layout_width::match_parent;layout_height::match_parent"
    data-android-attr-app="layout_scrollFlags::scroll|exitUntilCollapsed">
  </div>

.. code-block:: xml
  :caption: Output

  <LinearLayout
    android:id="@+id/customId"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:layout_scrollFlags="scroll|exitUntilCollapsed" />