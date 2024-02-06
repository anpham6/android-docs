Extensions
==========

Layout rendering can be customized using extensions as the program was built to be nearly completely modular. Some of the common layouts already have built-in extensions which you can load or unload based on your preference.

.. code-block::
  :caption: Create

  class Sample extends squared.base.ExtensionUI {
    options = {
      attributeName: [],
      floatPrecision: 3
    };

    constructor(name, framework = 0, options = {}) {
      super(name, framework, options);
    }

    processNode(node) {
      const data = this.project.get(node.element, node.localSettings.projectId);
      if (data) {
          node.each((child, index) => child.element.title = data[index]);
      }
    }
  }

.. code-block::
  :caption: Install

  const sample = new Sample("widget.example.com", 2 /* APP_FRAMEWORK.ANDROID */, { tagNames: ["span", "li"], dependencies: ["android.substitute"] });
  squared.add(sample);
  // OR
  squared.add([sample, { attributeName: ["width", "height"] }]);

.. code-block::
  :caption: Configure

  squared.attr("widget.example.com", "floatPrecision", 2); // typeof is enforced and will only set existing attributes

.. code-block::
  :caption: Add project data

  const ext = squared.get("widget.example.com");
  ext.project.set(element, await fetch(url), "project-1"); // Map interface with optional "projectId" argument

Some extensions have a few settings which can be configured. The default settings usually achieve the best overall rendering accuracy without noticeably affecting performance.