.. _books:

Books about Parallel Computing
==============================

This is a very incomplete list, permanently under construction, of
books about parallel computing.

General
-------

* G. Hager and G. Wellein.
  `Introduction to high performance computing for scientists and engineers <https://www.crcpress.com/Introduction-to-High-Performance-Computing-for-Scientists-and-Engineers/Hager-Wellein/p/book/9781439811924>`_.
  Chapman & Hall, 2010.

  This book first introduces the architecture of modern cache-based
  microprocessors and discusses their inherent performance limitations, before
  describing general optimization strategies for serial code on cache-based
  architectures. It next covers shared- and distributed-memory parallel
  computer architectures and the most relevant network topologies. After
  discussing parallel computing on a theoretical level, the authors show how to
  avoid or ameliorate typical performance problems connected with OpenMP. They
  then present cache-coherent nonuniform memory access (ccNUMA) optimization
  techniques, examine distributed-memory parallel programming with message
  passing interface (MPI), and explain how to write efficient MPI code. The
  final chapter focuses on hybrid programming with MPI and OpenMP.

* V. Eijkhout.
  `Introduction to high performance scientific computing <https://insidehpc.com/2010/12/download-introduction-to-high-performance-scientific-computing/>`_.
  2011.

  This is a textbook that teaches the bridging topics between numerical
  analysis, parallel computing, code performance, large scale applications. It
  can be freely accessed on `archive.org
  <https://archive.org/details/EijkhoutIntroToHPC>`_ (though you have to
  respect the copyright of course).

* A. Grama, A. Gupta, G. Kapyris, and V. Kumar.
  `Introduction to parallel computing (2nd edition) <http://www.pearsoned.co.uk/Bookshop/detail.asp?item=100000000005961>`_.
  Pearson Addison Wesley, 2003. ISBN 978-0-201-64865-2.

  A somewhat older book, but still used a lot as textbook in academic courses
  on parallel computing.

* C. Lin and L. Snyder.
  `Principles of parallel programming <http://www.pearsoned.co.uk/bookshop/detail.asp?WT.oss=Principles%20of%20parallel%20programming&WT.oss_r=1&item=100000000247080>`_.
  Pearson Addison Wesley, 2008. ISBN 978-0-32148790-2.

  This books discusses parallel programming both from a more abstract level and
  a more practical level, touching briefly threads programming, OpenMP, MPI and
  PGAS-languages (using ZPL).

* M. McCool, A.D. Robinson, and J. Reinders.
  `Structured parallel programming: patterns for efficient computation <https://www.elsevier.com/books/structured-parallel-programming/mccool/978-0-12-415993-8>`_.
  Morgan Kaufmann, 2012. ISBN 978-0-12-415993-8.

Grid computing
--------------

* F. Magoules, J. Pan, K.-A. Tan, and A. Kumar.
  `Introduction to grid computing <https://www.routledge.com/Introduction-to-Grid-Computing-1st-Edition/Magoules-Pan-Tan-Kumar/p/book/9780367385828>`_.
  CRC Press, 2019. ISBN 9780367385828.

MPI
---

* A two-volume set in tutorial style:

  * W. Gropp, E. Lusk, and A. Skjellum.
    `Using MPI: portable parallel programming with the Message-Passing Interface, third edition <https://mitpress.mit.edu/?q=using-MPI-3ed>`__.
    MIT Press, 2014. ISBN 978-0-262-57139-2 (paperback) or 978-0-262-32659-9 (ebook).

    This edition of the book is based on the MPI-3.0 specification.

  * W. Gropp, T. Hoeffler, R. Thakur and E. Lusk.
    `Using advanced MPI: modern features of the Message-Passing Interface <https://mitpress.mit.edu/?q=using-advanced-MPI>`_.
    MIT Press, 2014. ISBN 978-0-262-52763-7 (paperback) or 978-0-262-32662-9 (ebook).

  These books replace the earlier editions of "Using MPI: Portable
  Parallel Programming with the Message-Passing Interface" and the
  book "Using MPI-2: Advanced Features of the Message-Passing
  Interface".

* A two-volume set in reference style, but somewhat outdated:

  * M. Snir, S.W. Otto, S. Huss-Lederman, D.W. Walker, and J. Dongarra.
    `MPI: the complete reference. Volume 1: the MPI core (2nd Edition) <https://mitpress.mit.edu/books/mpi-complete-reference-second-edition-volume-1>`_.
    MIT Press, 1998. ISBN 978-0-262-69215-1.

  * W. Gropp, S. Huss-Lederman, A. Lumsdaine, E. Lusk, B. Nitzberg, W. Saphir, and M. Snir.
    `MPI: the complete reference, Volume 2: the MPI-2 extensions <https://mitpress.mit.edu/books/mpi-complete-reference-volume-2>`_.
    MIT Press, 1998. ISBN 978-0-262-57123-4.

  These two volumes are also available as one set with
  `ISBN number 978-0-262-69216-8 <https://mitpress.mit.edu/?q=books/mpi-complete-reference>`_.

OpenMP
------

* B. Chapman, G. Jost, and R. van der Pas.
  `Using OpenMP - portable shared memory parallel Programming <https://mitpress.mit.edu/?q=books/using-openmp>`_.
  The MIT Press, 2008. ISBN 978-0-262-53302-7.

* R. Chandra, L. Dagum, D. Kohr, D. Maydan, J. McDonald, and R. Menon.
  `Parallel programming in OpenMP <https://www.elsevier.com/books/parallel-programming-in-openmp/chandra/978-1-55860-671-5>`_.
  Academic Press, 2000. ISBN 978-1-55860-671-5.

GPU computing
-------------

* M. Scarpino.
  `OpenCL in action <https://www.manning.com/books/opencl-in-action>`_.
  Manning Publications Co., 2012. ISBN 978-1-617290-17-6

* D.R. Kaeli, P. Mistry, D. Schaa, and D.P. Zhang.
  `Heterogeneous computing with OpenCL 2.0, 1st Edition <https://www.elsevier.com/books/heterogeneous-computing-with-opencl-20/kaeli/978-0-12-801414-1>`_.
  Morgan Kaufmann, 2015. ISBN 978-0-12-801414-1 (print) or 978-0-12-801649-7 (eBook).

  A thorough rewrite of the earlier well-selling book for OpenCL 1.2 that saw
  2 editions.

Case studies and examples of programming paradigms
--------------------------------------------------

* J. Reinders and J. Jeffers (editors).
  `High performance parallelism pearls. Volume 1: multicore and many-core programming approaches <https://www.elsevier.com/books/high-performance-parallelism-pearls-volume-one/reinders/978-0-12-802118-7>`_.
  Morgan Kaufmann, 2014. ISBN 978-0-12-802118-7

* J. Reinders and J. Jeffers (editors).
  `High performance parallelism pearls. Volume 2: multicore and many-core programming approaches <https://www.elsevier.com/books/high-performance-parallelism-pearls-volume-two/jeffers/978-0-12-803819-2>`_.
  Morgan Kaufmann, 2015. ISBN 978-0-12-803819-2

*Please mail further suggestions to geertjan.bex@uhasselt.be*
