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
.STYLE2 {
	font-size: 24px;
	font-family: "宋体";
}
</style>
</head>

<body>



  <table border="0" cellspacing="0" width="385">
    <tr>
      <td colspan="5">	<p align="center" class="STYLE2" >
	<xsl:value-of select="dish_menu/@hotel_name"/>结账单</p></td>
      </tr>
    <tr>
      <td>桌号：</td>
      <td><div align="left">A22</div></td>
      <td>&nbsp;</td>
      <td>餐别：</td>
      <td><div align="left"><xsl:value-of select="dish_menu/@meal_type"/></div></td>
    </tr>
    <tr>
      <td>结账时间：</td>
      <td colspan="4"><xsl:value-of select="dish_menu/@meal_time"/></td>
      </tr>
    <tr>
      <td colspan="5"><hr style="border-top-style:dotted" /></td>
      </tr>
    <tr>
      <td width="100"><div align="left">品名</div></td>
        <td><div align="center">规格</div></td>
        <td><div align="center">数量</div></td>
        <td><div align="center">单价</div></td>
        <td><div align="center">金额</div></td>
      </tr>
    <xsl:for-each select="dish_menu/dish">
      <tr>
        <td><div align="left"><xsl:value-of select="dish_name"/></div></td>
        <td><div align="center">份</div></td>
        <td><div align="center" ><xsl:value-of select="dish_num"/></div></td>
        <td><div align="right"><xsl:value-of select="dish_price"/></div></td>
        <td><div align="right"><xsl:value-of select="dish_account"/></div></td>
      </tr>
	  </xsl:for-each>
      <tr>
        <td colspan="5"><hr style="border-top-style:dotted" /></td>
        </tr>
      <tr>
        <td>原价合计：</td>
        <td colspan="2"><xsl:value-of select="dish_menu/@meal_account"/></td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <td colspan="5"><hr style="border-top-style:dotted" /></td>
      </tr>
      <tr>
        <td>刷卡支付：</td>
        <td colspan="2"><xsl:value-of select="dish_menu/@meal_account"/></td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <td><strong>实收支付：</strong></td>
        <td colspan="2"><strong><xsl:value-of select="dish_menu/@meal_account"/></strong></td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
  </table>

</body>
</html>

</xsl:template>
</xsl:stylesheet>