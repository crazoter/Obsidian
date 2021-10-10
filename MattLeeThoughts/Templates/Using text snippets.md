### motivation
https://forum.obsidian.md/t/template-plugin-improvement-tab-stops-1/4917/6

### extension
https://github.com/ArianaKhit/text-snippets-obsidian

go to the settings and add whatever you need. For me, I use the extension to add snippets.

snip : ```Python$nl$# This is an automatically generated template for Sublime Text snippets. For more information, see https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html$nl$# Fields: ${1:this} is a ${2:snippet}$nl$# Context: $SELECTION$nl$# File is saved using tabTrigger name.$nl$$nl$#region SNIPPET$nl$<snippet><content><![CDATA[$nl$$tb$$nl$]]></content>$nl$<tabTrigger>$tb$</tabTrigger>$nl$<scope>source.python</scope>$nl$</snippet>$nl$#endregion$nl$```

So whenever I want to add a snippet I type snip and press ctrl-tab.

I have a more concise version to remove the initial blurb (after you get used to the syntax):

sn : ```Python$nl$#region SNIPPET$nl$<snippet><content><![CDATA[$nl$$tb$$nl$]]></content><tabTrigger>$tb$</tabTrigger>$nl$<scope>source.python</scope></snippet>$nl$#endregion$nl$```

I have also improved the format to make it more readable:

sn1 : ```python$nl$# Region marker		 | Syntax		 | Name of snippet$nl$#region SHORTSNIPPET | source.python | $tb$$nl$$tb$$nl$```

For quickly making a field:
f : ${$tb$:1}