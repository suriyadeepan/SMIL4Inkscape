# SMIL

**Synchronized Multimedia Integration Language**


## SVG Boiler Plate

```xml
<?xml version="1.0"?>
<svg xmlns="http://www.w3.org/2000/svg">
  <title>Title goes here</title>
  <desc>Description of svg goes here</desc>

	<!---Elements of svg, here--->

</svg>
```

## Dynamic Rectangle

```xml
<?xml version="1.0"?>
<svg xmlns="http://www.w3.org/2000/svg">
  <title>Simple animate example</title>
  <desc>Rectangle shape will change</desc>
  <rect x="50" y="50" width="10" height="100" style="fill:#CCCCFF;stroke:#000099">
    <animate attributeName="width"  from="10px"  to="100px" 
	     begin="0s" dur="10s" />
    <animate attributeName="height" from="100px" to="10px"
	     begin="0s" dur="10s" />
  </rect>
  <text x="50" y="170" style="stroke:#000099;fill:#000099;font-size:14;">
  Hello. Admire the dynamic rectangle</text>
</svg>
```

- [Open in browser](http://tecfa.unige.ch/guides/svg/ex/anim-trans/animate-size.svg)
