======
Chrome
======

Uses the :doc:`vdom` framework as the element base but can also export any used resources for further processing. It is adequate for most single page applications and gives you the ability to preview your application before building a working copy of it.

Example usage
=============

.. code-block:: html

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/squared.base.min.js"></script>
  <script src="/dist/chrome.framework.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", async () => {
      squared.setFramework(chrome, {/* settings */});

      await squared.save(); // Uses defaults from settings
      /* OR */
      await squared.saveAs("android.zip", /* options */);
      /* OR */
      await squared.copyTo("/path/project", /* options */);
      /* OR */
      await squared.appendTo("/path/to/android.7z", /* options */);
    });
  </script>

.. code-block::
  :caption: Observe element

  await squared.copyTo("/path/project", { useOriginalHtmlPage: false, observe: true }).then(() => {
    squared.observe(); // Watch all events
    /* OR */
    squared.observe({
      subtree: true,
      childList: true,
      attributes: true,
      characterData: true,
      attributeOldValue: true,
      characterDataOldValue: true
    });
    /* OR */
    squared.observe(false);
  });