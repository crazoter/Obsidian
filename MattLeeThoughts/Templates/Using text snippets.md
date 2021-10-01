### motivation
https://forum.obsidian.md/t/template-plugin-improvement-tab-stops-1/4917/6

### extension
https://github.com/ArianaKhit/text-snippets-obsidian

go to the settings and add whatever you need as per the syntax e.g. for me I use snippets.

snip : ```$nl$<!-- File to save snippet to. -->$nl$$tb$.sublime-snippet$nl$<!-- Hello, ${1:this} is a ${2:snippet}. -->$nl$<!-- Snippets can also use context e.g. $SELECTION. See https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html#environment-variables -->$nl$<snippet>$nl$	<content><![CDATA[$nl$$tb$$nl$]]></content>$nl$	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->$nl$	<tabTrigger>$tb$</tabTrigger>$nl$	<!-- Optional: Set a scope to limit where the snippet will trigger -->$nl$	<scope>source.python</scope>$nl$</snippet>$nl$```
