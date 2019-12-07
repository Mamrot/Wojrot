from xml.dom import minidom

doc = minidom.parse("reminder.xml")
to = doc.getElementsByTagName("to")[0]
heading = doc.getElementsByTagName("heading")[0]
print(to.firstChild.data)

to.firstChild.data = "Toni"
heading.firstChild.data = "anything"
file = open("newReminder.xml","w")
xml = doc.toxml()
file.write(xml)

