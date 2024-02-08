============
Data Binding
============

View model data can be applied to most HTML elements using the *dataset* [#]_ feature. Different view models can be used for every ``parseDocument`` session.

Leaving the *sessionId* empty uses the default view model which is searched last for all projects when attempting a bind.

Method
======

.. code-block::
  :emphasize-lines: 14,23

  squared.parseDocument("element-1", "element-2", "element-3").then(nodes => {
    const sessions = squared.latest(2); // ["2", "3"]
    android.setViewModel(
      {
        import: ["java.util.Map", "java.util.List"],
        variable: [
          { name: "user", type: "com.example.User" },
          { name: "list", type: "List&lt;String>" },
          { name: "map", type: "Map&lt;String, String>" },
          { name: "index", type: "int" },
          { name: "key", type: "String" }
        ]
      },
      sessions[0] // nodes[1].sessionId
    );
    android.setViewModel(
      {
        import: ["java.util.Map"],
        variable: [
          { name: "map", type: "Map&lt;String, String>" }
        ]
      },
      sessions[1] // nodes[2].sessionId
    );
  });

::

  squared.parseDocument({
    element: "main",
    enabledViewModel: true,
    dataBindableElements: [
      {
        selector: "#first_name",
        namespace: "android", // "android" is default
        attr: "text",
        expression: "user.firstName"
      },
      {
        selector: "#last_name",
        attr: "text",
        expression: "user.lastName"
      },
      {
        selector: "#remember_me",
        attr: "checked",
        expression: "user.rememberMe",
        twoWay: true
      }
    ],
    data: {
      viewModel: {
        import: ["java.util.List"],
        variable: [
          { name: "user", type: "com.example.User" }
        ]
      }
    }
  });

Inline
======

Creating a view model inline can be more convenient for simple layouts. JavaScript is the recommended solution when ``parseDocument`` is called multiple times.

.. code-block:: none

  data-viewmodel-{namespace}-{attribute} -> data-viewmodel-android-text

These two additional output parameters are required when using the **data-viewmodel** prefix.

.. code-block:: html
  :emphasize-lines: 5

  <div id="main">
    <label>Name:</label>
    <input id="first_name" type="text" data-viewmodel-android-text="user.firstName" />
    <input id="last_name" type="text" data-viewmodel-android-text="user.lastName" />
    <input id="remember_me" type="checkbox" data-viewmodel-android-checked="=user.rememberMe" />
  </div>

.. tip:: Use "=" to create a two-way binding.

.. code-block:: xml
  :caption: Output
  :emphasize-lines: 16,20,23

  <layout>
    <data>
      <import type="java.util.Map" />
      <import type="java.util.List" />
      <variable name="user" type="com.example.User" />
      <variable name="list" type="List&lt;String&gt;" />
      <variable name="map" type="Map&lt;String, String&gt;" />
      <variable name="index" type="int" />
      <variable name="key" type="String" />
    </data>
    <LinearLayout android:id="@+id/main">
      <TextView android:text="Name:" />
      <EditText
        android:id="@+id/first_name"
        android:inputType="text"
        android:text="@{user.firstName}" />
      <EditText
        android:id="@+id/last_name"
        android:inputType="text"
        android:text="@{user.lastName}" />
      <CheckBox
        android:id="@+id/remember_me"
        android:checked="@={user.rememberMe}" />
    </LinearLayout>
  </layout>

.. [#] https://developer.mozilla.org/docs/Web/API/HTMLElement/dataset