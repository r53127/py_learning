from lxml import etree
xml_filename='dish_menu.xml'
xsl_filename="dish_print.xsl"
html_filename='dish.html'

xmldom=etree.parse(xml_filename)
xsldom=etree.parse(xsl_filename)

transform=etree.XSLT(xsldom)
htmldoc=transform(xmldom)

fo = open(html_filename, "w")
fo.write(str(htmldoc))
