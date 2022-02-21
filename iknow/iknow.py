import iknowpy
import mg_python
import sys

mg_python.m_set_host(0, "yottadb", 7041, "", "")
engine = iknowpy.iKnowEngine()


key = mg_python.m_order(0, "^IKNOW", "text", "")
while (key != ""):
      text=key
      engine.index(text, 'en')
      for s in engine.m_index['sentences']:
         for e in s['entities']:
            mg_python.m_set(0, "^IKNOW", "text", key, e['type'], e['index'], "")
            print('<'+e['type']+'>'+e['index']+'</'+e['type']+'>', end=' ')
         print('\n')
      key  = mg_python.m_order(0, "^IKNOW", "text", key)

