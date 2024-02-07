=================
Custom Attributes
=================

System or extension generated attributes can be overridden preceding finalization. They will only be visible on the declared framework.

Method
======

.. code-block::

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

  <div id="customId"
    data-android-attr="layout_width::match_parent;layout_height::match_parent"
    data-android-attr-app="layout_scrollFlags::scroll|exitUntilCollapsed">
  </div>

.. code-block:: xml
  :caption: output

  <LinearLayout
    android:id="@+id/customId"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:layout_scrollFlags="scroll|exitUntilCollapsed" />

.. note:: Default namespace is "android"