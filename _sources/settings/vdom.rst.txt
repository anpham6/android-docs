====
VDOM
====

Interface
=========

.. code-block:: typescript

  import type { UserSettings } from "./interface";

Example usage
=============

.. code-block::
  :caption: Global

  squared.settings = {
    createElementMap: true,
    pierceShadowRoot: false,
    adaptStyleMap: false,
    showErrorMessages: false
  };

.. code-block::
  :caption: Global (unused)

  squared.settings = {
    builtInExtensions: []
  };

.. tip:: Frequent modifications to the *DOM* use the setting :code:`createElementMap = false`.