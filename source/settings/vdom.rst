====
VDOM
====

.. highlight:: typescript

Interface
=========

::

  import type { UserSettings } from "./interface";

Example usage
=============

.. code-block::
  :caption: Global

  squared.settings = {
    createElementMap: true,
    pierceShadowRoot: false,
    showErrorMessages: false
  };

.. code-block::
  :caption: Global (unused)

  squared.settings = {
    builtInExtensions: []
  };

.. tip:: Frequent modifications to the DOM use the setting ``createElementMap = false``.