====
vdom
====

.. module:: vdom

.. function:: userSettings([value, loadName, saveName])

  Applies object values to |Application| property ``userSettings``. (ESM only)

  :param value: PlainObject with settings overrides
  :type value: |UserSettings|
  :param string loadName: Restore previously saved settings from local storage
  :param string saveName: Store current settings into local storage

  Usage::

    import { userSettings } from "squared/vdom.js";

    userSettings({
      pierceShadowRoot: true,
      adaptStyleMap: true
    });

  Alternate::

    const settings = userSettings();
    settings.pierceShadowRoot = true;

.. |Application| replace:: :ref:`Application <references-squared-base>`
.. |UserSettings| replace:: :ref:`UserSettings <references-squared-base-application>`