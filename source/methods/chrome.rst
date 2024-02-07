======
chrome
======

.. module:: chrome

.. function:: removeObserver(element)

  Forwards the target element to |Application| which will stop it from being monitored for changes.

  :param element: HTMLElement instance

  :returns: boolean

  Usage::

    await squared.parseDocument(document.body);

    await squared.copyTo("/path/project", { useOriginalHtmlPage: false, observe: true }).then(() => {
      squared.observe();
    });

    chrome.removeObserver(document.body);

.. |Application| replace:: :any:`Application <references-squared-base>`