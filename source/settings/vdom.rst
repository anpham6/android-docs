VDOM
====

Interface
---------

.. code-block:: typescript

  import type { UserSettings } from "./interface";

Example usage
-------------

.. code-block:: typescript
  :caption: Global

  squared.settings = {
    createElementMap: true,
    pierceShadowRoot: false,
    showErrorMessages: false
  };

.. code-block:: typescript
  :caption: Global (unused)

  squared.settings = {
    builtInExtensions: []
  };

.. tip:: Frequent modifications to the DOM use the setting ``createElementMap = false``.