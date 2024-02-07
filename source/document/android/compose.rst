===============
Jetpack Compose
===============

Most mobile applications do not have a deeply nested hierarchy and are generally better to implement using declarative programming.

Method
======

.. code-block::

  squared.settings.composableElements = ["main", "#content", "--boxShadow", "--height=300px"];
  squared.settings.createBuildDependencies = true; // Optional

You can also do it using the ``android.substitute`` extension directly inside the HTML element.

.. code-block::

  squared.add(["android.substitute", {
    element: {
      content: { android: { layout_width: "match_parent" } }
    }
  }]);

  const items = squared.attr("android.substitute", "viewAttributes");
  items.push("hint", "buttonTint");
  squared.attr("android.substitute", "attributeMapping", {
    "android:src": "app:srcCompat", // Rename
    "icon": "navigationIcon" // Set "android:icon"
  });

  squared.parseDocument({
    element: document.body,
    substitutableElements: [{
      selector: "#content",
      tag: "androidx.compose.ui.platform.ComposeView",
      renderChildren: false
    }],
    enabledSubstitute: true, // Disabled built-in extensions have convenience toggles
    /* OR */
    include: ["android.substitute"]
  });

Inline
======

.. code-block:: html
  :emphasize-lines: 4,5

  <body>
    <header style="height: 100px"></header>
    <main id="content"
      data-use="android.substitute"
      data-android-substitute-tag="androidx.compose.ui.platform.ComposeView"
      style="height: 300px; box-shadow: 10px 5px 5px black;">
      <!-- Interior elements are not rendered -->
    </main>
    <footer style="height: 80px"></footer>
  </body>

.. tip:: Compose will remove child elements by default. You can preserve them by explictly using the **renderChildren** property.

.. code-block:: html
  :emphasize-lines: 4

  <div id="fragment"
    data-use="android.substitute"
    data-android-substitute-tag="androidx.fragment.app.FragmentContainerView"
    data-android-substitute-render-children="false"
    data-android-attr="name::com.github.fragment;tag::example">
    <!-- Interior elements are not rendered -->
  </div>

.. tip:: You can also use ``android.substitute`` to create fragments within a layout similar to Compose.