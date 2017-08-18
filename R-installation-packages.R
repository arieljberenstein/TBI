install.packages(devtools)
library(devtools)

## install some dependencies
source("https://bioconductor.org/biocLite.R")
biocLite(c('AnnotationDbi''biomaRt','cowplot','GOSemSim','omicade4','ontoCAT','org.Hs.eg.db','ReactomePA','RTCGAToolbox','topGO','ellipse','mixOmics'))

install_github("ggbiplot", "vqv")
install_github('TCGAome', 'priesgo')
