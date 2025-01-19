# TraceReconstructionReview
Welcome to Trace Reconstruction Review (TRR), a central repository for all things trace reconstruction.

We've got string trace reconstruction, we've got tree trace reconstruction, we've got graph trace reconstruction. 

The goal of TRR is to track all the current work on trace reconstruction problems, with a short overview, and 
results stated in a comparable manner. Tables with state of the art results are currently a work in progress. 

This repository has works broken down into catagories, based on the type of objects that are being reconstructed. For now, the catagories are "String" (binary or larger alphabet sequences), "Trees" (graphs with a natural hierarchical structure), and "Graphs" (General graphs beyond trees). 

Here is a list of a few useful resources that are not necessarily papers: 
- [Blog post by Mingda Qiao](https://theorydish.blog/2021/06/29/trace-reconstruction/comment-page-1/?unapproved=226352&moderation-hash=6b4525b9205ab4125f2e3687c124cca9#respond): This blog post is an excellent quick tutorial on string trace reconstruction. It also makes the connection between trace reconstruction and complex polynomials quite clear. (This connection was used for several state of the art string trace reconstruction results)
- 



This repository serves as a curation of published works. We do not claim ownership of any of the materials presented in the stored works.

If you think we missed something, feel free to make a pull request or to contact me directly. All complaints should be directed to my advisor (gandikota.venkata@gmail.com). 


# What is Trace Reconstruction?

Trace reconstruction is in general the problem of reconstructing an object given multiple noisy (often with deletion noise) observations of the structure. For example, the string trace reconstruction problem is the problem of reconstructing an arbitrary binary string given $T$ outputs of a probability $q$ deletion channel. 

Many variations of this problem exist, including string coded trace reconstruction, approximate string trace reconstruction, tree trace reconstruction, matrix trace reconstruction, and many more.
