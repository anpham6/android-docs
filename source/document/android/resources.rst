=========
Resources
=========

Projects can include additional values which may have missed detection and are required during compilation.

Interface
=========

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
=============

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

.. seealso:: :doc:`References </references>` for any non-browser named definitions.