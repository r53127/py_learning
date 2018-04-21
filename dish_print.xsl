<?xml version="1.0" encoding="utf-8"?><!-- DWXMLSource="file:///C|/Users/Administrator/Desktop/dish_menu.xml" -->
<!DOCTYPE xsl:stylesheet  [
	<!ENTITY nbsp   "&#160;">
	<!ENTITY copy   "&#169;">
	<!ENTITY reg    "&#174;">
	<!ENTITY trade  "&#8482;">
	<!ENTITY mdash  "&#8212;">
	<!ENTITY ldquo  "&#8220;">
	<!ENTITY rdquo  "&#8221;"> 
	<!ENTITY pound  "&#163;">
	<!ENTITY yen    "&#165;">
	<!ENTITY euro   "&#8364;">
]>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8" doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"/>
<xsl:template match="/">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>Untitled Document</title>
<style type="text/css">
<!--
.STYLE1 {
	font-family: "新宋体";
	font-size: 24px;
	font-weight: bold;
}
-->
</style>
</head>

<body>
<div>
<p align="center" class="STYLE1"><xsl:value-of select="dish_menu/@hotel_name"/></p>
<p align="center" class="STYLE1">结账单</p>
<table border="0" cellspacing="0">
  <tr>
    <td><div align="left">品名</div></td>
    <td><div align="center">规格</div></td>
    <td><div align="center">数量</div></td>
    <td><div align="center">单价</div></td>
    <td><div align="center">金额</div></td>
  </tr>
  <xsl:for-each select="dish_menu/dish">
  <tr>
    <td><div align="left"><xsl:value-of select="dish_name"/></div></td>
    <td><div align="center">份</div></td>
    <td><div align="center"><xsl:value-of select="dish_num"/></div></td>
    <td><div align="right"><xsl:value-of select="dish_price"/></div></td>
    <td><div align="right"><xsl:value-of select="dish_account"/></div></td>
  </tr>
  </xsl:for-each>
</table>
</div>
</body>
</html>

</xsl:template>
</xsl:stylesheet>