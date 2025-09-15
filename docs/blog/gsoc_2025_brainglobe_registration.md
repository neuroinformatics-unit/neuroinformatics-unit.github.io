:blogpost: true
:date: August 25, 2025
:author: Saarah Hussain
:location: London, UK
:category: Blog
:language: English
:image: 0

# GSoC 2025: brainglobe-registration

Over the summer, I worked on extending the brainglobe-registration plugin, 
focusing on making atlas alignment more accessible and less error-prone for 
users without a neuroscience background. Thus far, choosing the correct atlas 
slice and orientation has been a manual task – requiring users to scroll 
through volumes, make rough visual judgements, and enter rotation values by 
hand. My project aimed to automate this step, using Bayesian optimisation to 
identify the best matching slice and orientation parameters directly from the 
data.

The result is a new Automatic Slice Detection widget in the plugin, which not 
only handles single 2D images but can also align slabs of consecutive slices. 
For slabs, the optimiser matches the first and last slices and then 
interpolates alignment parameters across the stack, so that users can align 
larger volumes in one go. A key part of this work was building clear and 
informative logging – every optimisation step records the parameters tested, 
the corresponding rotated slice, and its similarity score. This makes the 
process more transparent and provides a useful record for reproducibility.

Working on this project has been a valuable experience in bridging methods 
from optimisation and image analysis with practical neuroscience workflows. 
I particularly enjoyed balancing algorithmic design with UX considerations, 
such as keeping the interface intuitive while still exposing enough 
flexibility for advanced use. Collaborating with the NIU team also gave me a 
deeper appreciation of the importance of open, well-documented tools in 
neuroinformatics, and the work that goes into making them robust and 
user-friendly.

Looking back, the most rewarding part was seeing the tool go from concept to 
a usable feature that I hope will save researchers time and difficulty in 
their workflows. Contributing to the BrainGlobe ecosystem has been a greatly 
rewarding opportunity, and I am incredibly excited to see how these tools 
continue to evolve in the future.
