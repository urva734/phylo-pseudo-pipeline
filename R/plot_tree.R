# plot_tree.R - Phylogenetic tree for 6 accessions
library(ape)
library(ggtree)
library(ggplot2)

# --- FIXED PATHS TO YOUR ACTUAL FOLDERS ---
TREE_FILE <- "results/tree/tree.nwk"
FIGURE_PDF <- "results/figures/pqqD_ML_tree.pdf"
FIGURE_PNG <- "results/figures/pqqD_ML_tree.png"

# Check
if (!file.exists(TREE_FILE)) {
  stop(paste("Tree file not found:", TREE_FILE, "\nFirst export ML tree from MEGA as .nwk to results/tree/"))
}

tree <- read.tree(TREE_FILE)
print(paste("Loaded", length(tree$tip.label), "tips:", paste(tree$tip.label, collapse=", ")))

# Plot - your 6 accessions
p <- ggtree(tree, layout="rectangular") +
  geom_tiplab(size=3.5, fontface="italic") +
  geom_nodepoint(size=2, color="firebrick") +
  theme_tree2() +
  labs(
    title="Phylogenetic Analysis of pqqD Gene in Pseudomonas spp.",
    subtitle="Maximum Likelihood (1000 bootstrap)",
    caption="KM251420.1, CP003080.1, CP023065.1, CP077007.1, CP125543.1, CP003685.1"
  ) +
  theme(plot.title = element_text(face="bold", size=12))

dir.create("results/figures", showWarnings=FALSE, recursive=TRUE)

ggsave(FIGURE_PDF, plot=p, width=10, height=7, dpi=300)
ggsave(FIGURE_PNG, plot=p, width=10, height=7, dpi=300)

message(paste("Saved:", FIGURE_PDF))
message(paste("Saved:", FIGURE_PNG))
