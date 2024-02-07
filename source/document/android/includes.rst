===============
Layout Includes
===============

Some applications can benefit from using includes or merge tags to share common templates. Merge is the default behavior and can be disabled using the "false" attribute value. Nested includes are also supported.

.. code-block:: html
  :emphasize-lines: 6

  <div>
    <div id="item1">Item 1</div>
    <div id="item2" data-android-include-start="true" data-android-include-merge="true" data-pathname-android="app/src/main/res/layout-land" data-filename-android="filename1.xml">Item 2</div>
    <div id="item3">Item 3</div>
    <div id="item4" data-android-include-end="true">Item 4</div>
    <div id="item5" data-android-include="filename2" data-android-include-end="true" data-android-include-viewmodel="exampleData">Item 5</div>
  </div>

.. tip:: **data-pathname-android** AND **data-filename-android** can also be used with any ``parseDocument`` root element.

.. code-block::
  :emphasize-lines: 3,24

  android.setViewModelByProject(
    {
      variable: [{ name: "exampleData", type: "com.example.ExampleData" }]
    },
    "project-1"
  );

  squared.parseDocument({
    element: document.body,
    projectId: "project-1", // Affects all layouts in same project
    enabledIncludes: true,
    includableElements: [
      {
        selectorStart: "#item2",
        selectorEnd: "#item4",
        pathname: "app/src/main/res/layout-land",
        filename: "filename1.xml",
        merge: true // Multiple elements will auto-merge
      },
      {
        selectorStart: "#item5",
        selectorEnd: "#item5",
        filename: "filename2", // Uses default layout file extension ".xml"
        viewModel: "exampleData" // One element only when "merge = false"
      }
    ]
  });

.. note:: By *sessionId* has precedence when associating a view model.

.. code-block:: xml
  :caption: Output

  <!-- res/layout/activity_main.xml -->
  <LinearLayout>
    <TextView>Item 1</TextView>
    <include layout="@layout/filename1" />
    <include layout="@layout/filename2" app:exampleData="@{exampleData}" />
  </LinearLayout>

  <!-- res/layout-land/filename1.xml -->
  <merge>
    <TextView>Item 2</TextView>
    <TextView>Item 3</TextView>
    <TextView>Item 4</TextView>
  </merge>

  <!-- res/layout/filename2.xml -->
  <layout>
    <data>
      <variable name="exampleData" type="com.example.ExampleData" />
    </data>
    <TextView>Item 5</TextView>
  </layout>

The attributes **data-android-include-start** and **data-android-include-end** can only be applied to elements which share the same parent container.

.. seealso:: Demo page using `squared-express <http://localhost:3000/demos/gradient.html>`_ [#]_ for an actual implementation.

.. [#] https://github.com/anpham6/squared/blob/master/html/demos/gradient.html