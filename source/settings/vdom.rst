vdom
====

Interface
---------

.. code-block:: typescript

  import type { UserResourceSettings } from "./interface";

Example usage
-------------

.. code-block:: typescript
  :caption: Global

  squared.settings = {
    createElementMap: true,
    pierceShadowRoot: false, // Native document.querySelector does not enter shadowRoot elements
    showErrorMessages: false
  };

.. code-block:: typescript
  :caption: Global (unused)

  squared.settings = {
    builtInExtensions: []
  };

.. tip:: Frequent modifications to the DOM use the setting ``createElementMap = false``.