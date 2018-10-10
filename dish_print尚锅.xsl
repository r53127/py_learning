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
	font-size: 30px;
	font-family: "黑体";
}
.STYLE4 {
	font-family: "楷体";
	font-size: 24px;
}
.STYLE8 {font-family: "楷体"}
</style>
</head>

<body>
  <table border="0" cellspacing="0" width="385">
    <tr>
      <td colspan="5" align="center" class="STYLE2"><span class="STYLE8">结账单</span></td>
      </tr>
    <tr>
      <td colspan="5">酒店名称：<xsl:value-of select="dish_menu/@hotel_name"/></td>
      </tr>
    <tr>
      <td>桌号：</td>
      <td id="table_no">
		<script type="text/javascript">
		var i=20-Math.ceil(Math.random()*10); 
		var element=document.getElementById("table_no");
		element.innerHTML="VIP"+i;	
		</script>	  </td>
      <td>&nbsp;</td>
      <td>餐别：</td>
      <td><div align="left"><xsl:value-of select="dish_menu/@meal_type"/></div></td>
    </tr>
    <tr>
      <td>账单编号：</td>
      <td colspan="4" id="dish_no">
	  <script>
		var j=100000-Math.ceil(Math.random()*10000)
		var k=Math.random().toString(12).substr(2)
		var element=document.getElementById("dish_no");
		element.innerHTML=j+k;		
	  </script>	  </td>
    </tr>
    <tr>
      <td>结账时间：</td>
      <td colspan="4"><xsl:value-of select="dish_menu/@meal_time"/></td>
      </tr>
    <tr>
      <td colspan="5"><hr style="border-top-style:dotted" /></td>
      </tr>
    <tr>
      <td width="120"><div align="left">品名</div></td>
        <td><div align="center">规格</div></td>
        <td><div align="center">数量</div></td>
        <td><div align="right">单价</div></td>
        <td><div align="right">金额</div></td>
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
      <tr>
        <td colspan="5"><hr style="border-top-style:dotted" /></td>
      </tr>
      <tr>
        <td colspan="5" align="center" class="STYLE4">谢谢光临，欢迎惠顾！</td>
      </tr>
  </table>

</body>
</html>

</xsl:template>
</xsl:stylesheet>