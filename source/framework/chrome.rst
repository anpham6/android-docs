Chrome
======

You have the same features as the :doc:`vdom` framework but you can also bundle assets using query selector syntax. It is adequate for most applications and gives you the ability to preview your application before building a working copy of it.

Example usage
-------------

.. code-block:: html

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/squared.base.min.js"></script>
  <script src="/dist/chrome.framework.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", async () => {
      squared.setFramework(chrome, /* settings */);

      await squared.save(); // Uses defaults from settings
      /* OR */
      await squared.saveAs(/* archive filename */, /* options */);
      /* OR */
      await squared.copyTo(/* directory */, /* options */);
      /* OR */
      await squared.appendTo(/* archive location */, /* options */);
    });
  </script>

.. code-block::
  :caption: Observe element [#]_

  await squared.copyTo(/* directory */, { useOriginalHtmlPage: false, observe: true }).then(() => {
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

.. [#] https://developer.mozilla.org/docs/Web/API/MutationObserver/observe#options