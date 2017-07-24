Copperfield FX
===========

Node based animation and compositing tool. Mimics world's famous Houdini FX.

At this stage it's even not a proof-of-concept thing. It's something else. But you can play with it at any time. Have fun!

The idea behind this project is to build open source node based all-in-one animaition and compositing software.

Why not Blender ? 

It's not a ture node based procedural design. End of story.

Why Python ?

Well. First of all i'm not a programmer, i just like some coding i my spare time. It takes much less time for me to prototype software in Python than in C++. If at any stage i would decide to speed up some
parts of it or the entire engine, i can port it to C++ and expose Python bindings so maintain UI in Python and by doing
this keep relatively high speed of development. But somehere deep inside me i want to stay in Python entirely. Don't want
to mess up with C++ on my own. But if there would be a team...

Haz renderz ?

Nope. Not even a documentation at his point, nor stable classes and interfaces. By the way. The second "sub goal" is to have build in OpenGL PBR render like in modern game engines. I tired of so caller "1-hour-per-frame production renderers". You name it. I want to have awesome looking graphics in a fraction of seconds. Not necessary real time, but close. And if you've
been played modern PC-XBOX-PS4 titles then you get the idea. I even have an title for that renderer of dream - "Cut Scene" :)
Yes, it's very inportand to have the title, icons and all that sh..t. Seriously!

Update.

Things getting more interesting as i've implemented some more features. And now it's a shame to waste so much power inside a Python interpreter, so... I decided to port everything to C++. Yep. So i think next two months i would be very busy. I mean very busy. Btw. All the interface things like panels and workspace itself is going to be pluggable. That means you can make any interface on your own. Why ? Simple. One would like to work in a 3DSMAX-a-like environment. And it's quite possible as you can 'reflect' underlying node structure to modifires stack approach. This is going to be done through the special structures.

Stay tuned!
