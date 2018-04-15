<?xml version="1.0" encoding="gb2312"?><!-- DWXMLSource="file:///C|/Users/Administrator/Desktop/dish_menu.xml" -->
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
<xsl:output method="html" encoding="gb2312" doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"/>
<xsl:template match="/">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
<title>Untitled Document</title>
</head>

<body>
<p>�͹�����</p>
<table border="0" cellspacing="0">
  <tr>
    <td><div align="center">Ʒ��</div></td>
    <td><div align="center">���</div></td>
    <td><div align="center">����</div></td>
    <td><div align="center">����</div></td>
    <td><div align="center">���</div></td>
  </tr>
  <xsl:for-each select="dish_menu/dish">
  <tr>
    <td><div align="left"><xsl:value-of select="dish_name"/></div></td>
    <td><div align="center">��</div></td>
    <td><div align="center"><xsl:value-of select="dish_num"/></div></td>
    <td><div align="right"><xsl:value-of select="dish_price"/></div></td>
    <td><div align="right"><xsl:value-of select="dish_account"/></div></td>
  </tr>
  </xsl:for-each>
</table>
</body>
</html>

</xsl:template>
</xsl:stylesheet>