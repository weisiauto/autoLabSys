"""
用于演示python内容存储的示例
1.存储为json
2.存储为ymal
"""

import datetime

class Post:
    """
    博客内容类，注意tag和rst_text部分，as_dict用于将博客内容生成字典
    """
    def __init__( self, date, title, rst_text, tags):
        self.date=date
        self.title=title
        self.rst_text=rst_text
        self.tags=tags
    def as_dict( self ):
        return dict(
            date=str(self.date),
            title=self.title,
            underline="-"*len(self.title),
            rst_text=self.rst_text,
            tag_text=" ".join(self.tags),
            )


from collections import defaultdict
class Blog:
    """
    博客类，是博客内容类的集合
    """
    def __init__( self, title, posts=None ):
        self.title=title
        self.entries=posts if posts is not None else []
    def append( self,post):
        self.entries.append(post)

    def by_tag(self):
        tag_index=defaultdict(list)
        for post in self.entries:
            for tag in post.tags:
                tag_index[tag].append( post.as_dict() )
        return tag_index
    def as_dict( self):
        return dict(
            title=self.title,
            underline="-"*len(self.title),
            entries=[p.as_dict() for p in self.entries],
            )


def examContent():
    """
    用于示例的博文数据
    """
    travel=Blog("Travel")
    travel.append(
        Post( date=datetime.datetime(2018,4,10,10,12,24),
              title="Hard Aground",
              rst_text="""some embarrassing revelation.
                Omc;idomg @""",
              tags=("#RedRanger","#Whiteby42","#ICW"),
              )
        )
    travel.append(
        Post( date=datetime.datetime(2018,4,11,12,13,24),
              title="Anchor Follies",
              rst_text="""some witty epigram. Including <&>
                characters.""",
              tags=("#RedRanger","#Whiteby42","#mistakes"),
              )
        )
    return travel

"""
导入jinja2模板
"""
from jinja2 import Template
blog_template=Template("""
    {{title}}
    {{underline}}

    {% for e in entries %}
    {{e.title}}
    {{e.underline}}
    
    {{e.rst_text}}
    :date: {{e.date}}
    :tags: {{e.tag_text}}
    {% endfor %}
    Tag Index
    =========
    {% for t in tags %}
    * {{t}}
      {% for post in tags[t]%}
      - '{{post.title}}'_
      {% endfor %}
    {% endfor %}
    """)

import json
if __name__=="__main__":
    travel=examContent()
    print( blog_template.render(tags=travel.by_tag(),**travel.as_dict()))
    print("-"*20)
    print("JSON")
    print("-"*20)
    print(json.dumps(travel.as_dict(),indent=4))
    
