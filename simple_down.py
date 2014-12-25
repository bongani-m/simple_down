'''
### syntax ###

#bold
b(this is bold)
# italics
i(this is italics)
# h#'s
h1..6(This is the header)
# breaks
&br //break
# line breaks
&hr // line break
# links
link(Google Homepage [http://google.com])
# imgs
img{http://google.com/cat.jpg}

'''
# regex package
import re

#bold
def bold(text):
	return re.sub(r'b\((.*)\)', '<b>' + r'\1' + '</b>', text, flags=re.MULTILINE)
# italics
def italic(text):
	return re.sub(r'i\((.*)\)', '<i>' + r'\1' + '</i>', text, flags=re.MULTILINE)
# h#'s
def headers(text):
	return re.sub(r'h(\d)\((.*)\)', '<h' + r'\1' + '>' + r'\2' + '</h' + r'\1' + '>\n', text, flags=re.MULTILINE)
# breaks 
def breaks(text):
	return re.sub(r'&br', '<br>', text, flags=re.MULTILINE)
# line breaks
def line_breaks(text):
	return re.sub(r'&hr', '<hr>', text, flags=re.MULTILINE)
# links
def links(text):
	return re.sub(r'links\((.*)\[(.*)\]\)', '<a href =\"' + r'\2' + '\">' + r'\1' + '</a>', text, flags=re.MULTILINE)
# img
def links(text):
	return re.sub(r'img\{(.*)\}', '<img src=\"' + r'\1' + '\">', text, flags=re.MULTILINE)
# paragraphs
def para(text):
	pre = re.split(r'\n', text)
	return reduce(lambda a,x: a+('<p>' + x + '</p>\n'), pre)
# full parser
def parser(text):
	text = bold(text)
	text = italic(text)
	text = headers(text)
	text = breaks(text)
	text = line_breaks(text)
	text = links(text)
	text = links(text)
	text = para(text)
	return text.replace('<p></p>', '')