Resources
=========

Projects can include additional values that are required during compilation which might not have been detected.

Interface
---------

.. code-block:: typescript

  class Resource {
      static addTheme(resourceId: number, theme: ThemeAttribute, options?: AddThemeOptions): boolean;
      static addString(resourceId: number, value: string, name?: string, options?: AddStringOptions): string;
      static addArray(resourceId: number, name: string, items: string[], options?: AddArrayOptions): string;
      static addImage(resourceId: number, images: Record<string, string>, options?: AddImageOptions): string;
      static addColor(resourceId: number, value: ColorRGB | string, transparency?: boolean): string;
      static addDimen(resourceId: number, name: string, value: string): string;
  }

Example usage
-------------

.. code-block::

  squared.parseDocument().then(node => {
    const resourceId = node.localSettings.resourceId;
    android.base.Resource.addString(resourceId, "123", "title", { isText: true });
    android.base.Resource.addArray(resourceId, "list_1", ["1", "2", "3"], { type: 8 }); // RESOURCE.STRING_ARRAY
    android.base.Resource.addColor(resourceId, "#000000");
    android.base.Resource.addDimen(resourceId, "border_width", "1px");
    android.base.Resource.addTheme(resourceId,
      {
        name: "AppTheme",
        items: { "android:windowTranslucentStatus": "true" }
      },
      { pathname: "res/values", filename: "theme.xml" }
    );
  });

References
----------

.. rst-class:: block-list

https://unpkg.com/squared/types/dom.d.ts
  | ColorRGB

.. rst-class:: block-list

https://unpkg.com/squared/types/android/squared.d.ts
  | RESOURCE

.. rst-class:: block-list

https://unpkg.com/squared/types/android/application.d.ts
  | ThemeAttribute

.. rst-class:: block-list

https://unpkg.com/squared/types/android/options.d.ts
  | AddArrayOptions
  | AddImageOptions
  | AddStringOptions
  | AddThemeOptions