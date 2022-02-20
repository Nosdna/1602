{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request, render_template\n",
    "\n",
    "@app.route(\"/\",methods = [\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == 'POST':\n",
    "        NPTA = request.form.get(\"NPTA\")\n",
    "        TLTA = request.form.get(\"TLTA\")\n",
    "        WCTA = request.form.get(\"WCTA\")\n",
    "        print(NPTA,TLTA,WCTA)\n",
    "        model = load_model('bankrupty_model')\n",
    "        pred = model.predict([[float(NPTA),float(TLTA),float(WCTA)]])\n",
    "        return(render_template(\"index.html\", result = '1'))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result = '2'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
