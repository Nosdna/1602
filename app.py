#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == 'POST':
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA,TLTA,WCTA)
        model = load_model('bankrupty_model')
        pred = model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        return(render_template("index.html", result = '1'))
    else:
        return(render_template("index.html", result = '2'))


# In[4]:


app.run()


# In[ ]:




