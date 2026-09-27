from pythonds3.basic import Stack

test_balanced = """<html>
   <head>
      <title>
         Example
      </title>
   </head>
 
   <body>
      <h1>Hello, world</h1>
   </body>
</html>
"""

test_mismatch ="""<html>
   <body>
      <h1>Hello, world</h2>
   </body>
</html>
"""

test_missingClose =  """<html>
   <head>
      <title>Example</title>
   </head>
   <body>
      <h1>Hello, world</h1>
</html>
"""

test_extraClose = """<html>
   <body>
   </body>
</html>
</div>
"""

def checkTags(htmlStr):
   s = Stack()
   tagList = htmlStr.split()
   for tag in tagList:
      if tag in ["<head>", "<title>", "<html>", "<body>", "<h1>", "<div>", "<p>"]:
         tag.strip('<>/')
         s.push(tag)
      elif tag in ["</head>", "</title>", "</html>", "</body>", "</h1>", "</div>", "</p>"]:
         tag = tag.strip('<>/')
         if s.is_empty():
            return False
         if s.peek() == tag:
            s.pop()
      else:
         return False
         
   return s.is_empty()
         

print(checkTags(test_balanced))
print(checkTags(test_mismatch))
print(checkTags(test_missingClose))
print(checkTags(test_extraClose))         