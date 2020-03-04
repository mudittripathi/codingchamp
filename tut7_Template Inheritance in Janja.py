# humlogo ne index.html fix kia ..phr about oe gaye to wapas se issue...phr se fix na krna pade
# isly ek technique hai
# jo header hai, footer hai, ya jo change ni ho rha hai, use ek file me lelo , ise inherit template kehte hai
# header se nevigation tk ka cut kro or layout.html me dalo
# beech me body rahegi but ye job change hoti hai
# neeche footer dalo copy paste
#
# ab layout me header hai footer hai or body me ye laga dia hai
# {% block body %} {% endblock %}
#
# or index.html me upar dal dia hai ye
# {% extends "layout.html" %}
# mtlb ye html layout.html ko extend kregi
#
# or index.html me body hai wo sb page ke lie change hti hai
# uske phle ye {% block body %} or last me ye {% endblock %} daalo
# isse adbvantage ye milega ki about, contact, post jaise inner pages ko change krne ki need ni padeg. wo layout wale page me body
# change kr kr ke display krega