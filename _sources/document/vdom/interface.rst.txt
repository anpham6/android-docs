=========
Interface
=========

.. highlight::  typescript

.. code-block::
  :emphasize-lines: 39-40,190,205-206,224

  class Container<T> implements Iterable<T> {
      children: T[];
      [Symbol.iterator](): IterableIterator<T>;
      item(index: number, value?: T): T | undefined;
      add(item: T): this;
      addAll(list: T[] | Container): this;
      remove(item: T): T | undefined;
      removeAll(list: T[] | Container): T[];
      retainAs(list: T[]): this;
      each(predicate: IteratorPredicate<T, void>, options?: ContainerEachOptions): this;
      every(predicate: IteratorPredicate<T, unknown>, options?: ContainerRangeOptions): boolean;
      removeIf(predicate: IteratorPredicate<T, unknown>, options?: ContainerRemoveIfOptions<T> | IteratorPredicate<T, boolean>): T[];
      find(predicate: IteratorPredicate<T, unknown>, options?: ContainerFindOptions<T>): T | undefined;
      includes(item: T, cascade: boolean): boolean;
      includes(item: T, options?: ContainerIncludesOptions<T>): boolean;
      cascade(predicate?: IteratorPredicate<T, unknown>, options?: ContainerCascadeOptions<T> | IteratorPredicate<T, boolean>): T[];
      map(predicate: IteratorPredicate<T, unknown>): unknown[];
      contains(...items: T[]): boolean;
      clear(): this;
      isEmpty(): boolean;
      size(): number;
      toArray(): T[];
      constructor(children?: T[]);
  }

  class Node extends Container<Node> {
      static readonly TEXT_STYLE: string[];
      static boxValueOf(node: Node, attr: BoxModelAttr, options?: CssUnitOptions): number;
      static sanitizeCss(element: HTMLElement, input: CssStyleMap, writingMode?: string, output?: CssStyleMap): CssStyleMap;
      readonly id: number;
      readonly sessionId: string;
      setParent(parent: Node | null, depth?: number, index?: number): void;
      syncWith(sessionId?: string, cache?: boolean): boolean;
      saveAsInitial(): void;
      elementAttr(attr: string, value: unknown): unknown;
      data(name: string | symbol, attr: string | symbol, value?: unknown, overwrite?: boolean): unknown;
      unsetCache(...attrs: (CssStyleAttr | keyof CacheValue)[]): void;
      unsetState(...attrs: (keyof CacheState<Node>)[]) : void;
      resetCache(): void;
      resetState(): void;
      ascend(options?: AscendParameterOptions<Node, NodeParentAttr>, attr?: boolean | string | ((item: Node) => boolean), error?: (item: Node) => boolean): Node[];
      ascendOne(options?: AscendParameterOptions<Node, NodeParentAttr>, attr?: boolean | string | ((item: Node) => boolean), error?: (item: Node) => boolean): Node | undefined;
      descend(options?: DescendParameterOptions<Node>): Node[];
      descendOne(options?: DescendParameterOptions<Node>): Node | undefined;
      intersectX(rect: BoxRectDimension, options?: CoordsXYOptions): boolean;
      intersectY(rect: BoxRectDimension, options?: CoordsXYOptions): boolean;
      withinX(rect: BoxRectDimension, options?: OffsetXYOptions): boolean;
      withinY(rect: BoxRectDimension, options?: OffsetXYOptions): boolean;
      outsideX(rect: BoxRectDimension, options?: OffsetXYOptions): boolean;
      outsideY(rect: BoxRectDimension, options?: OffsetXYOptions): boolean;
      as(target: typeof Element): InstanceType<typeof Element> | null;
      css(attr: CssStyleAttr, value?: string, cache?: boolean): string;
      cssInitial(attr: CssStyleAttr, options?: CssInitialOptions): string;
      cssAny(attr: CssStyleAttr, values: string[], options?: CssAnyOptions): boolean;
      cssAscend(attr: CssStyleAttr, options?: CssAscendOptions): string;
      cssSort(attr: CssStyleAttr, options?: CssSortOptions): Node[];
      cssSpecificity(attr: CssStyleAttr): Specificity | undefined;
      cssParent(attr: CssStyleAttr, value?: string, cache?: boolean): string;
      cssUnit(attr: CssStyleAttr, options?: CssUnitOptions): number;
      cssAsTuple(...attrs: CssStyleAttr[]): string[];
      cssAsObject(...attrs: CssStyleAttr[]): CssStyleMap;
      cssApply(values: CssStyleMap, overwrite?: boolean, cache?: boolean): this;
      cssCopy(node: Node, ...attrs: CssStyleAttr[]): void;
      cssCopyIfEmpty(node: Node, ...attrs: CssStyleAttr[]): void;
      cssTry(attr: CssStyleAttr, value: string, callback?: (this: Node, ...args: unknown[]) => void): boolean;
      cssTryAll(attrs: CssStyleMap, callback?: (this: Node, ...args: unknown[]) => void): CssStyleMap | boolean;
      cssFinally(attrs: CssStyleAttr | CssStyleMap): void;
      parseUnit(value: unknown, options?: NodeParseUnitOptions): number;
      withDisplay(type: boolean, ...values: string[]): boolean;
      withDisplay(...values: string[]): boolean;
      withLayout(outside: "block" | "inline" | number, type: number, ...values: string[]): boolean;
      withLayout(outside: "block" | "inline" | number, ...values: string[]): boolean;
      parseColor(value: string, opacity: number): ColorRGB | null;
      parseColor(value: string, options?: NodeParseColorOptions): ColorRGB | null;
      convertUnit(value: unknown, options: NodeConvertUnitOptions): string;
      convertUnit(value: unknown, unit?: string, options?: NodeConvertUnitOptions): string;
      has(attr: CssStyleAttr, options?: HasOptions): boolean;
      hasUnit(attr: CssStyleAttr, percent: boolean): boolean;
      hasUnit(attr: CssStyleAttr, options?: HasUnitOptions | boolean): boolean;
      toInt(attr: CssStyleAttr, options: CssInitialOptions): number;
      toInt(attr: CssStyleAttr, fallback?: number, options?: CssInitialOptions): number;
      toFloat(attr: CssStyleAttr, options: CssInitialOptions): number;
      toFloat(attr: CssStyleAttr, fallback?: number, options?: CssInitialOptions): number;
      toElementInt(attr: string, fallback?: number): number;
      toElementFloat(attr: string, fallback?: number): number;
      toElementBoolean(attr: string, fallback?: boolean): boolean;
      toElementString(attr: string, fallback?: string): string;
      setBounds(cache?: boolean): BoxRectDimension | null;
      resetBounds(recalibrate?: boolean): void;
      getContainerSize(options?: NodeUnitOptions): number;
      flex(attr: "inline" | "row" | "column" | "reverse" | "wrap" | "wrapReverse", parent?: boolean | Node): boolean;
      flex(attr: "alignContent" | "justifyContent" | "basis" | "alignSelf" | "justifySelf", parent?: boolean | Node): string;
      flex(attr: "grow" | "shrink" | "order", parent?: boolean | Node): number;
      flex(attr: string, parent?: boolean | Node): boolean | number | string;
      min(attr: string, options?: MinMaxOptions): Node;
      max(attr: string, options?: MinMaxOptions): Node;
      querySelector(value: string): Node | null;
      querySelectorAll(value: string, queryMap?: Node[], queryRoot?: HTMLElement | null): Node[];
      ancestors(value?: string | AscendParameterOptions<Node, NodeParentAttr>, options?: AscendParameterOptions<Node, NodeParentAttr>): Node[];
      ancestorsOne(value?: string | AscendParameterOptions<Node, NodeParentAttr>, options?: AscendParameterOptions<Node, NodeParentAttr>): Node | undefined;
      descendants(value?: string | DescendParameterOptions<Node>, options?: DescendParameterOptions<Node>): Node[];
      descendantsOne(value?: string | DescendParameterOptions<Node>, options?: DescendParameterOptions<Node>): Node | undefined;
      siblings(value?: string | SiblingsParameterOptions<Node>, options?: SiblingsParameterOptions<Node>): Node[];
      siblingsOne(value?: string | SiblingsParameterOptions<Node>, options?: SiblingsParameterOptions<Node>): Node | undefined;
      boxOf(attr: keyof (BoxRect & Dimension)): number;
      valueOf(attr: CssStyleAttr, options?: CssInitialOptions): string;
      get documentRoot(): boolean;
      get parent(): Node | null;
      get shadowRoot(): boolean;
      get shadowHost(): ShadowRoot | null;
      get depth(): number;
      get childIndex(): number;
      get naturalChildren(): Node[];
      get naturalElements(): Node[];
      get dir(): TextDirection;
      get textBounds(): BoxRectDimension | null;
      get box(): BoxRectDimension;
      get bounds(): BoxRectDimension;
      get linear(): BoxRectDimension;
      get element(): Element | null;
      get elementId(): string;
      get tagName(): string;
      get naturalChild(): boolean;
      get naturalElement(): boolean;
      get parentElement(): Element | null;
      get htmlElement(): boolean;
      get styleElement(): boolean;
      get imageElement(): boolean;
      get svgElement(): boolean;
      get flexElement(): boolean;
      get gridElement(): boolean;
      get textElement(): boolean;
      get tableElement(): boolean;
      get inputElement(): boolean;
      get buttonElement(): boolean;
      get mathElement(): boolean;
      get voidElement(): boolean;
      get pseudoElement(): boolean;
      get pseudoElt(): PseudoElt | "";
      get documentBody(): boolean;
      get dataset(): DOMStringMap;
      get centerAligned(): boolean;
      get rightAligned(): boolean;
      get bottomAligned(): boolean;
      get width(): number;
      get height(): number;
      get hasWidth(): boolean;
      get hasHeight(): boolean;
      get lineHeight(): number;
      get display(): string;
      get positionStatic(): boolean;
      get positionRelative(): boolean;
      get positionFixed(): boolean;
      get top(): number;
      get right(): number;
      get bottom(): number;
      get left(): number;
      get borderTopWidth(): number;
      get borderRightWidth(): number;
      get borderBottomWidth(): number;
      get borderLeftWidth(): number;
      get marginTop(): number;
      get marginRight(): number;
      get marginBottom(): number;
      get marginLeft(): number;
      get paddingTop(): number;
      get paddingRight(): number;
      get paddingBottom(): number;
      get paddingLeft(): number;
      get outlineWidth(): number;
      get inline(): boolean;
      get inlineStatic(): boolean;
      get inlineText(): boolean;
      get block(): boolean;
      get blockStatic(): boolean;
      get plainText(): boolean;
      get textContent(): string;
      get lineBreak(): boolean;
      get pageFlow(): boolean;
      get autoMargin(): AutoMargin;
      get floating(): boolean;
      get float(): FloatDirectionAttr;
      get floatClear(): ClearDirectionAttr;
      get baseline(): boolean;
      get multiline(): boolean;
      get contentBox(): boolean;
      get contentBoxWidth(): number;
      get contentBoxHeight(): number;
      get borderBoxElement(): boolean;
      get flexdata(): FlexData;
      get flexbox(): FlexBox;
      get zIndex(): number;
      get opacity(): number;
      get backgroundColor(): string;
      get backgroundImage(): string;
      get visibleStyle(): VisibleStyle;
      get fontSize(): number;
      get verticalAlign(): number;
      get actualParent(): Node | null;
      get absoluteParent(): Node | null;
      get wrapperOf(): Node | null;
      get actualWidth(): number;
      get actualHeight(): number;
      get actualDimension(): Dimension;
      get leftPos(): number;
      get rightPos(): number;
      get containerDimension(): Readonly<ContainerDimension>[] | null;
      get containerHeight(): boolean;
      get percentWidth(): number;
      get percentHeight(): number;
      get aspectRatio(): [number, number] | null;
      get firstChild(): Node | null;
      get lastChild(): Node | null;
      get firstElementChild(): Node | null;
      get lastElementChild(): Node | null;
      get previousSibling(): Node | null;
      get nextSibling(): Node | null;
      get previousElementSibling(): Node | null;
      get nextElementSibling(): Node | null;
      get attributes(): StringMap;
      get checked(): boolean | null;
      get boundingClientRect(): DOMRect | null;
      get preserveWhiteSpace(): boolean;
      get nowrapWhiteSpace(): boolean;
      get style(): CSSStyleDeclaration;
      get cssStyle(): CssStyleMap;
      get textStyle(): CssStyleMap;
      get writingMode(): string;
      get elementData(): ElementData | null;
      get initial(): InitialData<Node>;
      constructor(id: number, sessionId?: string, element?: Element, children?: Node[]);
  }

