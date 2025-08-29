=========
Interface
=========

squared
=======

.. highlight:: typescript

.. rst-class:: section-caption

.. code-block::
  :caption: Serve *(API)*

  function setHostname(value: string): void;
  function setEndpoint(name: string, value: string): void;
  function setLocalAddress(...values: (string | URL)[]): void;
  function auth(token: string): void;

  function kill(timeout: string): Promise<number>;
  function kill(pid?: number, timeout?: number | string): Promise<number>;

  function broadcast(callback: BroadcastMessageCallback, socketId: string): boolean;
  function broadcast(callback: BroadcastMessageCallback, options: FileBroadcastOptions): boolean;

.. rst-class:: section-caption

.. code-block::
  :caption: Framework

  function setFramework(value: Application, options?: PlainObject, cache?: boolean): void;
  function setFramework(value: Application, loadName: string, cache?: boolean): void;
  function setFramework(value: Application, options?: PlainObject, saveName?: string, cache?: boolean): void;

  function extend(functionMap: PlainObject, framework?: number): void;
  function clear(): void;

.. rst-class:: section-caption

.. code-block::
  :caption: Extensions

  function add(...values: ExtensionRequestObject[]): number;
  function remove(...values: ExtensionRequest[]): number;
  function get(value: string): Extension | undefined;
  function get(...values: string[]): Extension[];
  function attr(name: ExtensionRequest, attrName: string, value?: unknown, append?: boolean): unknown;

  function apply(value: ExtensionRequest, saveAs: string): boolean;
  function apply(value: ExtensionRequest, options: PlainObject, saveAs?: string): boolean;

.. rst-class:: section-caption

.. code-block::
  :caption: Session *(create)*

  function prefetch(type: "css", all: boolean, ...targets: (Document | ShadowRoot)[]): Promise<PrefetchItem[]>;
  function prefetch(type: "css", ...targets: (Document | ShadowRoot)[]): Promise<PrefetchItem[]>;
  function prefetch(type: "javascript" | "image" | "svg", all: boolean, ...targets: string[]): Promise<PrefetchItem[]>;
  function prefetch(type: "javascript" | "image" | "svg", ...targets: string[]): Promise<PrefetchItem[]>;

  function parseDocument(...elements: RootElement[]): Promise<Node | Node[] | void>;
  function parseDocumentSync(...elements: RootElement[]): Node | Node[] | undefined;

.. rst-class:: section-caption

.. code-block::
  :caption: Session *(modify)*

  function findDocumentNode(value: HTMLElement | string, projectId?: string): Node | undefined;
  function findDocumentNode(value: HTMLElement | string, all: true, projectId?: string): Node[];

  function latest(value = 1): string;
  function latest(value: 1 | -1): string;
  function latest(value: number): string[];

  function close(projectId?: string): Promise<boolean>;
  function reset(projectId?: string): void;

.. rst-class:: section-caption

.. code-block::
  :caption: Session *(API)*

  function save(): FileActionResult;
  function save(timeout: number): FileActionResult;
  function save(projectId: string, timeout: number): FileActionResult;
  function save(projectId: string, broadcastId?: string): FileActionResult;

  function saveAs(value: string, setting: string): FileActionResult;
  function saveAs(value: string, options?: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function appendTo(value: string, setting: string): FileActionResult;
  function appendTo(value: string, options?: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function copyTo(value: string | string[], setting: string): FileActionResult;
  function copyTo(value: string | string[], options?: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function saveFiles(value: string, setting: string): FileActionResult;
  function saveFiles(value: string, options: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function appendFiles(value: string, setting: string): FileActionResult;
  function appendFiles(value: string, options: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function copyFiles(value: string | string[], setting: string): FileActionResult;
  function copyFiles(value: string | string[], options: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function toString(projectId?: string): string;

.. rst-class:: section-caption

.. code-block::
  :caption: DOM

  function getElementById(value: string, sync: true, cache = true): Node | null;
  function getElementById(value: string, sync?: false, cache = true): Promise<Node | null>;

  function querySelector(value: string, sync: true, cache = true): Node | null;
  function querySelector(value: string, sync?: false, cache = true): Promise<Node | null>;

  function querySelectorAll(value: string, sync: true, cache = true): Node[];
  function querySelectorAll(value: string, sync?: false, cache = true): Promise<Node[] | null>;

  function fromElement(element: HTMLElement | string, sync: true, cache?: boolean): Node | null;
  function fromElement(element: HTMLElement | string, sync?: false, cache?: boolean): Promise<Node | null>;

  function fromNode(node: Node, sync: true, cache?: boolean): Node | null;
  function fromNode(node: Node, sync?: false, cache?: boolean): Promise<Node | null>;

.. rst-class:: section-caption

.. code-block::
  :caption: ESM

  function userSettings(): PlainObject;
  function userSettings(value: PlainObject, loadName?: string, saveName?: string): void;

.. rst-class:: section-caption

.. code-block::
  :caption: Observe

  function observe(enable = true): void;
  function observe(options: MutationObserverInit): void;

  function observeSrc(element: HTMLElement | string, options: FileObserveOptions): Promise<ObserveSocket | ObserveSocket[]>;
  function observeSrc(element: HTMLElement | string, callback: (ev: MessageEvent, target: HTMLElement) => void, options?: FileObserveOptions): Promise<ObserveSocket | ObserveSocket[]>;

android
=======

::

  interface AppFramework {
      setViewModel(data: AppViewModel, sessionId?: string): void;
      setViewModelByProject(data: AppViewModel, projectId?: string): void;
      addDependency(group: string, name: string, version?: number | string, type?: number | boolean, overwrite?: boolean): string;
      addDependencyByProject(projectId: string, group: string, name: string, version?: number | string, type?: number | boolean, overwrite?: boolean): string;
      addFontProvider(authority: string, package: string, certs: string[], webFonts: string | FontProviderFonts): boolean | Promise<boolean>;
      addXmlNs(name: string, uri: string): void;
      customize(api: number, widget: string, options: Record<string, StringMap>): Record<string, StringMap> | undefined;
      loadCustomizations(name: string): void;
      saveCustomizations(name: string): void;
      resetCustomizations(): void;
      setResolutionByDeviceName(value: string): boolean;
      getLocalSettings(): ControllerSettingsUI;
      removeObserver(element: HTMLElement): boolean;
  }

chrome
======

::

  interface AppFramework {
      removeObserver(element: HTMLElement): boolean;
  }