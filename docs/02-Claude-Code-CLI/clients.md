---
source: https://modelcontextprotocol.io/clients.md
downloaded: 2026-02-02
---

# Example Clients

> A list of applications that support MCP integrations

export const FEATURES = ["Resources", "Prompts", "Tools", "Discovery", "Sampling", "Roots", "Elicitation", "Instructions", "Tasks", "Apps"];


export const filterStore = {
  state: {
    selectedFeatures: [],
    searchText: "",
    visibleCount: 0,
    totalCount: 0
  },
  listeners: new Set(),
  setState(updater) {
    if (typeof updater === "function") {
      this.state = {
        ...this.state,
        ...updater(this.state)
      };
    } else {
      this.state = {
        ...this.state,
        ...updater
      };
    }
    this.listeners.forEach(fn => fn(this.state));
  },
  subscribe(fn) {
    this.listeners.add(fn);
    return () => this.listeners.delete(fn);
  }
};


export const useFilterStore = () => {
  const [state, setState] = useState(filterStore.state);
  useEffect(() => filterStore.subscribe(setState), []);
  return state;
};


export const useFilter = ({name, supports}) => {
  const {selectedFeatures, searchText} = useFilterStore();
  const isVisible = name.toLowerCase().includes(searchText.toLowerCase()) && selectedFeatures.every(feature => supports?.includes(feature));
  useEffect(() => {
    filterStore.setState(s => ({
      totalCount: s.totalCount + 1
    }));
    return () => filterStore.setState(s => ({
      totalCount: s.totalCount - 1
    }));
  }, []);
  useEffect(() => {
    if (isVisible) {
      filterStore.setState(s => ({
        visibleCount: s.visibleCount + 1
      }));
      return () => filterStore.setState(s => ({
        visibleCount: s.visibleCount - 1
      }));
    }
  }, [isVisible]);
  return isVisible;
};


export const ClientFilter = () => {
  const {selectedFeatures, searchText, visibleCount, totalCount} = useFilterStore();
  useEffect(() => {
    filterStore.setState({
      selectedFeatures: [],
      searchText: ""
    });
  }, []);
  const toggleFeature = feature => {
    const newFeatures = selectedFeatures.includes(feature) ? selectedFeatures.filter(f => f !== feature) : [...selectedFeatures, feature];
    filterStore.setState({
      selectedFeatures: newFeatures
    });
  };
  const clearFilters = () => {
    filterStore.setState({
      selectedFeatures: [],
      searchText: ""
    });
  };
  const hasFilters = selectedFeatures.length > 0 || searchText.length > 0;
  return <div className="p-4 border border-gray-200 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800/50">
      <div className="flex items-center justify-between">
        <span className="font-bold text-gray-700 dark:text-gray-300">
          Showing {visibleCount} of {totalCount} clients
        </span>
        {hasFilters && <button onClick={clearFilters} className="text-sm cursor-pointer px-3 py-1 rounded-full bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors">
            <Icon icon="xmark" iconType="solid" size={16} /> Clear filters
          </button>}
      </div>
      <div className="mt-3">
        <input type="text" placeholder="Search clients by name..." value={searchText} onChange={e => filterStore.setState({
    searchText: e.target.value
  })} className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent" />
      </div>
      <div className="mt-4">
        <div className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
          Filter by features:
        </div>
        <div className="flex flex-wrap gap-2">
          {FEATURES.map(feature => <button key={feature} onClick={() => toggleFeature(feature)} className={`flex items-center gap-1.5 px-2 py-1 rounded text-sm transition-colors cursor-pointer ${selectedFeatures.includes(feature) ? 'bg-primary/10 text-primary dark:bg-gray-700 dark:text-gray-100' : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800'}`}>
              <Icon icon={selectedFeatures.includes(feature) ? "square-check" : "square"} iconType={selectedFeatures.includes(feature) ? "solid" : "regular"} size={16} />
              {feature}
            </button>)}
        </div>
      </div>
    </div>;
};


