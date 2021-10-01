```
<!-- File to save snippet to. -->
$tb$.sublime-snippet

<!-- Hello, ${1:this} is a ${2:snippet}. -->
<!-- Snippets can also use context e.g. $SELECTION. See https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html#environment-variables -->
<snippet>
	<content><![CDATA[
$tb$
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>$tb$</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<scope>source.python</scope>
</snippet>
```