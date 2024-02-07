==========
Substitute
==========

There are some cases where a DOM layout tree has to be transformed into an equivalent layout using third-party controls.

.. code-block::

  squared.parseDocument({
    element: document.body,
    include: ["android.substitute"],
    substitutableElements: [{
      selector: "#navigation",
      tag: "com.google.android.material.tabs.TabLayout",
      tagChild: "com.google.android.material.tabs.TabItem",
      tagChildAttr: {
        android: {
          layout_height: "match_parent"
        }
      },
      renderChildren: true,
      autoLayout: true
    }]
  });

.. code-block:: html
  :emphasize-lines: 4,5,6

  <ul id="navigation"
    data-use-android="android.substitute"
    data-android-attr="layout_height::match_parent"
    data-android-substitute-tag="com.google.android.material.tabs.TabLayout"
    data-android-substitute-tag-child="com.google.android.material.tabs.TabItem"
    data-android-substitute-tag-child-attr="layout_height::match_parent"
    data-android-substitute-auto-layout="true">
    <li>TAB 1</li>
    <li>TAB 2</li>
    <li>TAB 3</li>
  </ul>

.. code-block:: xml
  :caption: Output

  <com.google.android.material.tabs.TabLayout
    android:id="@+id/navigation"
    android:layout_height="match_parent"
    android:layout_width="wrap_content">
    <com.google.android.material.tabs.TabItem
      android:layout_height="match_parent"
      android:layout_width="wrap_content"
      android:text="@string/tab_1" />
    <com.google.android.material.tabs.TabItem
      android:layout_height="match_parent"
      android:layout_width="wrap_content"
      android:text="@string/tab_2" />
    <com.google.android.material.tabs.TabItem
      android:layout_height="match_parent"
      android:layout_width="wrap_content"
      android:text="@string/tab_3" />
  </com.google.android.material.tabs.TabLayout>