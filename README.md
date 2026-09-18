# NFDI Matwerk Summer School 2026
[![Pipeline](https://github.com/pyiron-workshop/NFDI-summerschool-2026/actions/workflows/pipeline.yml/badge.svg)](https://github.com/pyiron-workshop/NFDI-summerschool-2026/actions/workflows/pipeline.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyiron-workshop/NFDI-summerschool-2026/HEAD)

Turn a scientific analysis into an explicit, reproducible and scalable workflow — from a plain Python script to a FAIR, HPC-ready workflow graph, using [pyiron](https://pyiron.org) as the example implementation.

📖 Read the tutorial online at **[workshop.pyiron.org/NFDI-summerschool-2026](http://workshop.pyiron.org/NFDI-summerschool-2026)**, or launch it interactively with the Binder badge above. This material was developed for the [NFDI-MatWerk Summer School 2026 in Bochum – Research Data Management in Materials Science and Engineering](https://www.eusmat.net/research/other-events/nfdi-matwerk-summer-school-2026/).

## Key Features
* **Turn a Python script into an explicit, reusable workflow.** Starting from plain functions, the tutorial builds the same analysis as a [`pyiron_workflow`](https://pyiron-workflow.readthedocs.io/en/latest/) node graph, with inputs, outputs and dependencies you can inspect, cache and rerun — instead of an implicit sequence of notebook cells.
* **Build and run the same workflow with code or with a mouse.** [`pyironflow`](https://github.com/pyiron/pyironFlow) puts that same workflow graph behind a drag-and-drop canvas, so it can be composed, inspected and executed with or without writing Python.
* **Scale from a laptop to an HPC cluster without rewriting anything.** [`executorlib`](https://executorlib.readthedocs.io/en/latest/) runs the same functions through a `concurrent.futures`-compatible executor, locally for development and on SLURM or flux for production — the workflow code itself does not change.
* **Save a workflow, not just its result.** Every workflow graph is exported to the engine-agnostic [Python Workflow Definition](https://pythonworkflow.github.io/python-workflow-definition/) — the basis for interoperable, FAIR and reproducible research workflows.
* **See it applied to a real research pipeline.** The same node/graph pattern is used to generate machine-learning-potential training data with the [ASSYST](https://www.nature.com/articles/s41524-025-01669-4) method, and to fit and validate an [Atomic Cluster Expansion](https://doi.org/10.1103/PhysRevB.99.014104) interatomic potential on the result.

## Why this tutorial?
A typical materials-science analysis has several steps: data are recorded or generated, processed, analysed and finally visualized — often by hand, spread across notebooks, scripts and software packages. Reproducing the result then requires not just the final data, but also knowledge of the exact sequence of operations that produced it.

This tutorial uses one running example throughout — determining the **Young's modulus** of a steel specimen from a tensile test, using a real dataset recorded at the [Bundesanstalt für Materialforschung und -prüfung (BAM)](https://bam.de) — and builds the *same* four-step analysis (read data → convert to stress/strain → fit → plot) four times, with a different tool each time, so that one concept can be isolated at a time: functions, an explicit workflow graph, a visual editor, and an HPC-ready executor. The last two notebooks apply that same thinking to a genuine research pipeline: generating training data and fitting a machine-learning interatomic potential.

## Example
The core idea used throughout the tutorial: an existing Python function is wrapped, unchanged, into a workflow node, and nodes are connected into a graph with explicit inputs and outputs.
```python
from pyiron_workflow import Workflow, to_function_node


def add(x, y):
    return x + y


add_node = to_function_node("add", add, "add")

wf = Workflow("demo")
wf.result = add_node(x=1, y=2)
wf.run()
```
The same graph can be built by dragging and connecting boxes in [`pyironflow`](http://workshop.pyiron.org/NFDI-summerschool-2026/3-pyironflow.html)'s visual canvas, executed locally or on an HPC cluster with [`executorlib`](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html), and saved as a [Python Workflow Definition](http://workshop.pyiron.org/NFDI-summerschool-2026/2-pyiron_workflow.html#python-workflow-definition) that any compatible engine can read back.

## Which notebook should I look at?
The notebooks share one [`workflow.py`](workflow.py) module and one dataset, and are best read in order — but each one also stands on its own if you already know what you are looking for:

| Notebook | Covers | Best for |
|---|---|---|
| [`0-python.ipynb`](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html) | Script → functions → module | starting point; only needs `numpy`, `pandas` and `matplotlib` |
| [`1-executorlib.ipynb`](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html) | Functions as `concurrent.futures`; implicit dependency graph; scaling to SLURM/flux | scaling the same functions from a laptop to an HPC cluster |
| [`2-pyiron_workflow.ipynb`](http://workshop.pyiron.org/NFDI-summerschool-2026/2-pyiron_workflow.html) | Functions as nodes; explicit, inspectable dependency graph; PWD export & FAIR | users comfortable in Python who want an explicit, cacheable workflow |
| [`3-pyironflow.ipynb`](http://workshop.pyiron.org/NFDI-summerschool-2026/3-pyironflow.html) | The same graph via a drag-and-drop canvas | users who would rather compose and run a workflow visually |
| [`4-assyst.ipynb`](http://workshop.pyiron.org/NFDI-summerschool-2026/4-assyst.html) | Applying nodes and graphs to generate structures for MLIP training data | domain scientists interested in atomistic simulation |
| [`5-fitting.ipynb`](http://workshop.pyiron.org/NFDI-summerschool-2026/5-fitting.html) | Fitting and validating an ACE potential from that data | closing the loop from data generation to a validated model |
| [`SUMMARY.md`](http://workshop.pyiron.org/NFDI-summerschool-2026/SUMMARY.html) | Recap of the concepts and takeaways across all notebooks | wrap-up, and applying the same thinking to your own research |

## Documentation
* [Introduction](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html)
  * [The materials science challenge](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html#the-materials-science-challenge)
  * [From analysis to workflow](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html#from-analysis-to-workflow)
  * [Learning objectives](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html#learning-objectives)
  * [Python Functions](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html#python-functions)
    * [Script](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html#script)
    * [Functions](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html#functions)
    * [Module](http://workshop.pyiron.org/NFDI-summerschool-2026/0-python.html#module)
* [executorlib](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html)
  * [Asynchronous Programming](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html#asynchronous-programming)
  * [Workflow](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html#workflow)
  * [Workflow Graph](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html#workflow-graph)
  * [High Performance Computing](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html#high-performance-computing)
  * [Python Workflow Definition](http://workshop.pyiron.org/NFDI-summerschool-2026/1-executorlib.html#python-workflow-definition)
* [pyiron_workflow](http://workshop.pyiron.org/NFDI-summerschool-2026/2-pyiron_workflow.html)
  * [Nodes](http://workshop.pyiron.org/NFDI-summerschool-2026/2-pyiron_workflow.html#nodes)
  * [Workflow](http://workshop.pyiron.org/NFDI-summerschool-2026/2-pyiron_workflow.html#workflow)
  * [Workflow Graph](http://workshop.pyiron.org/NFDI-summerschool-2026/2-pyiron_workflow.html#workflow-graph)
  * [Python Workflow Definition](http://workshop.pyiron.org/NFDI-summerschool-2026/2-pyiron_workflow.html#python-workflow-definition)
* [pyironflow](http://workshop.pyiron.org/NFDI-summerschool-2026/3-pyironflow.html)
  * [Nodes](http://workshop.pyiron.org/NFDI-summerschool-2026/3-pyironflow.html#nodes)
  * [Workflow](http://workshop.pyiron.org/NFDI-summerschool-2026/3-pyironflow.html#workflow)
  * [Visual Editor](http://workshop.pyiron.org/NFDI-summerschool-2026/3-pyironflow.html#visual-editor)
  * [Reload Workflow](http://workshop.pyiron.org/NFDI-summerschool-2026/3-pyironflow.html#reload-workflow)
* [Application: ASSYST Method](http://workshop.pyiron.org/NFDI-summerschool-2026/4-assyst.html)
  * [Background](http://workshop.pyiron.org/NFDI-summerschool-2026/4-assyst.html#background)
  * [Spacegroup Sampling](http://workshop.pyiron.org/NFDI-summerschool-2026/4-assyst.html#spacegroup-sampling)
  * [Full Workflow for a Small Structure Set](http://workshop.pyiron.org/NFDI-summerschool-2026/4-assyst.html#full-workflow-for-a-small-structure-set)
  * [Precomputed Full Workflow with Large Structure Set](http://workshop.pyiron.org/NFDI-summerschool-2026/4-assyst.html#precomputed-full-workflow-with-large-structure-set)
* [Application: Fit MLIP](http://workshop.pyiron.org/NFDI-summerschool-2026/5-fitting.html)
  * [Loading and Analyzing the dataset](http://workshop.pyiron.org/NFDI-summerschool-2026/5-fitting.html#loading-and-analyzing-the-dataset)
  * [Split the dataset into training and test](http://workshop.pyiron.org/NFDI-summerschool-2026/5-fitting.html#split-the-dataset-into-training-and-test)
  * [Define and specify the configuration of the ACE potential](http://workshop.pyiron.org/NFDI-summerschool-2026/5-fitting.html#define-and-specify-the-configuration-of-the-ace-potential)
  * [Linear fitting](http://workshop.pyiron.org/NFDI-summerschool-2026/5-fitting.html#linear-fitting)
  * [Workflow For Fitting and Validating the Potential](http://workshop.pyiron.org/NFDI-summerschool-2026/5-fitting.html#workflow-for-fitting-and-validating-the-potential)
* [Summary](http://workshop.pyiron.org/NFDI-summerschool-2026/SUMMARY.html)

## Getting Started
The tutorial can be run without any local installation via the Binder badge above. To run it locally instead:
```
conda env create -n nfdi-summerschool-2026 -f environment.yml
conda activate nfdi-summerschool-2026
jupyter lab
```
Then open the notebooks in order, starting with [`0-python.ipynb`](0-python.ipynb).

## Support & Contribution
This tutorial is developed and maintained on GitHub at [pyiron-workshop/NFDI-summerschool-2026](https://github.com/pyiron-workshop/NFDI-summerschool-2026). Issues and pull requests are welcome.
