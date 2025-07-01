====
vdom
====

.. module:: vdom

.. function:: userSettings(value)

  Applies object values to |Application| property ``userSettings``. (ESM only)

  :param value: PlainObject with settings overrides
  :type value: |UserSettings|

  Usage::

    import { userSettings } from 'squared/vdom.js';

    userSettings({
      pierceShadowRoot: true,
      adaptStyleMap: true
    });

.. |Application| replace:: :ref:`Application <references-squared-base>`
.. |UserSettings| replace:: :ref:`UserSettings <references-squared-base-application>`