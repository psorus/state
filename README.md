# state
A class to extend my python( in a nonpythonic way)

The only really important file is state.py, which implements a state metaclass. Its documentation can be accessed by help(state) (after importing state.state obviously)
Having a state class creates a state for your object. This migth not seem like much, but you can implement magic functions to be automatically called when your state chances or to forbid state chances of a certain type. This can allow you to quickly define behaviours for your objects, especcially since it also allows you to do the same for each variable used in your object.

The easiest example you find in test_shop.py. This implements an object, which you can buy (aslong as the state is not soldout) or restock (unless the state is full). This shows how states can be used to create save interfaces.

The second example (test_tic.py) plays tic tac toe. Its state object is a tictactoe board, which allows you to overwrite the functions letting somebody play (tic1). This shows how states can be combined with class inheritance to get something that is something between a function and a class (a function, which behaviour is build into multiple segments that you can overwrite or a class, which can calculates stuff)

My third usecase does not work yet (app.py and everything else). There I tried to implement a flask app to work with states online, but my state saving modules dont really work


Finally, I know that states are not really pythonic (as you can find another way to do each of my examples), but working with state objects requires you to tilt the way you think a bit, and I am always faszinated by this. I remember my first object truly using polymorphy, how it chanced the way I think and how I am always searching for something similar since then. Maybe state based programming can do this for you? Also if you have any Ideas on how to chance state.py, please write me, I really would love to hear from you (Simon.Kluettermann@gmx.de)