Changelog
=========

.. versionadded:: 5.3.0

  - *Node* property getters **leftPos** | **rightPos** for direction precedence was created.
  - *Node* property getter **nowrapWhiteSpace** for :alt:`text-wrap` detection was created.
  - *Node* method **resetCache** for all property cache values was created.
  - *Node* method **resetState** for all property state values was created.

.. versionadded:: 5.2.1

  - *Node* method **as** for element casting was created.

.. versionadded:: 5.2.0

  - *Node* method **withDisplay** for group display values was created.
  - *Node* method **withLayout** for display outside and inside values was created.
  - *Node* method **parseColor** for color scheme detection was created.
  - *Node* method **flex** for parsed Flexbox values was created.
  - *Node* property getter **mathElement** for MathML elements was created.
  - *Container* methods **removeIf** | **cascade** argument **options** with :alt:`IteratorPredicate` was amended.

.. deprecated:: 5.2.0

  - *Node* property getter **flexdata** as :alt:`Node.flex(attr, parent)` is pending removal.

.. code-block::
  :caption: squared.lib.js

  class Container<T> {
      addAt(index: number, ...items: T[]): this;
      removeAt(index: number): T | undefined;
      sortBy(...attrs: [...string[], boolean?]): this;
      iterator(): ListIterator<T>;
  }