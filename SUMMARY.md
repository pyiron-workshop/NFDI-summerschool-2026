# Summary

Every notebook in this tutorial computed the same quantity — the Young's modulus of a steel specimen from a tensile test — or, in the last two notebooks, applied the same thinking to a genuine materials-science research pipeline. What changed from notebook to notebook was never *what* was computed, but *how explicitly* the procedure that computed it was represented. That progression is the actual subject of this tutorial; pyiron, executorlib and pyironflow are one implementation of it.

## What each notebook added

| Notebook | What it introduced |
| --- | --- |
| [`0-python.ipynb`](0-python.ipynb) | The same analysis as a script, then as functions, then as a module (`workflow.py`). A function already has inputs, an operation and outputs — the raw material a workflow node is built from. |
| [`2-pyiron_workflow.ipynb`](2-pyiron_workflow.ipynb) | Those functions wrapped, unchanged, as `pyiron_workflow` nodes and wired into an explicit, inspectable dependency graph. Saving that graph as a [Python Workflow Definition](https://pythonworkflow.github.io/python-workflow-definition/) makes the *procedure*, not only the *result*, findable, accessible, interoperable and reusable. |
| [`1-executorlib.ipynb`](1-executorlib.ipynb) | The same functions as asynchronous tasks, submitted to an executor whose dependency graph is implicit in how `Future` objects are passed around. Swapping `SingleNodeExecutor` for `SlurmClusterExecutor` moves the same workflow onto an HPC cluster without changing what it computes — scale is a property of the execution backend, not the workflow. |
| [`3-pyironflow.ipynb`](3-pyironflow.ipynb) | The same `pyiron_workflow` graph, built, run and reloaded entirely through a drag-and-drop canvas — the same underlying object, a different interface for a different audience. |
| [`4-assyst.ipynb`](4-assyst.ipynb) | The same node-and-edge structure applied to a real, multi-stage pipeline: sampling candidate structures, relaxing them, and perturbing them to generate training data for a machine-learning interatomic potential. |
| [`5-fitting.ipynb`](5-fitting.ipynb) | The pipeline's final stage: turning that training data into a validated ACE potential, with the dependency graph making explicit that validation happens on data the potential was never fitted on. |

## What you should take away

- **Scientific results are produced by procedures, not by individual software commands.** The number at the end of a notebook is rarely the whole story; the sequence of operations that produced it is.
- **Functions** make individual operations reusable — independently of any workflow tool.
- **Workflows** make the dependencies between operations explicit, instead of leaving them implicit in the order notebook cells happen to have been run.
- **Workflow engines** — code-driven (`pyiron_workflow`), visual (`pyironflow`) or executor-based (`executorlib`) — build, execute, inspect and scale the same underlying workflow. Which one to reach for is a question of audience and scale, not of which one is "correct".
- **Provenance**, captured as an explicit, saved workflow rather than left implicit in a notebook, is what makes a result reproducible — and a workflow is not automatically FAIR simply because it was built with one of these tools; it has to actually be described, saved and shared.
- **Interoperable workflow descriptions**, such as the Python Workflow Definition, reduce how much a result depends on any one piece of software, letting a workflow built with one engine run on another.
- **Scale is a consequence of structure.** Once a procedure is an explicit workflow rather than a script tied to one machine and one run, moving it from a laptop to an HPC cluster — or from one calculation to a parameter study of thousands — is a change of execution backend, not a rewrite.

## From concept to application

The first four notebooks built the same small example four ways to isolate one idea at a time. The last two notebooks dropped the training wheels: [`4-assyst.ipynb`](4-assyst.ipynb) and [`5-fitting.ipynb`](5-fitting.ipynb) are a real research workflow, end to end — from deciding which structures to compute, through generating and labelling them, to fitting and validating a machine-learning potential on the result. Every node in those two notebooks is still just a function with explicit inputs and outputs, wired into a graph, exactly as in [`2-pyiron_workflow.ipynb`](2-pyiron_workflow.ipynb) — nothing new had to be learned to go from a four-step tutorial example to a multi-stage research pipeline.

## Transfer to your research

Before you close this tutorial, revisit the exercise at the end of [`3-pyironflow.ipynb`](3-pyironflow.ipynb): take a procedure from your own work, write down its individual steps, and mark their inputs, outputs, parameters, dependencies and software. That diagram is already a workflow. Whether you go on to build it with pyiron, with a different engine, or on paper for now, the habit of making a procedure explicit — rather than leaving it implicit in a script or a sequence of manual steps — is the transferable skill this tutorial was actually about.

## Where to go from here

- [`pyiron_workflow` documentation](https://pyiron-workflow.readthedocs.io/en/latest/)
- [`executorlib` documentation](https://executorlib.readthedocs.io/en/latest/)
- [`pyironflow` repository](https://github.com/pyiron/pyironFlow)
- [Python Workflow Definition](https://pythonworkflow.github.io/python-workflow-definition/)
- [pyiron project](https://pyiron.org/)