export const McpClient = ({name, homepage, supports, sourceCode, instructions, children}) => {
  const slug = name.toLowerCase().replace(/[().\s-]+/g, "-").replace(/^-|-$/g, "");
  if (homepage?.match(/^https:\/\/github\.com\/[^/]+\/[^/]+/)) {
    sourceCode ??= homepage;
  }
  const instructionsLinks = Array.isArray(instructions) ? <>
        <strong>Configuration instructions:</strong>{" "}
        {instructions.map(([text, url], i) => [i > 0 && ", ", <a href={url} target="_blank" rel="noopener noreferrer">{text}</a>])}
      </> : <a href={instructions} target="_blank" rel="noopener noreferrer">
        Configuration instructions
      </a>;
  const [expanded, setExpanded] = useState(false);
  const [hasOverflow, setHasOverflow] = useState(false);
  const contentRef = useRef(null);
  const isVisible = useFilter({
    name,
    supports
  });
  useEffect(() => {
    const el = contentRef.current;
    if (el) {
      setHasOverflow(el.scrollHeight > el.clientHeight);
    }
  }, []);
  if (!isVisible) return null;
  return <div id={slug} className="group mt-8 scroll-mt-32">
      <div className="border border-gray-200 dark:border-gray-700 rounded-lg overflow-hidden">
        <div className="px-4 py-3 border-b border-gray-200 dark:border-gray-700">
          <div className="flex items-center gap-2">
            <a href={homepage} className="border-0 text-xl font-semibold text-primary underline" target="_blank" rel="noopener noreferrer">
              {name}
            </a>
            <a href={`#${slug}`} className="ml-auto border-0 opacity-0 group-hover:opacity-100 text-xl text-gray-400 hover:text-gray-600" aria-label={`Link to ${name}`}>
              #
            </a>
          </div>
          {supports && <div className="flex items-start gap-1.5 mt-2 text-base">
              <span className="flex items-center h-[1lh]">
                <Icon icon="check" iconType="solid" size={18} />
              </span>
              <span><strong>Supports:</strong> {supports}</span>
            </div>}
          {sourceCode && <div className="flex items-start gap-1.5 mt-2 text-base">
              <span className="flex items-center h-[1lh]">
                <Icon icon="code" iconType="solid" size={18} />
              </span>
              <span>
                <a href={sourceCode} target="_blank" rel="noopener noreferrer">
                  Open source
                </a>
              </span>
            </div>}
          {instructions && <div className="flex items-start gap-1.5 mt-2 text-base">
              <span className="flex items-center h-[1lh]">
                <Icon icon="gear" iconType="solid" size={18} />
              </span>
              <span>
                {instructionsLinks}
              </span>
            </div>}
        </div>
        <div className="relative">
          <div ref={contentRef} className={`px-4 py-4 prose ${!expanded ? "max-h-[7rem] overflow-hidden" : "pb-8"}`}>
            {children}
          </div>
          {hasOverflow && <button onClick={() => setExpanded(!expanded)} className={`absolute bottom-0 left-0 right-0 flex justify-center items-end pb-1 cursor-pointer text-gray-400 hover:text-gray-600 ${!expanded ? "h-16 bg-gradient-to-t from-white dark:from-gray-900 to-transparent" : "h-8"}`}>
              <span className={`${expanded ? "rotate-180" : ""} bg-white/60 dark:bg-gray-900/60 rounded-full`}>
                <Icon icon="chevron-down" iconType="solid" size={18} />
              </span>
            </button>}
        </div>
      </div>
    </div>;
};


This page provides an overview of applications that support the Model Context Protocol (MCP). Each client may support different MCP features, allowing for varying levels of integration with MCP servers.

<Note>
  This list is maintained by the community. If you notice any inaccuracies or would like to add or update information about MCP support in your application, please [submit a pull request](https://github.com/modelcontextprotocol/modelcontextprotocol/pulls).
</Note>

[Content continues with all client details as fetched...]
