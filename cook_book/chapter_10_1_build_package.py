#import chapter_10_1_graphics.primitive.line
from chapter_10_1_graphics.primitive import line
#from chapter_10_1_graphics.formats import jpg
#from chapter_10_1_graphics.formats import *
import chapter_10_1_graphics.formats

####由于formats里的__init__文件导入了两个png,jpg所以可以直接使用
####如果formats里的__init__文件没有导入则不可以使用
####至于调用时，需要写完整的路径
line.print_line()
chapter_10_1_graphics.formats.jpg.print_jpg()
